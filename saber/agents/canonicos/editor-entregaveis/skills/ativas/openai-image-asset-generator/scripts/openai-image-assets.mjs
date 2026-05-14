#!/usr/bin/env node
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { basename, dirname, extname, join } from "node:path";

const DEFAULT_BASE_URL = process.env.OPENAI_BASE_URL || "https://api.openai.com/v1";
const DEFAULT_MODEL = process.env.OPENAI_IMAGE_MODEL || "gpt-image-2";

const ASPECT_SIZES = {
  "16:9": "1536x864",
  "9:16": "864x1536",
  "1:1": "1024x1024",
  "4:5": "1024x1280",
  "1.91:1": "1536x804",
};

const PRESETS = {
  "cutout-person": {
    background: "transparent",
    suffix:
      "Generic non-identifiable person, isolated transparent background, clean studio lighting, crisp edges, no text, no logo, ready for compositing.",
  },
  "cutout-object": {
    background: "transparent",
    suffix:
      "Single isolated object, transparent background, product-photo quality, soft controlled shadow, clean edges, no text, no invented logo.",
  },
  "slide-background": {
    background: "auto",
    suffix:
      "Abstract premium presentation background, subtle texture, strong negative space for title and cards, no text, no logo, design-system friendly.",
  },
  "paper-texture": {
    background: "auto",
    suffix:
      "Editorial paper texture, subtle fibers, low contrast, usable behind text overlays, no words, no central object, seamless design feel.",
  },
  "textured-gradient": {
    background: "auto",
    suffix:
      "Textured gradient with fine grain, soft depth, modern design background, no text, no icons, ready for slide or creative composition.",
  },
  icon: {
    background: "transparent",
    suffix:
      "Simple geometric icon, transparent background, high contrast, no words, no brand marks, clean vector-like silhouette.",
  },
  "ad-visual": {
    background: "auto",
    suffix:
      "Campaign key visual, conceptual, no factual claims, no third-party marks, no real identifiable person, composition leaves room for copy overlay.",
  },
};

function parseArgs(argv) {
  const [command, ...rest] = argv;
  const args = { _: [] };
  for (let i = 0; i < rest.length; i += 1) {
    const token = rest[i];
    if (!token.startsWith("--")) {
      args._.push(token);
      continue;
    }
    const key = token.slice(2);
    const next = rest[i + 1];
    if (!next || next.startsWith("--")) {
      args[key] = true;
    } else {
      args[key] = next;
      i += 1;
    }
  }
  return { command, args };
}

function apiKey() {
  // OPENAI_IMAGE_API_KEY: só Images API — no Paperclip, use isto no adapter env para o Codex
  // continuar em assinatura/subscription (OPENAI_API_KEY vazio no processo do adapter).
  const key = (process.env.OPENAI_IMAGE_API_KEY || process.env.OPENAI_API_KEY || "").trim();
  if (!key) {
    throw new Error(
      "Missing API key. Set OPENAI_IMAGE_API_KEY (recomendado no Paperclip com Codex por assinatura) or OPENAI_API_KEY for CLI. Do not commit keys.",
    );
  }
  return key;
}

function headers(extra = {}) {
  return { Authorization: `Bearer ${apiKey()}`, ...extra };
}

function sizeFrom(args) {
  if (args.size) return args.size;
  if (args.aspect && ASPECT_SIZES[args.aspect]) return ASPECT_SIZES[args.aspect];
  return "auto";
}

function promptFrom(args) {
  if (!args.prompt) throw new Error("Missing --prompt");
  const preset = args.preset ? PRESETS[args.preset] : null;
  const brand = args.brand ? `Brand/design direction: ${args.brand}.` : "";
  const suffix = preset ? preset.suffix : "";
  return [args.prompt, brand, suffix].filter(Boolean).join("\n\n");
}

async function ensureDir(path) {
  await mkdir(dirname(path), { recursive: true });
}

async function saveImagePayload(item, outPath) {
  await ensureDir(outPath);
  if (item.b64_json) {
    await writeFile(outPath, Buffer.from(item.b64_json, "base64"));
    return outPath;
  }
  if (item.url) {
    const response = await fetch(item.url);
    if (!response.ok) throw new Error(`Failed to download image URL: ${response.status}`);
    await writeFile(outPath, Buffer.from(await response.arrayBuffer()));
    return outPath;
  }
  throw new Error("Image response did not include b64_json or url");
}

async function requestJson(path, options) {
  const response = await fetch(`${DEFAULT_BASE_URL}${path}`, options);
  const text = await response.text();
  let json;
  try {
    json = text ? JSON.parse(text) : {};
  } catch {
    json = { raw: text };
  }
  if (!response.ok) {
    throw new Error(`${path} failed with ${response.status}: ${JSON.stringify(json, null, 2)}`);
  }
  return json;
}

async function generate(args) {
  const preset = args.preset ? PRESETS[args.preset] : null;
  const body = {
    model: args.model || DEFAULT_MODEL,
    prompt: promptFrom(args),
    size: sizeFrom(args),
    n: Number(args.n || 1),
  };
  if (args.quality) body.quality = args.quality;
  if (args.output_format) body.output_format = args.output_format;
  if (args.background || preset?.background) body.background = args.background || preset.background;

  const json = await requestJson("/images/generations", {
    method: "POST",
    headers: headers({ "Content-Type": "application/json" }),
    body: JSON.stringify(body),
  });

  const out = args.out || `outputs/${args.preset || "image"}-${Date.now()}.png`;
  const outputs = [];
  for (let i = 0; i < json.data.length; i += 1) {
    const target = json.data.length === 1 ? out : withIndex(out, i + 1);
    outputs.push(await saveImagePayload(json.data[i], target));
  }
  console.log(JSON.stringify({ outputs }, null, 2));
}

function withIndex(path, index) {
  const ext = extname(path) || ".png";
  return `${path.slice(0, -ext.length)}-${String(index).padStart(2, "0")}${ext}`;
}

async function edit(args) {
  if (!args.image) throw new Error("Missing --image");
  const preset = args.preset ? PRESETS[args.preset] : null;
  const form = new FormData();
  form.append("model", args.model || DEFAULT_MODEL);
  form.append("prompt", promptFrom(args));
  form.append("size", sizeFrom(args));
  form.append("n", String(Number(args.n || 1)));
  if (args.quality) form.append("quality", args.quality);
  if (args.output_format) form.append("output_format", args.output_format);
  if (args.background || preset?.background) form.append("background", args.background || preset.background);
  await appendFile(form, "image", args.image);
  if (args.mask) await appendFile(form, "mask", args.mask);

  const json = await requestJson("/images/edits", {
    method: "POST",
    headers: headers(),
    body: form,
  });

  const out = args.out || `outputs/edit-${Date.now()}.png`;
  const outputs = [];
  for (let i = 0; i < json.data.length; i += 1) {
    const target = json.data.length === 1 ? out : withIndex(out, i + 1);
    outputs.push(await saveImagePayload(json.data[i], target));
  }
  console.log(JSON.stringify({ outputs }, null, 2));
}

async function appendFile(form, key, path) {
  const bytes = await readFile(path);
  const type = mimeFrom(path);
  form.append(key, new Blob([bytes], { type }), basename(path));
}

function mimeFrom(path) {
  const ext = extname(path).toLowerCase();
  if (ext === ".jpg" || ext === ".jpeg") return "image/jpeg";
  if (ext === ".webp") return "image/webp";
  return "image/png";
}

async function batchPrepare(args) {
  if (!args.input) throw new Error("Missing --input JSON file");
  const rows = JSON.parse(await readFile(args.input, "utf8"));
  if (!Array.isArray(rows)) throw new Error("--input must be a JSON array");
  const out = args.out || "outputs/image-batch.jsonl";
  await ensureDir(out);
  const lines = rows.map((row, index) => {
    const prompt = [row.prompt, row.brand ? `Brand/design direction: ${row.brand}.` : "", PRESETS[row.preset]?.suffix || ""]
      .filter(Boolean)
      .join("\n\n");
    return JSON.stringify({
      custom_id: row.id || `image-${String(index + 1).padStart(4, "0")}`,
      method: "POST",
      url: "/v1/responses",
      body: {
        model: row.response_model || args.response_model || "gpt-5.5",
        input: prompt,
        tools: [
          {
            type: "image_generation",
            model: row.model || args.model || DEFAULT_MODEL,
            size: row.size || (row.aspect ? ASPECT_SIZES[row.aspect] : undefined) || args.size || "auto",
            quality: row.quality || args.quality || "high",
            background: row.background || PRESETS[row.preset]?.background || "auto",
          },
        ],
      },
    });
  });
  await writeFile(out, `${lines.join("\n")}\n`);
  console.log(JSON.stringify({ output: out, endpoint: "/v1/responses", requests: rows.length }, null, 2));
}

async function batchCreate(args) {
  if (!args.file) throw new Error("Missing --file JSONL");
  const upload = new FormData();
  upload.append("purpose", "batch");
  const bytes = await readFile(args.file);
  upload.append("file", new Blob([bytes], { type: "application/jsonl" }), basename(args.file));
  const file = await requestJson("/files", { method: "POST", headers: headers(), body: upload });
  const batch = await requestJson("/batches", {
    method: "POST",
    headers: headers({ "Content-Type": "application/json" }),
    body: JSON.stringify({
      input_file_id: file.id,
      endpoint: args.endpoint || "/v1/responses",
      completion_window: args.window || "24h",
      metadata: { kind: "image-assets" },
    }),
  });
  console.log(JSON.stringify(batch, null, 2));
}

async function batchStatus(args) {
  if (!args.id) throw new Error("Missing --id");
  const batch = await requestJson(`/batches/${args.id}`, { method: "GET", headers: headers() });
  console.log(JSON.stringify(batch, null, 2));
}

async function batchDownload(args) {
  if (!args.id) throw new Error("Missing --id");
  const batch = await requestJson(`/batches/${args.id}`, { method: "GET", headers: headers() });
  if (!batch.output_file_id) {
    console.log(JSON.stringify({ status: batch.status, message: "No output_file_id yet" }, null, 2));
    return;
  }
  const response = await fetch(`${DEFAULT_BASE_URL}/files/${batch.output_file_id}/content`, { headers: headers() });
  if (!response.ok) throw new Error(`Failed to download batch content: ${response.status}`);
  const text = await response.text();
  const outDir = args.out || join("outputs", args.id);
  await mkdir(outDir, { recursive: true });
  await writeFile(join(outDir, "output.jsonl"), text);

  let imageCount = 0;
  for (const line of text.trim().split("\n")) {
    if (!line.trim()) continue;
    const row = JSON.parse(line);
    const images = [];
    collectBase64Images(row, images);
    for (const b64 of images) {
      imageCount += 1;
      await writeFile(join(outDir, `image-${String(imageCount).padStart(4, "0")}.png`), Buffer.from(b64, "base64"));
    }
  }
  console.log(JSON.stringify({ outDir, imageCount }, null, 2));
}

function collectBase64Images(value, acc) {
  if (!value || typeof value !== "object") return;
  if (typeof value.b64_json === "string") acc.push(value.b64_json);
  if (typeof value.image_base64 === "string") acc.push(value.image_base64);
  if (value.type === "image_generation_call" && typeof value.result === "string") acc.push(value.result);
  for (const child of Array.isArray(value) ? value : Object.values(value)) collectBase64Images(child, acc);
}

function usage() {
  console.log(`Usage:
  generate --prompt "..." [--preset slide-background] [--aspect 16:9] [--out path.png]
  edit --image input.png --prompt "..." [--mask mask.png] [--preset cutout-object] [--out path.png]
  batch-prepare --input prompts.json --out batch.jsonl
  batch-create --file batch.jsonl
  batch-status --id batch_...
  batch-download --id batch_... --out outputs/batch
`);
}

const { command, args } = parseArgs(process.argv.slice(2));
try {
  if (command === "generate") await generate(args);
  else if (command === "edit") await edit(args);
  else if (command === "batch-prepare") await batchPrepare(args);
  else if (command === "batch-create") await batchCreate(args);
  else if (command === "batch-status") await batchStatus(args);
  else if (command === "batch-download") await batchDownload(args);
  else usage();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
