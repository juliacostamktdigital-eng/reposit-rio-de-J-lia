(() => {
  // js/store.js
  var state = {
    workflow: null,
    manifest: null,
    selectedId: null,
    /** Macro cuja camada de micro/entregas está aberta em overlay (mastermind só). */
    microsPeekMacroId: null,
    inspectorExpanded: false,
    pan: { x: 0, y: 0 },
    zoom: 1,
    isPanning: false,
    panStart: { x: 0, y: 0 },
    originStart: { x: 0, y: 0 }
  };
  function resolveNode(id) {
    return state.workflow?.byId[id] ?? null;
  }
  function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  // js/engine/asset-layout.js
  function layoutMicroRects(node, assetCount, options = {}) {
    const maxCols = options.maxCols ?? 2;
    const gap = options.gap ?? 10;
    const rowGap = options.rowGap ?? 10;
    const topGap = options.topGap ?? 22;
    const minW = options.minW ?? 80;
    const innerW = node.w - 4;
    const rects = [];
    let index = 0;
    let y = node.y + node.h + topGap;
    const rowH = options.rowH ?? 76;
    while (index < assetCount) {
      const remaining = assetCount - index;
      let cols = Math.min(maxCols, remaining);
      while (cols > 1 && (innerW - (cols - 1) * gap) / cols < minW - 1e-6) {
        cols--;
      }
      cols = Math.max(1, cols);
      let w = (innerW - (cols - 1) * gap) / cols;
      w = Math.min(152, w);
      const rowW = cols * w + (cols - 1) * gap;
      const x0 = node.x + (node.w - rowW) / 2;
      for (let c = 0; c < cols; c++) {
        rects.push({ x: x0 + c * (w + gap), y, w, h: rowH });
        index++;
        if (index >= assetCount) break;
      }
      y += rowH + rowGap;
    }
    return rects;
  }
  function bottomIncludingMicroStrip(macro, microCount, options = {}) {
    const stripBottomPad = options.stripBottomPad ?? 36;
    let b = macro.y + (macro.h || 190);
    if (!microCount) return b;
    const rects = layoutMicroRects(macro, microCount, options);
    const lastBottom = Math.max(...rects.map((r) => r.y + r.h));
    return Math.max(b, lastBottom) + stripBottomPad;
  }
  function normalizeAssetEntry(raw, parentId, idx) {
    if (typeof raw === "string") return { id: `${parentId}__asset_${idx}`, label: raw };
    return {
      id: raw.id || `${parentId}__asset_${idx}`,
      label: raw.label || raw.title || raw.name || "?",
      title: raw.title || raw.label || raw.name || "?",
      note: raw.note || raw.summary || raw.definitionOfDone || "",
      kind: raw.kind || raw.type || "",
      order: raw.order ?? idx + 1,
      required: raw.required,
      statusInJourney: raw.statusInJourney || "",
      owner: raw.owner || "",
      whenCreated: raw.whenCreated || "",
      inputs: raw.inputs || [],
      contents: raw.contents || [],
      outputs: raw.outputs || [],
      definitionOfDone: raw.definitionOfDone || "",
      n2Evidence: raw.n2Evidence || "",
      n3Use: raw.n3Use || "",
      docPath: raw.docPath || raw.doc?.path || "",
      aiSummary: raw.aiSummary || ""
    };
  }

  // js/engine/migrate.js
  var MACROS_TIER_ROWS = [
    ["s0-project", "s1-classify", "s2-diagnose", "s3-os", "s4-assets"],
    ["s5-tracking", "s6-run", "s7-audit"],
    ["s8-growth", "s9-library", "s10-rebrief"]
  ];
  var BOTTOM_ROW_IDS = ["p-packs", "p-examples", "c1-operational", "c2-performance", "c3-learning"];
  function macroTierIndex(id) {
    for (let i = 0; i < MACROS_TIER_ROWS.length; i++) {
      if (MACROS_TIER_ROWS[i].includes(id)) return i;
    }
    if (BOTTOM_ROW_IDS.includes(id)) return 3;
    return 0;
  }
  function orderInTier(id) {
    const t = macroTierIndex(id);
    const merge = t < 3 ? MACROS_TIER_ROWS[t] : BOTTOM_ROW_IDS;
    const idx = merge.indexOf(id);
    return idx < 0 ? 0 : idx;
  }
  function migrateLegacyToMastermind(data, { splitMicrosFromAssets = true } = {}) {
    const macros = [];
    const micros = [];
    for (const raw of data.nodes || []) {
      const { assets = [], ...rest } = raw;
      const macro = {
        ...rest,
        role: "macro",
        tier: macroTierIndex(raw.id),
        orderInTier: orderInTier(raw.id),
        assets: []
      };
      if (splitMicrosFromAssets && assets.length) {
        assets.forEach((a, idx) => {
          const n = normalizeAssetEntry(a, macro.id, idx);
          micros.push({
            id: n.id,
            parentId: macro.id,
            type: "micro",
            role: "micro",
            number: `\xB7`,
            phase: "Entrega",
            title: n.label,
            summary: n.note || "",
            tags: [],
            inputs: [],
            outputs: [],
            evidence: "",
            tone: macro.tone || "red",
            tier: -1,
            w: 110,
            h: 76
          });
        });
      } else {
        macro.assets = assets;
      }
      macros.push(macro);
    }
    const edges = [...data.edges || []];
    const bonds = [];
    if (splitMicrosFromAssets) {
      for (const m of micros) {
        bonds.push({
          id: `bond__${m.id}__${m.parentId}`,
          kind: "bond",
          from: m.id,
          to: m.parentId,
          label: "",
          order: ""
        });
      }
    }
    return {
      schema: "mastermind-v2",
      version: data.version,
      title: data.title,
      date: data.date,
      source: data.source,
      canvas: { ...data.canvas || {} },
      groups: data.groups || [],
      macros,
      micros,
      edges,
      bonds
    };
  }

  // js/engine/layout-linear-spine.js
  var DEFAULT_MAIN_MACRO_ORDER = [
    "s0-project",
    "s1-classify",
    "s2-diagnose",
    "s3-os",
    "s4-assets",
    "s5-tracking",
    "s6-run",
    "s7-audit",
    "s8-growth",
    "s9-library",
    "s10-rebrief"
  ];
  var DEFAULT_BOTTOM_MACRO_ORDER = [
    "p-packs",
    "p-examples",
    "c1-operational",
    "c2-performance",
    "c3-learning"
  ];
  function microByParentCount(workflow) {
    const counts = {};
    for (const u of workflow.micros || []) {
      counts[u.parentId] = (counts[u.parentId] || 0) + 1;
    }
    return counts;
  }
  function placeRow(workflow, list, tierY, startX, gap, microOpts, tierMicroCount) {
    let x = startX;
    let footprintBottom = tierY;
    for (const macro of list) {
      macro.x = x;
      macro.y = tierY;
      x += (macro.w || 220) + gap;
      const nMicro = tierMicroCount[macro.id] || 0;
      const siblings = (workflow.micros || []).filter((u) => u.parentId === macro.id).sort((a, b) => a.id.localeCompare(b.id));
      const rects = layoutMicroRects(macro, siblings.length, microOpts);
      siblings.forEach((mi, i) => {
        const r = rects[i];
        mi.x = r.x;
        mi.y = r.y;
        mi.w = r.w;
        mi.h = r.h;
      });
      footprintBottom = Math.max(footprintBottom, bottomIncludingMicroStrip(macro, nMicro, microOpts));
    }
    return { nextX: x, footprintBottom };
  }
  function placeBottomNotes(list, tierY, startX, gap) {
    let x = startX;
    for (const macro of list) {
      macro.x = x;
      macro.y = tierY;
      x += (macro.w || 260) + gap;
    }
  }
  function applyLinearSpineLayout(workflow, model = {}) {
    const gap = model.columnGap ?? 104;
    const tierGap = model.verticalTierGap ?? 96;
    const bottomRowOffsetFromMain = typeof model.bottomRowOffsetFromMain === "number" ? model.bottomRowOffsetFromMain : null;
    const baseStartY = model.tierBaseStartY ?? 138;
    const marginLeft = model.marginLeftMain ?? 88;
    const mainOrder = model.mainMacroOrder ?? DEFAULT_MAIN_MACRO_ORDER;
    const bottomOrder = model.bottomMacrosOrder ?? model.tier3BottomMacrosOrder ?? DEFAULT_BOTTOM_MACRO_ORDER;
    const microOpts = {
      ...model.microLayout || {},
      stripBottomPad: model.microStripBottomPad ?? 40
    };
    const tierMicroCount = microByParentCount(workflow);
    const byId = new Map((workflow.macros || []).map((m) => [m.id, m]));
    const mainMacros = mainOrder.map((id) => byId.get(id)).filter(Boolean);
    const bottomMacros = bottomOrder.map((id) => byId.get(id)).filter(Boolean);
    const placed = new Set([...mainMacros, ...bottomMacros].map((m) => m.id));
    let orphans = (workflow.macros || []).filter((m) => !placed.has(m.id));
    orphans = orphans.sort((a, b) => `${a.title}`.localeCompare(`${b.title}`));
    const firstFootprint = placeRow(
      workflow,
      mainMacros,
      baseStartY,
      marginLeft,
      gap,
      microOpts,
      tierMicroCount
    );
    let tierCursorY = firstFootprint.footprintBottom + tierGap;
    if (bottomRowOffsetFromMain !== null) {
      const mainBottom = Math.max(
        ...mainMacros.map((macro) => macro.y + (macro.h || 190)),
        baseStartY
      );
      tierCursorY = mainBottom + bottomRowOffsetFromMain;
    }
    placeBottomNotes([...bottomMacros, ...orphans], tierCursorY, marginLeft, gap);
  }

  // js/engine/group-bounds.js
  function bboxMacroAndChildren(workflow, macroId) {
    const macro = (workflow.macros || []).find((m) => m.id === macroId);
    if (!macro) return null;
    let minX = macro.x;
    let minY = macro.y;
    let maxX = macro.x + (macro.w || 0);
    let maxY = macro.y + (macro.h || 0);
    for (const u of workflow.micros || []) {
      if (u.parentId !== macroId) continue;
      minX = Math.min(minX, u.x || 0);
      minY = Math.min(minY, u.y || 0);
      maxX = Math.max(maxX, (u.x || 0) + (u.w || 0));
      maxY = Math.max(maxY, (u.y || 0) + (u.h || 0));
    }
    return { minX, minY, maxX, maxY };
  }
  function unionBoxes(boxes) {
    if (!boxes.length) return null;
    return boxes.reduce(
      (acc, b) => ({
        minX: Math.min(acc.minX, b.minX),
        minY: Math.min(acc.minY, b.minY),
        maxX: Math.max(acc.maxX, b.maxX),
        maxY: Math.max(acc.maxY, b.maxY)
      }),
      boxes[0]
    );
  }
  var DEFAULT_LABEL_RESERVE_Y = 56;
  function syncGroupBounds(workflow, options = {}) {
    const pad = options.groupPadding ?? 28;
    const labelReserve = options.groupLabelReserveY ?? DEFAULT_LABEL_RESERVE_Y;
    const minSize = options.groupMinSize ?? 100;
    for (const g of workflow.groups || []) {
      const ids = g.includeMacroIds;
      if (!Array.isArray(ids) || ids.length === 0) continue;
      const boxes = ids.map((id) => bboxMacroAndChildren(workflow, id)).filter(Boolean);
      const u = unionBoxes(boxes);
      if (!u) continue;
      g.x = Math.round(u.minX - pad);
      g.y = Math.round(u.minY - pad - labelReserve);
      g.w = Math.round(u.maxX - u.minX + 2 * pad);
      g.h = Math.round(u.maxY - u.minY + 2 * pad + labelReserve);
      g.w = Math.max(g.w, minSize);
      g.h = Math.max(g.h, minSize);
    }
  }

  // js/engine/normalize.js
  function assetIndexFromMicroId(id) {
    const m = String(id).match(/__asset_(\d+)$/);
    return m ? parseInt(m[1], 10) : 0;
  }
  function layoutMicrosUnderMacros(workflow, microOpts = {}) {
    const micros = workflow.micros || [];
    if (!micros.length) return;
    const byParent = /* @__PURE__ */ new Map();
    for (const u of micros) {
      if (!u.parentId) continue;
      if (!byParent.has(u.parentId)) byParent.set(u.parentId, []);
      byParent.get(u.parentId).push(u);
    }
    for (const [, list] of byParent) {
      const parentNeeds = list.some(
        (u) => typeof u.x !== "number" || typeof u.y !== "number"
      );
      if (!parentNeeds) continue;
      list.sort((a, b) => assetIndexFromMicroId(a.id) - assetIndexFromMicroId(b.id));
      const macro = workflow.macros?.find((m) => m.id === list[0]?.parentId);
      if (!macro) continue;
      const rects = layoutMicroRects(macro, list.length, microOpts);
      list.forEach((mi, i) => {
        const r = rects[i];
        if (!r) return;
        mi.x = r.x;
        mi.y = r.y;
        mi.w = r.w;
        mi.h = r.h;
      });
    }
  }
  function assignMicroStepIndex(workflow) {
    const micros = workflow.micros || [];
    const byParent = /* @__PURE__ */ new Map();
    for (const m of micros) {
      if (!m.parentId) continue;
      if (!byParent.has(m.parentId)) byParent.set(m.parentId, []);
      byParent.get(m.parentId).push(m);
    }
    for (const [, list] of byParent) {
      list.sort((a, b) => a.y !== b.y ? a.y - b.y : a.x - b.x);
      list.forEach((m, i) => {
        m.microStep = i + 1;
      });
    }
  }
  function appendMicroSequenceEdges(workflow) {
    const micros = workflow.micros || [];
    if (!micros.length) return;
    const byParent = /* @__PURE__ */ new Map();
    for (const m of micros) {
      if (!m.parentId) continue;
      if (!byParent.has(m.parentId)) byParent.set(m.parentId, []);
      byParent.get(m.parentId).push(m);
    }
    const rowTol = 10;
    for (const [, list] of byParent) {
      const sorted = [...list].sort((a, b) => a.y !== b.y ? a.y - b.y : a.x - b.x);
      for (let i = 0; i < sorted.length - 1; i++) {
        const a = sorted[i];
        const b = sorted[i + 1];
        if (Math.abs(a.y - b.y) > rowTol) continue;
        if (b.x <= a.x + 2) continue;
        workflow.renderEdges.push({
          id: `micro-seq:${a.id}:${b.id}`,
          kind: "micro-seq",
          from: a.id,
          to: b.id
        });
      }
    }
  }
  function appendExplicitMicroEdges(workflow) {
    const extras = workflow.microEdges;
    if (!Array.isArray(extras) || extras.length === 0) return;
    const existing = new Set(
      (workflow.renderEdges || []).filter((e) => e.kind === "micro-seq").map((e) => `${e.from}|${e.to}`)
    );
    for (const raw of extras) {
      const from = raw.from;
      const to = raw.to;
      if (!from || !to) continue;
      const key = `${from}|${to}`;
      if (existing.has(key)) continue;
      workflow.renderEdges.push({
        id: raw.id ?? `micro-seq:${from}->${to}`,
        kind: "micro-seq",
        from,
        to,
        label: raw.label ?? "",
        order: raw.order ?? ""
      });
      existing.add(key);
    }
  }
  function expandCanvasBounds(workflow, paddingRight = 120, paddingBottom = 160) {
    const micros = workflow.micros || [];
    let maxR = 200;
    let maxB = 200;
    for (const n of [...workflow.macros, ...micros]) {
      maxR = Math.max(maxR, (n.x || 0) + (n.w || 0));
      maxB = Math.max(maxB, (n.y || 0) + (n.h || 0));
    }
    for (const g of workflow.groups || []) {
      if (typeof g.x === "number" && typeof g.w === "number") {
        maxR = Math.max(maxR, g.x + g.w);
      }
      if (typeof g.y === "number" && typeof g.h === "number") {
        maxB = Math.max(maxB, g.y + g.h);
      }
    }
    workflow.canvas = workflow.canvas || {};
    workflow.canvas.width = Math.max(workflow.canvas.width || 0, maxR + paddingRight);
    workflow.canvas.height = Math.max(workflow.canvas.height || 0, maxB + paddingBottom);
  }
  function buildWorkflowView(rawPayload, versionMeta) {
    const engine = versionMeta.engine || {};
    let workflow;
    if (rawPayload.schema === "mastermind-v2" && rawPayload.macros) {
      workflow = JSON.parse(JSON.stringify(rawPayload));
    } else {
      workflow = migrateLegacyToMastermind(rawPayload, {
        splitMicrosFromAssets: engine.splitMicrosFromAssets !== false
      });
    }
    workflow.micros = workflow.micros || [];
    workflow.groups = workflow.groups || [];
    if (workflow.macros?.length) {
      for (const m of workflow.macros) {
        m.role = m.role || "macro";
      }
      for (const u of workflow.micros) {
        u.role = u.role || "micro";
        u.type = u.type || "micro";
      }
    }
    const layoutModel = engine.layoutModel || {};
    if (engine.splitMicrosFromAssets !== false && engine.applyTieredLayoutToMacros !== false) {
      applyLinearSpineLayout(workflow, layoutModel);
    } else if (engine.splitMicrosFromAssets !== false) {
      layoutMicrosUnderMacros(workflow, layoutModel.microLayout || {});
    }
    if (engine.syncGroupBoundsToMacros !== false) {
      syncGroupBounds(workflow, {
        groupPadding: layoutModel.groupPadding,
        groupLabelReserveY: layoutModel.groupLabelReserveY,
        groupMinSize: layoutModel.groupMinSize
      });
    }
    assignMicroStepIndex(workflow);
    workflow.renderEdges = [...workflow.edges || [], ...workflow.bonds || []];
    appendMicroSequenceEdges(workflow);
    appendExplicitMicroEdges(workflow);
    workflow.byId = {};
    for (const n of [...workflow.macros, ...workflow.micros]) {
      workflow.byId[n.id] = n;
    }
    workflow.activeMeta = {
      versionId: versionMeta.id,
      label: versionMeta.label,
      engine
    };
    expandCanvasBounds(workflow);
    return workflow;
  }

  // js/canvas/render-groups.js
  function renderGroups(els2) {
    els2.groups.innerHTML = (state.workflow.groups || []).map(
      (g) => `
      <section
        class="group"
        style="left:${g.x}px; top:${g.y}px; width:${g.w}px; height:${g.h}px"
        aria-label="${g.label}"
      >
        <span class="group__label">${g.label}</span>
      </section>
    `
    ).join("");
  }

  // js/canvas/render-macros.js
  function safe(str) {
    return String(str ?? "").replace(/"/g, "&quot;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  function renderMacros(els2) {
    els2.stepNodes.innerHTML = (state.workflow.macros || []).map((node) => {
      const sel = node.id === state.selectedId ? "is-selected" : "";
      const isNote = node.type === "note";
      const stripOpen = Boolean(state.workflow.micros?.length) && node.id === state.microsPeekMacroId ? " is-micro-strip-open" : "";
      const chips = (node.tags || []).map((t) => `<span class="chip" title="${safe(t)}">${safe(t)}</span>`).join("");
      const noteLines = (node.noteLines || []).map((line) => `<li>${safe(line)}</li>`).join("");
      return `
        <button
          class="node ${isNote ? "node--note" : ""} ${sel}${stripOpen}"
          data-node-id="${node.id}"
          data-role="${node.role || "macro"}"
          data-type="${node.type || "step"}"
          data-tone="${node.tone || "red"}"
          style="left:${node.x}px; top:${node.y}px; --node-w:${node.w}px; --node-h:${node.h}px"
          type="button"
          aria-label="${safe(node.title)}"
        >
          <div class="node__inner">
            <div class="node__meta">
              <span class="node__number">${safe(node.number)}</span>
              <span class="node__kind">${safe(node.phase)}</span>
            </div>
            <h2 class="node__title" title="${safe(node.title)}">${safe(node.title)}</h2>
            <p class="node__summary" title="${safe(node.summary)}">${safe(node.summary)}</p>
            ${isNote && noteLines ? `<ul class="node__note-lines">${noteLines}</ul>` : ""}
            <div class="node__chips">${chips}</div>
          </div>
        </button>
      `;
    }).join("");
  }

  // js/canvas/render-micros.js
  function safe2(str) {
    return String(str ?? "").replace(/"/g, "&quot;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  function microCardHtml(mic, x, y, w, h, selected, stepNum, extraClass = "") {
    const sel = selected ? " is-selected" : "";
    const step = typeof stepNum === "number" ? `<span class="micro-card__step" aria-hidden="true">${stepNum}</span>` : "";
    return `
    <button
      type="button"
      class="micro-card${extraClass}${sel}"
      data-node-id="${mic.id}"
      data-role="${mic.role || "micro"}"
      data-parent-id="${mic.parentId || ""}"
      data-tone="${mic.tone || "red"}"
      style="left:${x}px; top:${y}px; width:${w}px; height:${h}px;"
      title="${safe2(mic.title)}"
      aria-label="${typeof stepNum === "number" ? safe2(`${stepNum}. ${mic.title}`) : safe2(mic.title)}"
    >
      <span class="micro-card__meta">
        ${step}
        <span class="micro-card__dot" aria-hidden="true"></span>
      </span>
      <span class="micro-card__label">${safe2(mic.title)}</span>
    </button>
  `.trim();
  }
  function renderMicros(els2) {
    const useSplit = Boolean(state.workflow.micros?.length);
    const blocks = [];
    if (useSplit) {
      const peek = state.microsPeekMacroId;
      if (!peek) {
        els2.assetCards.innerHTML = "";
        els2.assetCards.setAttribute("aria-hidden", "true");
        return;
      }
      const list = (state.workflow.micros || []).filter((m) => m.parentId === peek).sort((a, b) => (a.microStep || 0) - (b.microStep || 0) || a.y - b.y || a.id.localeCompare(b.id));
      for (const mic of list) {
        blocks.push(
          microCardHtml(
            mic,
            mic.x,
            mic.y,
            mic.w,
            mic.h,
            mic.id === state.selectedId,
            mic.microStep,
            " micro-card--revealed"
          )
        );
      }
      els2.assetCards.innerHTML = blocks.join("");
      els2.assetCards.setAttribute("aria-hidden", blocks.length ? "false" : "true");
      return;
    }
    if (!state.workflow.uiModel?.showCanvasAssetCards) {
      els2.assetCards.innerHTML = "";
      els2.assetCards.setAttribute("aria-hidden", "true");
      return;
    }
    for (const node of state.workflow.macros) {
      const entries = node.assets || [];
      if (!entries.length) continue;
      const normalized = entries.map((a, i) => normalizeAssetEntry(a, node.id, i));
      const rects = layoutMicroRects(node, normalized.length);
      normalized.forEach((asset, i) => {
        const r = rects[i];
        const selected = node.id === state.selectedId;
        const synthetic = {
          id: asset.id,
          parentId: node.id,
          role: "macro-asset",
          tone: node.tone,
          title: asset.label
        };
        blocks.push(microCardHtml(synthetic, r.x, r.y, r.w, r.h, selected, i + 1, ""));
      });
    }
    els2.assetCards.innerHTML = blocks.join("");
    els2.assetCards.setAttribute("aria-hidden", blocks.length ? "false" : "true");
  }

  // js/canvas/render-peek-backdrop.js
  function renderPeekBackdrop(els2) {
    const host = els2.peekBackdrop;
    if (!host || !state.workflow) return;
    const peekId = state.microsPeekMacroId;
    const split = Boolean(state.workflow.micros?.length);
    if (!split || !peekId) {
      host.hidden = true;
      host.setAttribute("aria-hidden", "true");
      host.innerHTML = "";
      return;
    }
    const macro = resolveNode(peekId);
    const microList = (state.workflow.micros || []).filter((m) => m.parentId === peekId);
    if (!macro || !microList.length) {
      host.hidden = true;
      host.innerHTML = "";
      return;
    }
    let minX = macro.x;
    let minY = macro.y;
    let maxX = macro.x + (macro.w || 240);
    let maxY = macro.y + (macro.h || 200);
    for (const u of microList) {
      minX = Math.min(minX, u.x);
      minY = Math.min(minY, u.y);
      maxX = Math.max(maxX, u.x + (u.w || 0));
      maxY = Math.max(maxY, u.y + (u.h || 0));
    }
    const pad = 26;
    minX -= pad;
    minY -= pad;
    maxX += pad;
    maxY += pad;
    const W = state.workflow.canvas.width;
    const H = state.workflow.canvas.height;
    minX = Math.max(0, minX);
    minY = Math.max(0, minY);
    maxX = Math.min(W, maxX);
    maxY = Math.min(H, maxY);
    const bw = Math.max(1, maxX - minX);
    const bh = Math.max(1, maxY - minY);
    const rx = Math.max(4, Math.min(26, bw / 2, bh / 2));
    const uid = `peek_${Date.now()}_${Math.random().toString(36).slice(2, 10)}`;
    const maskId = `${uid}_mask`;
    host.hidden = false;
    host.setAttribute("aria-hidden", "false");
    host.innerHTML = `
    <svg class="peek-svg" width="${W}" height="${H}" aria-hidden="true" focusable="false">
      <defs>
        <mask id="${maskId}">
          <rect width="${W}" height="${H}" fill="white"></rect>
          <rect x="${minX}" y="${minY}" width="${bw}" height="${bh}" rx="${rx}" ry="${rx}" fill="black"></rect>
        </mask>
      </defs>
      <rect class="peek-dim" width="${W}" height="${H}" fill="rgba(17,17,17,0.40)" mask="url(#${maskId})"></rect>
    </svg>
  `;
  }

  // js/canvas/edges.js
  var SIDE = {
    left: "left",
    right: "right",
    top: "top",
    bottom: "bottom"
  };
  var ARROW_OUTSET = 15;
  function midpointOnSide(node, side) {
    if (side === SIDE.left || side === SIDE.right) {
      const x = side === SIDE.left ? node.x : node.x + node.w;
      return { x, y: node.y + node.h / 2 };
    }
    const y = side === SIDE.top ? node.y : node.y + node.h;
    return { x: node.x + node.w / 2, y };
  }
  function sideNormal(side) {
    if (side === SIDE.left) return { x: -1, y: 0 };
    if (side === SIDE.right) return { x: 1, y: 0 };
    if (side === SIDE.top) return { x: 0, y: -1 };
    return { x: 0, y: 1 };
  }
  function centerOf(node) {
    return { x: node.x + node.w / 2, y: node.y + node.h / 2 };
  }
  function outwardPointFromSide(node, side, distance) {
    const point = midpointOnSide(node, side);
    const normal = sideNormal(side);
    return { x: point.x + normal.x * distance, y: point.y + normal.y * distance };
  }
  function edgePortsDirected(from, to) {
    const fc = centerOf(from);
    const tc = centerOf(to);
    const dx = tc.x - fc.x;
    const dy = tc.y - fc.y;
    const tierY = 72;
    if (dy > tierY) {
      return {
        start: outwardPointFromSide(from, SIDE.bottom, 30),
        meta: { fromSide: SIDE.bottom, toSide: SIDE.top }
      };
    }
    if (dy < -tierY) {
      return {
        start: outwardPointFromSide(from, SIDE.top, 30),
        meta: { fromSide: SIDE.top, toSide: SIDE.bottom }
      };
    }
    if (Math.abs(dx) >= Math.abs(dy)) {
      if (dx >= 0) {
        return {
          start: outwardPointFromSide(from, SIDE.right, 30),
          meta: { fromSide: SIDE.right, toSide: SIDE.left }
        };
      }
      return {
        start: outwardPointFromSide(from, SIDE.left, 30),
        meta: { fromSide: SIDE.left, toSide: SIDE.right }
      };
    }
    if (dy >= 0) {
      return {
        start: outwardPointFromSide(from, SIDE.bottom, 30),
        meta: { fromSide: SIDE.bottom, toSide: SIDE.top }
      };
    }
    return {
      start: outwardPointFromSide(from, SIDE.top, 30),
      meta: { fromSide: SIDE.top, toSide: SIDE.bottom }
    };
  }
  function terminalPointOutside(toNode, toSide, outset = ARROW_OUTSET, lane = 0) {
    const mid = midpointOnSide(toNode, toSide);
    const n = sideNormal(toSide);
    const tangentAlongFace = toSide === SIDE.left || toSide === SIDE.right ? { x: 0, y: 1 } : { x: 1, y: 0 };
    const skewPx = lane * 17;
    return {
      x: mid.x + n.x * outset + tangentAlongFace.x * skewPx,
      y: mid.y + n.y * outset + tangentAlongFace.y * skewPx
    };
  }
  function routeSegmentOrthogonal(from, to, edgeKind = null) {
    const dx = to.x - from.x;
    const dy = to.y - from.y;
    const ax = Math.abs(dx);
    const ay = Math.abs(dy);
    if (ax < 0.5) return [from, to];
    if (ay < 0.5) return [from, to];
    let horizontalFirst = ax >= ay;
    const SUPPORT_DESCEND_DROP = 88;
    if (edgeKind === "support" && dy > SUPPORT_DESCEND_DROP) {
      horizontalFirst = false;
    }
    const bend = horizontalFirst ? { x: to.x, y: from.y } : { x: from.x, y: to.y };
    const sameAsFrom = Math.abs(bend.x - from.x) < 0.5 && Math.abs(bend.y - from.y) < 0.5;
    const sameAsTo = Math.abs(bend.x - to.x) < 0.5 && Math.abs(bend.y - to.y) < 0.5;
    if (sameAsFrom || sameAsTo) return [from, to];
    return [from, bend, to];
  }
  function dedupeConsecutivePoints(points) {
    const out = [];
    for (const p of points) {
      const prev = out[out.length - 1];
      if (!prev || Math.abs(prev.x - p.x) > 0.4 || Math.abs(prev.y - p.y) > 0.4) out.push(p);
    }
    return out;
  }
  function dist(a, b) {
    return Math.hypot(b.x - a.x, b.y - a.y);
  }
  function orthogonalPathWithRoundedCorners(points, radius = 22) {
    const n = points.length;
    if (n < 2) return "";
    if (n === 2) {
      const [a, b] = points;
      return `M ${a.x} ${a.y} L ${b.x} ${b.y}`;
    }
    let cursor = points[0];
    let d = `M ${cursor.x} ${cursor.y}`;
    for (let i = 1; i <= n - 2; i++) {
      const p = points[i];
      const pNext = points[i + 1];
      const segIn = dist(cursor, p);
      const segOut = dist(p, pNext);
      if (segIn < 2 || segOut < 2) {
        d += ` L ${p.x} ${p.y}`;
        cursor = { x: p.x, y: p.y };
        continue;
      }
      const rr = Math.min(radius, segIn / 2 - 0.6, segOut / 2 - 0.6);
      const ux = (p.x - cursor.x) / segIn;
      const uy = (p.y - cursor.y) / segIn;
      const vx = (pNext.x - p.x) / segOut;
      const vy = (pNext.y - p.y) / segOut;
      const dot = ux * vx + uy * vy;
      if (dot > 0.992 || rr < 5) {
        d += ` L ${p.x} ${p.y}`;
        cursor = { x: p.x, y: p.y };
        continue;
      }
      const Ax = p.x - ux * rr;
      const Ay = p.y - uy * rr;
      const Bx = p.x + vx * rr;
      const By = p.y + vy * rr;
      d += ` L ${Ax} ${Ay}`;
      d += ` Q ${p.x} ${p.y} ${Bx} ${By}`;
      cursor = { x: Bx, y: By };
    }
    const last = points[n - 1];
    d += ` L ${last.x} ${last.y}`;
    return d;
  }
  function polylineToSvgPath(points) {
    return points.map((point, index) => `${index === 0 ? "M" : "L"} ${point.x} ${point.y}`).join(" ");
  }
  function routedEdgePoints(edge, from, to) {
    const ek = edge.kind || null;
    if (ek === "micro-seq") {
      return routedMicroSeqPolyline(from, to);
    }
    if (ek === "loop") {
      return routedLoopPolyline(from, to);
    }
    if (ek === "support") {
      return routedSupportBusPolyline(edge, from, to);
    }
    const ports = edgePortsDirected(from, to);
    const manualPoints = (edge.points || []).map(([x, y]) => ({ x, y }));
    const term = terminalPointOutside(to, ports.meta.toSide, ARROW_OUTSET, 0);
    const anchors = [ports.start, ...manualPoints, term];
    const merged = anchors.reduce((points, anchor, index) => {
      if (index === 0) return [anchor];
      const segment = routeSegmentOrthogonal(anchors[index - 1], anchor, ek);
      return [...points, ...segment.slice(1)];
    }, []);
    return dedupeConsecutivePoints(merged);
  }
  function routedLoopPolyline(from, to) {
    const SAME_ROW_TOL = 56;
    const LOOP_PAD = 68;
    const ports = edgePortsDirected(from, to);
    const term = terminalPointOutside(to, ports.meta.toSide, ARROW_OUTSET, 0);
    const start = ports.start;
    const fy = from.y + (from.h || 0) / 2;
    const ty = to.y + (to.h || 0) / 2;
    const sameRowApprox = Math.abs(fy - ty) < SAME_ROW_TOL && Math.abs(from.y - to.y) < SAME_ROW_TOL;
    if (sameRowApprox) {
      const minTop = Math.min(from.y, to.y);
      const busY2 = Math.max(36, minTop - LOOP_PAD);
      const pts2 = [start, { x: start.x, y: busY2 }, { x: term.x, y: busY2 }, term];
      return dedupeConsecutivePoints(pts2);
    }
    const bottomA = Math.max(from.y + (from.h || 200), to.y + (to.h || 200));
    const busY = bottomA + LOOP_PAD;
    const pts = [start, { x: start.x, y: busY }, { x: term.x, y: busY }, term];
    return dedupeConsecutivePoints(pts);
  }
  function routedMicroSeqPolyline(from, to) {
    const midYFrom = from.y + from.h / 2;
    const midYTo = to.y + to.h / 2;
    const rowTol = 18;
    const sameRow = Math.abs(midYFrom - midYTo) < rowTol && Math.abs(from.y - to.y) < rowTol && to.x > from.x + 4;
    if (sameRow) {
      const y = (midYFrom + midYTo) / 2;
      return dedupeConsecutivePoints([
        { x: from.x + from.w, y },
        { x: to.x, y }
      ]);
    }
    const bottomMid = { x: from.x + from.w / 2, y: from.y + from.h };
    const topMid = { x: to.x + to.w / 2, y: to.y };
    if (Math.abs(bottomMid.x - topMid.x) < 10) {
      return dedupeConsecutivePoints([bottomMid, topMid]);
    }
    const midY = (bottomMid.y + topMid.y) / 2;
    return dedupeConsecutivePoints([
      bottomMid,
      { x: bottomMid.x, y: midY },
      { x: topMid.x, y: midY },
      topMid
    ]);
  }
  function routedSupportBusPolyline(edge, from, to) {
    const ports = edgePortsDirected(from, to);
    const term = terminalPointOutside(to, ports.meta.toSide, ARROW_OUTSET, 0);
    const start = ports.start;
    const manualPoints = (edge.points || []).map(([x, y]) => ({ x, y }));
    if (manualPoints.length) {
      const anchors = [start, ...manualPoints, term];
      const merged = anchors.reduce((points, anchor, index) => {
        if (index === 0) return [anchor];
        const segment = routeSegmentOrthogonal(anchors[index - 1], anchor, "support");
        return [...points, ...segment.slice(1)];
      }, []);
      return dedupeConsecutivePoints(merged);
    }
    const nLanes = Math.max(edge._supportLaneCount ?? 1, 1);
    const idx = edge._supportLaneIndex ?? 0;
    const slot = (idx + 1) / (nLanes + 1);
    const minY = Math.min(start.y, term.y);
    const maxY = Math.max(start.y, term.y);
    const span = Math.max(maxY - minY, 96);
    const inset = span * 0.14;
    const busY = minY + inset + Math.max(span - 2 * inset, 8) * slot;
    const pts = [
      start,
      { x: start.x, y: busY },
      { x: term.x, y: busY },
      term
    ];
    return dedupeConsecutivePoints(pts);
  }
  function routedBondPoints(micro, macro) {
    const x = micro.x + micro.w / 2;
    const macroBottom = macro.y + (macro.h || 196);
    const yMidGap = (macroBottom + micro.y) / 2;
    return [
      { x, y: micro.y },
      { x, y: yMidGap }
    ];
  }
  function edgePath(edge, from, to) {
    if (edge.kind === "bond") {
      const pts2 = routedBondPoints(from, to);
      return polylineToSvgPath(pts2);
    }
    const pts = routedEdgePoints(edge, from, to);
    if (edge.kind === "main") {
      return orthogonalPathWithRoundedCorners(pts, 26);
    }
    return polylineToSvgPath(pts);
  }
  function pickLabelSegment(edge, allPoints) {
    const segs = [];
    for (let i = 0; i < allPoints.length - 1; i++) {
      const a = allPoints[i];
      const b = allPoints[i + 1];
      const dx = Math.abs(b.x - a.x);
      const dy = Math.abs(b.y - a.y);
      const len = Math.hypot(dx, dy);
      const horizish = dy < 12 && dx > 32;
      segs.push({ a, b, len, horizish });
    }
    const k = edge.kind || "";
    const prefersHoriz = k === "main" || k === "loop";
    const horizCandidates = prefersHoriz ? segs.filter((s) => s.horizish) : [];
    const pool = horizCandidates.length ? horizCandidates : segs;
    let best = pool[0];
    for (const s of pool) {
      if (s.len > best.len) best = s;
    }
    return best;
  }
  function edgeLabelPosition(edge, from, to) {
    let allPoints;
    if (edge.kind === "bond") {
      allPoints = routedBondPoints(from, to);
    } else {
      allPoints = routedEdgePoints(edge, from, to);
    }
    if (allPoints.length < 2) {
      const p = allPoints[0] || { x: 0, y: 0 };
      return { x: p.x, y: p.y - 14 };
    }
    const { a: aa, b: bb } = pickLabelSegment(edge, allPoints);
    const lx = (aa.x + bb.x) / 2;
    const rowTop = Math.min(from.y, to.y);
    const rowBottom = Math.max(from.y + (from.h || 0), to.y + (to.h || 0));
    const segDy = Math.abs(bb.y - aa.y);
    const horizSeg = segDy < 12;
    const k = edge.kind || "";
    let ly = (aa.y + bb.y) / 2 - 16;
    if (horizSeg && (k === "main" || k === "loop")) {
      const sameRowMacros = Math.abs(from.y - to.y) < 28;
      const midY = (aa.y + bb.y) / 2;
      if (sameRowMacros) {
        ly = rowTop - 20;
      } else if (midY >= rowTop - 6 && midY <= rowBottom + 6) {
        ly = midY - 26;
      } else {
        ly = midY - 18;
      }
    }
    return { x: lx, y: ly };
  }

  // js/canvas/render-edges.js
  var DEFS = `
<defs>
  <marker id="dot" markerWidth="9" markerHeight="9" refX="4.5" refY="4.5" orient="auto" markerUnits="userSpaceOnUse">
    <circle cx="4.5" cy="4.5" r="2.9" fill="#111111"></circle>
  </marker>
  <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M0 0 L12 6 L0 12z" fill="#111111"></path>
  </marker>
  <marker id="dot-support" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto" markerUnits="userSpaceOnUse">
    <circle cx="4" cy="4" r="2.6" fill="#5c5548"></circle>
  </marker>
  <marker id="arrow-support" markerWidth="11" markerHeight="11" refX="9" refY="5.5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M0 0 L11 5.5 L0 11z" fill="#5c5548"></path>
  </marker>
  <marker id="dot-loop" markerWidth="9" markerHeight="9" refX="4.5" refY="4.5" orient="auto" markerUnits="userSpaceOnUse">
    <circle cx="4.5" cy="4.5" r="2.9" fill="#e50914"></circle>
  </marker>
  <marker id="arrow-loop" markerWidth="11" markerHeight="11" refX="9" refY="5.5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M0 0 L11 5.5 L0 11z" fill="#e50914"></path>
  </marker>
  <marker id="dot-bond" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto" markerUnits="userSpaceOnUse">
    <circle cx="3" cy="3" r="2" fill="rgba(17,17,17,0.35)"></circle>
  </marker>
</defs>
`;
  function svgEscape(s) {
    return String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
  }
  function assignSupportLanes(edges) {
    const supports = edges.filter((e) => e.kind === "support");
    supports.sort((a, b) => {
      const ta = resolveNode(a.to);
      const tb = resolveNode(b.to);
      const fa = resolveNode(a.from);
      const fb = resolveNode(b.from);
      if (!ta || !tb || !fa || !fb) return `${a.id}`.localeCompare(`${b.id}`);
      const ay = ta.y + (ta.h || 0) / 2;
      const by = tb.y + (tb.h || 0) / 2;
      if (Math.abs(ay - by) > 12) return ay - by;
      const ax = ta.x + (ta.w || 0) / 2;
      const bx = tb.x + (tb.w || 0) / 2;
      if (Math.abs(ax - bx) > 12) return ax - bx;
      const fax = fa.x + (fa.w || 0) / 2;
      const fbx = fb.x + (fb.w || 0) / 2;
      return fax - fbx;
    });
    supports.forEach((e, i) => {
      e._supportLaneIndex = i;
      e._supportLaneCount = Math.max(supports.length, 1);
    });
  }
  function renderBond(edge, micro, macro) {
    const pts = routedBondPoints(micro, macro);
    const d = pts.map((p, i) => `${i === 0 ? "M" : "L"} ${p.x} ${p.y}`).join(" ");
    const title = `${micro.title || micro.id} \u2192 macro ${macro.number || ""} ${macro.title || ""}`.trim();
    return `<path class="edge-path edge-bond" d="${d}" marker-start="url(#dot-bond)"><title>${svgEscape(title)}</title></path>`;
  }
  function renderMicroSeq(edge, from, to) {
    const d = edgePath(edge, from, to);
    const title = `${from.title || from.id} \u2192 ${to.title || to.id}${edge.label ? `: ${edge.label}` : ""}`.trim();
    let labelEl = "";
    if (edge.label) {
      const lp = edgeLabelPosition(edge, from, to);
      labelEl = `<text class="edge-label edge-label--micro-seq" x="${lp.x}" y="${lp.y}" text-anchor="middle">${svgEscape(edge.label)}</text>`;
    }
    return `
    <path class="edge-path edge-micro-seq" d="${d}"><title>${svgEscape(title)}</title></path>
    ${labelEl}
  `;
  }
  function renderFlowEdge(edge, from, to) {
    const d = edgePath(edge, from, to);
    const lp = edgeLabelPosition(edge, from, to);
    const kind = edge.kind || "support";
    let mStart = "dot-support";
    let mEnd = "arrow-support";
    if (kind === "main") {
      mStart = "dot";
      mEnd = "arrow";
    } else if (kind === "loop") {
      mStart = "dot-loop";
      mEnd = "arrow-loop";
    }
    const showOrder = kind !== "support" && edge.order;
    const showTextLabel = Boolean(edge.label) && kind !== "support";
    const orderEl = showOrder ? `<text class="edge-order edge-order-${kind}" x="${lp.x - 34}" y="${lp.y}" text-anchor="middle">${svgEscape(edge.order)}</text>` : "";
    const labelAnchor = kind === "support" ? "middle" : kind === "loop" ? "middle" : "start";
    const labelDx = kind === "support" ? 0 : kind === "loop" ? 0 : 18;
    const labelDy = kind === "support" ? 14 : kind === "loop" ? -2 : 0;
    const labelEl = showTextLabel ? `<text class="edge-label edge-label--${kind}" x="${lp.x + labelDx}" y="${lp.y + labelDy}" text-anchor="${labelAnchor}">${svgEscape(edge.label)}</text>` : "";
    const pathTitle = `${from.title || edge.from} \u2192 ${to.title || edge.to}${edge.label ? `: ${edge.label}` : ""}`.trim();
    if (kind === "main") {
      return `
    <path class="edge-path edge-main edge-main__ribbon" d="${d}" aria-hidden="true" />
    <path class="edge-path edge-main edge-main__ink" d="${d}" marker-start="url(#${mStart})" marker-end="url(#${mEnd})">
      <title>${svgEscape(pathTitle)}</title>
    </path>
    ${orderEl}
    ${labelEl}
  `;
    }
    return `
    <path class="edge-path edge-${kind}" d="${d}" marker-start="url(#${mStart})" marker-end="url(#${mEnd})">
      <title>${svgEscape(pathTitle)}</title>
    </path>
    ${orderEl}
    ${labelEl}
  `;
  }
  function rankEdge(e) {
    const k = e.kind || "support";
    if (k === "main") return 0;
    if (k === "support") return 1;
    if (k === "loop") return 2;
    if (k === "micro-seq") return 3;
    if (k === "bond") return 5;
    return 2;
  }
  function microChildEdgeVisible(edge) {
    const hasSplitMicros = Boolean(state.workflow.micros?.length);
    if (!hasSplitMicros) return true;
    const peek = state.microsPeekMacroId;
    const k = edge.kind;
    if (k === "bond") {
      const micro = resolveNode(edge.from);
      return Boolean(peek && micro?.parentId === peek);
    }
    if (k === "micro-seq") {
      const from = resolveNode(edge.from);
      return Boolean(peek && from?.parentId === peek);
    }
    return true;
  }
  function renderEdges(els2) {
    const allEdges = [...state.workflow.renderEdges || []];
    assignSupportLanes(allEdges);
    const flowSvg = allEdges.filter((e) => e.kind !== "bond" && e.kind !== "micro-seq").sort((a, b) => rankEdge(a) - rankEdge(b)).map((edge) => {
      const from = resolveNode(edge.from);
      const to = resolveNode(edge.to);
      if (!from || !to) return "";
      return renderFlowEdge(edge, from, to);
    }).join("");
    const microSvg = allEdges.filter((e) => e.kind === "micro-seq" && microChildEdgeVisible(e)).map((edge) => {
      const from = resolveNode(edge.from);
      const to = resolveNode(edge.to);
      if (!from || !to) return "";
      return renderMicroSeq(edge, from, to);
    }).join("");
    const bondSvg = allEdges.filter((e) => e.kind === "bond" && microChildEdgeVisible(e)).map((edge) => {
      const micro = resolveNode(edge.from);
      const macro = resolveNode(edge.to);
      if (!micro || !macro) return "";
      return renderBond(edge, micro, macro);
    }).join("");
    els2.edges.setAttribute("viewBox", `0 0 ${state.workflow.canvas.width} ${state.workflow.canvas.height}`);
    els2.edges.innerHTML = DEFS + flowSvg + microSvg + bondSvg;
  }

  // js/canvas/inspector.js
  function padList(items = []) {
    return items.map((item) => `<li>${item}</li>`).join("");
  }
  function renderGuideList(items = []) {
    if (!items.length) return "<p>-</p>";
    return `<ul>${items.map((item) => `<li>${safe3(item)}</li>`).join("")}</ul>`;
  }
  function safe3(str) {
    return String(str ?? "").replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  function clearDocPreview(els2) {
    if (!els2.sectionDoc) return;
    els2.sectionDoc.hidden = true;
    if (els2.selectedDocPath) els2.selectedDocPath.textContent = "-";
    if (els2.selectedDocContent) els2.selectedDocContent.innerHTML = "";
    if (els2.copyDocMarkdown) {
      els2.copyDocMarkdown.disabled = true;
      els2.copyDocMarkdown.textContent = "Copiar markdown";
      els2.copyDocMarkdown.onclick = null;
    }
    if (els2.playbookSkillsSection) {
      els2.playbookSkillsSection.hidden = true;
      if (els2.playbookSkillsList) {
        els2.playbookSkillsList.innerHTML = "";
        els2.playbookSkillsList.onclick = null;
      }
    }
  }
  function clearAssetModalDoc(els2) {
    if (!els2.assetModalDocSection) return;
    els2.assetModalDocSection.hidden = true;
    if (els2.assetModalDocPath) els2.assetModalDocPath.textContent = "-";
    if (els2.assetModalDocContent) els2.assetModalDocContent.innerHTML = "";
    if (els2.assetModalCopyMarkdown) {
      els2.assetModalCopyMarkdown.disabled = true;
      els2.assetModalCopyMarkdown.textContent = "Copiar markdown";
      els2.assetModalCopyMarkdown.onclick = null;
    }
    if (els2.assetModalSkillsSection) {
      els2.assetModalSkillsSection.hidden = true;
      if (els2.assetModalSkillsList) {
        els2.assetModalSkillsList.innerHTML = "";
        els2.assetModalSkillsList.onclick = null;
      }
    }
  }
  function inlineMarkdown(text) {
    return safe3(text).replace(/`([^`]+)`/g, "<code>$1</code>").replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>").replace(/\*([^*]+)\*/g, "<em>$1</em>");
  }
  var docsIndexPromise = null;
  function loadDocsIndex() {
    if (!docsIndexPromise) {
      docsIndexPromise = fetch("./docs-index.json").then((res) => {
        if (!res.ok) throw new Error(`${res.status}`);
        return res.json();
      });
    }
    return docsIndexPromise;
  }
  var skillsIndexPromise = null;
  function loadSkillsIndex() {
    if (!skillsIndexPromise) {
      skillsIndexPromise = fetch("./skills-index.json").then((res) => {
        if (!res.ok) throw new Error(`${res.status}`);
        return res.json();
      });
    }
    return skillsIndexPromise;
  }
  var playbookSkillsPromise = null;
  function loadPlaybookSkillsMap() {
    if (!playbookSkillsPromise) {
      playbookSkillsPromise = fetch("./playbook-skills.json").then((res) => {
        if (!res.ok) throw new Error(`${res.status}`);
        return res.json();
      });
    }
    return playbookSkillsPromise;
  }
  function bindPlaybookSkillsUi(docPath, skillsSection, skillsList, els2) {
    if (!skillsSection || !skillsList) return;
    skillsSection.hidden = true;
    skillsList.innerHTML = "";
    skillsList.onclick = null;
    if (!docPath) return;
    loadPlaybookSkillsMap().then((pb) => {
      const items = pb.byDocPath?.[docPath] || [];
      if (!items.length) {
        skillsSection.hidden = true;
        skillsList.innerHTML = "";
        skillsList.onclick = null;
        return null;
      }
      return loadSkillsIndex().then((idx) => ({ items, idx }));
    }).then((pack) => {
      if (!pack) return;
      const { items, idx } = pack;
      const docBasename = docPath.replace(/^\.\/assets\/canonicos\//, "").replace(/\.md$/, "");
      skillsSection.hidden = false;
      skillsList.innerHTML = items.map((s) => {
        const entry = idx.skills?.[s.skillPath];
        const title = safe3(entry?.title || s.id);
        const folder = safe3((s.skillPath.match(/\.claude\/skills\/([^/]+)\//) || [])[1] || "");
        return `
        <li class="playbook-skill-card">
          <button type="button" class="playbook-skill-card__btn" data-skill-path="${safe3(s.skillPath)}" data-skill-id="${safe3(s.id)}" data-playbook-label="${safe3(docBasename)}">
            <span class="playbook-skill-card__eyebrow">${folder}</span>
            <strong class="playbook-skill-card__title">${title}</strong>
            <span class="playbook-skill-card__id"><code>${safe3(s.id)}</code></span>
          </button>
        </li>`;
      }).join("");
      skillsList.onclick = (ev) => {
        const btn = ev.target.closest?.("button[data-skill-path]");
        if (!btn) return;
        openSkillModal(btn.dataset.skillPath, btn.dataset.skillId, btn.dataset.playbookLabel, els2);
      };
    }).catch(() => {
      skillsSection.hidden = true;
      skillsList.innerHTML = "";
      skillsList.onclick = null;
    });
  }
  function renderMarkdown(md) {
    const lines = md.split("\n");
    const out = [];
    let inCode = false;
    let code = [];
    let inList = false;
    const closeList = () => {
      if (!inList) return;
      out.push("</ul>");
      inList = false;
    };
    for (const line of lines) {
      if (line.startsWith("```")) {
        if (inCode) {
          out.push(`<pre><code>${safe3(code.join("\n"))}</code></pre>`);
          code = [];
          inCode = false;
        } else {
          closeList();
          inCode = true;
        }
        continue;
      }
      if (inCode) {
        code.push(line);
        continue;
      }
      if (!line.trim()) {
        closeList();
        continue;
      }
      const heading = line.match(/^(#{1,4})\s+(.+)$/);
      if (heading) {
        closeList();
        const level = Math.min(heading[1].length + 1, 5);
        out.push(`<h${level}>${inlineMarkdown(heading[2])}</h${level}>`);
        continue;
      }
      const bullet = line.match(/^\s*[-*]\s+(.+)$/);
      if (bullet) {
        if (!inList) {
          out.push("<ul>");
          inList = true;
        }
        out.push(`<li>${inlineMarkdown(bullet[1])}</li>`);
        continue;
      }
      closeList();
      out.push(`<p>${inlineMarkdown(line)}</p>`);
    }
    closeList();
    if (inCode) out.push(`<pre><code>${safe3(code.join("\n"))}</code></pre>`);
    return out.join("");
  }
  function renderDocPreview(node, els2) {
    if (!els2.sectionDoc || !els2.selectedDocPath || !els2.selectedDocContent) return;
    const docPath = node.docPath || node.doc?.path;
    if (!docPath) {
      clearDocPreview(els2);
      return;
    }
    els2.sectionDoc.hidden = false;
    els2.selectedDocPath.textContent = docPath;
    els2.selectedDocContent.innerHTML = "<p>Carregando documento...</p>";
    if (els2.copyDocMarkdown) {
      els2.copyDocMarkdown.disabled = true;
      els2.copyDocMarkdown.textContent = "Copiar markdown";
    }
    if (els2.playbookSkillsSection) els2.playbookSkillsSection.hidden = true;
    if (els2.playbookSkillsList) {
      els2.playbookSkillsList.innerHTML = "";
      els2.playbookSkillsList.onclick = null;
    }
    bindPlaybookSkillsUi(docPath, els2.playbookSkillsSection, els2.playbookSkillsList, els2);
    loadDocsIndex().then((idx) => {
      const doc = idx.docs?.[docPath];
      if (!doc) throw new Error(`Documento nao indexado: ${docPath}`);
      els2.selectedDocContent.innerHTML = doc.html || renderMarkdown(doc.markdown || "");
      if (!els2.copyDocMarkdown) return;
      els2.copyDocMarkdown.disabled = false;
      els2.copyDocMarkdown.onclick = async () => {
        await navigator.clipboard.writeText(doc.markdown || "");
        els2.copyDocMarkdown.textContent = "Copiado";
        setTimeout(() => {
          els2.copyDocMarkdown.textContent = "Copiar markdown";
        }, 1200);
      };
    }).catch(() => {
      fetch(docPath).then((res) => {
        if (!res.ok) throw new Error(`${res.status}`);
        return res.text();
      }).then((txt) => {
        els2.selectedDocContent.innerHTML = renderMarkdown(txt);
        if (!els2.copyDocMarkdown) return;
        els2.copyDocMarkdown.disabled = false;
        els2.copyDocMarkdown.onclick = async () => {
          await navigator.clipboard.writeText(txt);
          els2.copyDocMarkdown.textContent = "Copiado";
          setTimeout(() => {
            els2.copyDocMarkdown.textContent = "Copiar markdown";
          }, 1200);
        };
      }).catch(() => {
        els2.selectedDocContent.innerHTML = "<p>N\xE3o foi poss\xEDvel carregar o documento. Rode o canvas via servidor local ou publique os arquivos est\xE1ticos.</p>";
      });
    });
  }
  function renderAssetModalDoc(asset, els2) {
    if (!els2.assetModalDocSection || !els2.assetModalDocPath || !els2.assetModalDocContent) return;
    const docPath = asset.docPath || asset.doc?.path;
    if (!docPath) {
      clearAssetModalDoc(els2);
      return;
    }
    els2.assetModalDocSection.hidden = false;
    els2.assetModalDocPath.textContent = docPath;
    els2.assetModalDocContent.innerHTML = "<p>Carregando documento...</p>";
    if (els2.assetModalCopyMarkdown) {
      els2.assetModalCopyMarkdown.disabled = true;
      els2.assetModalCopyMarkdown.textContent = "Copiar markdown";
    }
    if (els2.assetModalSkillsSection) els2.assetModalSkillsSection.hidden = true;
    if (els2.assetModalSkillsList) {
      els2.assetModalSkillsList.innerHTML = "";
      els2.assetModalSkillsList.onclick = null;
    }
    bindPlaybookSkillsUi(docPath, els2.assetModalSkillsSection, els2.assetModalSkillsList, els2);
    loadDocsIndex().then((idx) => {
      const doc = idx.docs?.[docPath];
      if (!doc) throw new Error(`Documento nao indexado: ${docPath}`);
      els2.assetModalDocContent.innerHTML = doc.html || renderMarkdown(doc.markdown || "");
      if (!els2.assetModalCopyMarkdown) return;
      els2.assetModalCopyMarkdown.disabled = false;
      els2.assetModalCopyMarkdown.onclick = async () => {
        await navigator.clipboard.writeText(doc.markdown || "");
        els2.assetModalCopyMarkdown.textContent = "Copiado";
        setTimeout(() => {
          els2.assetModalCopyMarkdown.textContent = "Copiar markdown";
        }, 1200);
      };
    }).catch(() => {
      fetch(docPath).then((res) => {
        if (!res.ok) throw new Error(`${res.status}`);
        return res.text();
      }).then((txt) => {
        els2.assetModalDocContent.innerHTML = renderMarkdown(txt);
        if (!els2.assetModalCopyMarkdown) return;
        els2.assetModalCopyMarkdown.disabled = false;
        els2.assetModalCopyMarkdown.onclick = async () => {
          await navigator.clipboard.writeText(txt);
          els2.assetModalCopyMarkdown.textContent = "Copiado";
          setTimeout(() => {
            els2.assetModalCopyMarkdown.textContent = "Copiar markdown";
          }, 1200);
        };
      }).catch(() => {
        els2.assetModalDocContent.innerHTML = "<p>N\xE3o foi poss\xEDvel carregar o documento. Rode o canvas via servidor local ou publique os arquivos est\xE1ticos.</p>";
      });
    });
  }
  function renderOperatorGuide(node, els2) {
    if (!els2.sectionOperatorGuide || !els2.selectedOperatorGuide) return;
    const guide = node.operatorGuide;
    if (!guide) {
      els2.sectionOperatorGuide.hidden = true;
      els2.selectedOperatorGuide.innerHTML = "";
      return;
    }
    const blocks = [
      ["Fazer agora", guide.doNow],
      ["Abrir", guide.openThese],
      ["Criar/preencher", guide.createThese],
      ["Decidir", guide.decisions],
      ["Avan\xE7ar quando", guide.doneWhen]
    ];
    els2.sectionOperatorGuide.hidden = false;
    els2.selectedOperatorGuide.innerHTML = blocks.map(
      ([title, items]) => `
        <div class="operator-guide__block">
          <strong>${safe3(title)}</strong>
          ${renderGuideList(items || [])}
        </div>
      `
    ).join("");
  }
  function renderPageContent(node, els2) {
    if (!els2.sectionPageContent || !els2.selectedPageContent) return;
    const sections = node.page?.sections || [];
    if (!node.page?.headline && !sections.length) {
      els2.sectionPageContent.hidden = true;
      els2.selectedPageContent.innerHTML = "";
      return;
    }
    const headline = node.page?.headline ? `<p class="stage-content__headline">${safe3(node.page.headline)}</p>` : "";
    const blocks = sections.map(
      (section) => `
        <div class="stage-content__block">
          <strong>${safe3(section.title)}</strong>
          <p>${safe3(section.body)}</p>
        </div>
      `
    ).join("");
    els2.sectionPageContent.hidden = false;
    els2.selectedPageContent.innerHTML = `${headline}${blocks}`;
  }
  function assetStatusLabel(asset) {
    if (asset.required === true) return "Obrigat\xF3rio";
    if (asset.required === false) return "Condicional";
    return asset.statusInJourney || "Asset";
  }
  function renderAssetDetailList(title, items = []) {
    if (!items.length) return "";
    return `
    <div class="asset-detail-block">
      <strong>${safe3(title)}</strong>
      <ul>${items.map((item) => `<li>${safe3(item)}</li>`).join("")}</ul>
    </div>
  `;
  }
  function clearSkillModal(els2) {
    if (els2.skillModalPath) els2.skillModalPath.textContent = "-";
    if (els2.skillModalContent) els2.skillModalContent.innerHTML = "";
    if (els2.skillModalCopyMarkdown) {
      els2.skillModalCopyMarkdown.disabled = true;
      els2.skillModalCopyMarkdown.textContent = "Copiar markdown";
      els2.skillModalCopyMarkdown.onclick = null;
    }
  }
  function closeSkillModal(els2) {
    if (!els2.skillModal) return;
    els2.skillModal.hidden = true;
    if (els2.skillModalBackdrop) {
      els2.skillModalBackdrop.hidden = true;
      els2.skillModalBackdrop.setAttribute("aria-hidden", "true");
    }
    document.body.classList.remove("skill-modal-open");
    clearSkillModal(els2);
  }
  function openSkillModal(skillPath, skillId, playbookLabel, els2) {
    if (!els2.skillModal || !skillPath) return;
    if (els2.skillModalMeta) els2.skillModalMeta.textContent = "Claude Code skill";
    if (els2.skillModalTitle) els2.skillModalTitle.textContent = skillId || "Skill";
    if (els2.skillModalPlaybook) {
      els2.skillModalPlaybook.textContent = playbookLabel ? `Playbook: ${playbookLabel}.md` : "Playbook can\xF4nico vinculado";
    }
    if (els2.skillModalPath) els2.skillModalPath.textContent = skillPath;
    if (els2.skillModalContent) els2.skillModalContent.innerHTML = "<p>Carregando skill...</p>";
    if (els2.skillModalCopyMarkdown) {
      els2.skillModalCopyMarkdown.disabled = true;
      els2.skillModalCopyMarkdown.textContent = "Copiar markdown";
    }
    els2.skillModal.hidden = false;
    if (els2.skillModalBackdrop) {
      els2.skillModalBackdrop.hidden = false;
      els2.skillModalBackdrop.setAttribute("aria-hidden", "false");
    }
    document.body.classList.add("skill-modal-open");
    loadSkillsIndex().then((idx) => {
      const row = idx.skills?.[skillPath];
      if (!row) throw new Error("skill not indexed");
      if (els2.skillModalTitle) els2.skillModalTitle.textContent = row.title || skillId || "Skill";
      if (els2.skillModalContent) {
        els2.skillModalContent.innerHTML = row.html || renderMarkdown(row.markdown || "");
      }
      if (!els2.skillModalCopyMarkdown) return;
      els2.skillModalCopyMarkdown.disabled = false;
      els2.skillModalCopyMarkdown.onclick = async () => {
        await navigator.clipboard.writeText(row.markdown || "");
        els2.skillModalCopyMarkdown.textContent = "Copiado";
        setTimeout(() => {
          els2.skillModalCopyMarkdown.textContent = "Copiar markdown";
        }, 1200);
      };
    }).catch(() => {
      fetch(skillPath).then((res) => {
        if (!res.ok) throw new Error(`${res.status}`);
        return res.text();
      }).then((txt) => {
        if (els2.skillModalContent) els2.skillModalContent.innerHTML = renderMarkdown(txt);
        if (!els2.skillModalCopyMarkdown) return;
        els2.skillModalCopyMarkdown.disabled = false;
        els2.skillModalCopyMarkdown.onclick = async () => {
          await navigator.clipboard.writeText(txt);
          els2.skillModalCopyMarkdown.textContent = "Copiado";
          setTimeout(() => {
            els2.skillModalCopyMarkdown.textContent = "Copiar markdown";
          }, 1200);
        };
      }).catch(() => {
        if (els2.skillModalContent) {
          els2.skillModalContent.innerHTML = "<p>N\xE3o foi poss\xEDvel carregar a skill. Rode o canvas via servidor local.</p>";
        }
      });
    });
  }
  function closeAssetModal(els2) {
    if (!els2.assetModal) return;
    els2.assetModal.hidden = true;
    if (els2.assetModalBackdrop) {
      els2.assetModalBackdrop.hidden = true;
      els2.assetModalBackdrop.setAttribute("aria-hidden", "true");
    }
    document.body.classList.remove("asset-modal-open");
    clearAssetModalDoc(els2);
  }
  function openAssetModal(asset, els2) {
    if (!els2.assetModal) return;
    closeSkillModal(els2);
    if (els2.assetModalMeta) {
      const status = assetStatusLabel(asset);
      const kind = asset.kind || "asset";
      els2.assetModalMeta.textContent = `${asset.order || ""} \xB7 ${kind} \xB7 ${status}`.trim();
    }
    if (els2.assetModalTitle) els2.assetModalTitle.textContent = asset.title || asset.label || "Asset";
    if (els2.assetModalSummary) {
      els2.assetModalSummary.textContent = asset.definitionOfDone || asset.note || asset.aiSummary || "Asset operacional da etapa.";
    }
    if (els2.assetModalDetails) {
      const metaBlocks = [
        asset.owner ? ["Dono", asset.owner] : null,
        asset.whenCreated ? ["Quando cria", asset.whenCreated] : null,
        asset.statusInJourney ? ["Status na jornada", asset.statusInJourney] : null,
        asset.n2Evidence ? ["Evid\xEAncia N2", asset.n2Evidence] : null,
        asset.n3Use ? ["Uso N3", asset.n3Use] : null
      ].filter(Boolean).map(
        ([title, value]) => `
          <div class="asset-detail-block">
            <strong>${safe3(title)}</strong>
            <p>${safe3(value)}</p>
          </div>
        `
      ).join("");
      els2.assetModalDetails.innerHTML = [
        metaBlocks,
        renderAssetDetailList("Inputs", asset.inputs || []),
        renderAssetDetailList("Conte\xFAdo m\xEDnimo", asset.contents || []),
        renderAssetDetailList("Outputs", asset.outputs || [])
      ].join("");
    }
    els2.assetModal.hidden = false;
    if (els2.assetModalBackdrop) {
      els2.assetModalBackdrop.hidden = false;
      els2.assetModalBackdrop.setAttribute("aria-hidden", "false");
    }
    document.body.classList.add("asset-modal-open");
    renderAssetModalDoc(asset, els2);
  }
  function renderStageAssets(node, els2) {
    if (!els2.sectionAssets || !els2.selectedAssets) return;
    const assets = (node.assets || []).map((a, idx) => normalizeAssetEntry(a, node.id, idx)).sort((a, b) => (a.order || 0) - (b.order || 0));
    els2.sectionAssets.hidden = !assets.length;
    if (!assets.length) {
      els2.selectedAssets.innerHTML = "";
      return;
    }
    els2.selectedAssets.innerHTML = assets.map((asset) => {
      const docBadge = asset.docPath ? `<span class="asset-card-pill asset-card-pill--doc">doc</span>` : "";
      const required = `<span class="asset-card-pill">${safe3(assetStatusLabel(asset))}</span>`;
      const owner = asset.owner ? `<span class="asset-card-owner">${safe3(asset.owner)}</span>` : "";
      const subtitle = asset.definitionOfDone || asset.note || asset.aiSummary || "";
      const done = subtitle ? `<p>${safe3(subtitle)}</p>` : "";
      return `
        <li class="inspector-asset-card">
          <button type="button" data-asset-id="${safe3(asset.id)}" data-doc-path="${safe3(asset.docPath)}">
            <span class="asset-card-index">${safe3(String(asset.order || ""))}</span>
            <span class="asset-card-main">
              <strong>${safe3(asset.label || asset.title)}</strong>
              <span>${safe3(asset.kind || "asset")}</span>
              ${done}
              <span class="asset-card-meta">${required}${docBadge}${owner}</span>
            </span>
          </button>
        </li>
      `;
    }).join("");
    els2.selectedAssets.onclick = (event) => {
      const button = event.target.closest?.("button[data-asset-id]");
      if (!button || button.disabled) return;
      const asset = assets.find((item) => item.id === button.dataset.assetId);
      if (!asset) return;
      els2.selectedAssets.querySelectorAll(".is-active").forEach((active) => active.classList.remove("is-active"));
      button.classList.add("is-active");
      openAssetModal(asset, els2);
    };
  }
  function setInspectorExpanded(on, els2) {
    state.inspectorExpanded = on;
    document.body.classList.toggle("inspector-expanded", on);
    if (els2.inspectorBackdrop) {
      els2.inspectorBackdrop.hidden = !on;
      els2.inspectorBackdrop.setAttribute("aria-hidden", on ? "false" : "true");
    }
    if (els2.inspectorToggleExpand) {
      els2.inspectorToggleExpand.setAttribute("aria-expanded", String(on));
      els2.inspectorToggleExpand.textContent = on ? "Fechar" : "Expandir";
      els2.inspectorToggleExpand.title = on ? "Fechar detalhes (Esc)" : "Abrir detalhes em tela cheia";
    }
  }
  function bindInspectorModal(els2) {
    if (!els2.inspectorToggleExpand) return;
    els2.inspectorToggleExpand.addEventListener(
      "click",
      () => setInspectorExpanded(!state.inspectorExpanded, els2)
    );
    if (els2.inspectorBackdrop) {
      els2.inspectorBackdrop.addEventListener("click", () => setInspectorExpanded(false, els2));
    }
    if (els2.assetModalClose) {
      els2.assetModalClose.addEventListener("click", () => closeAssetModal(els2));
    }
    if (els2.assetModalBackdrop) {
      els2.assetModalBackdrop.addEventListener("click", () => closeAssetModal(els2));
    }
    if (els2.skillModalClose) {
      els2.skillModalClose.addEventListener("click", () => closeSkillModal(els2));
    }
    if (els2.skillModalBackdrop) {
      els2.skillModalBackdrop.addEventListener("click", () => closeSkillModal(els2));
    }
    document.addEventListener("keydown", (event) => {
      if (event.key !== "Escape") return;
      if (els2.skillModal && !els2.skillModal.hidden) {
        closeSkillModal(els2);
        event.preventDefault();
        return;
      }
      if (els2.assetModal && !els2.assetModal.hidden) {
        closeAssetModal(els2);
        event.preventDefault();
        return;
      }
      if (!state.inspectorExpanded) return;
      setInspectorExpanded(false, els2);
      event.preventDefault();
    });
  }
  function renderInspector(node, els2) {
    if (!node) return;
    closeAssetModal(els2);
    closeSkillModal(els2);
    const isMicro = node.role === "micro" || node.type === "micro";
    renderDocPreview(node, els2);
    renderOperatorGuide(node, els2);
    renderPageContent(node, els2);
    els2.selectedKind.textContent = isMicro ? "Microt\xF3pico" : node.type || "step";
    els2.selectedId.textContent = node.id;
    els2.selectedTitle.textContent = node.title;
    els2.selectedDescription.textContent = node.summary || node.title;
    if (isMicro) {
      els2.selectedInputs.innerHTML = padList(node.inputs || []);
      els2.selectedOutputs.innerHTML = padList(node.outputs || []);
      els2.selectedEvidence.textContent = node.evidence || "-";
      const parent = resolveNode(node.parentId);
      if (els2.sectionParent && els2.parentMeta) {
        els2.sectionParent.hidden = !parent;
        els2.parentMeta.textContent = parent ? `${parent.number} \xB7 ${parent.title}` : "-";
      }
      els2.sectionAssets.hidden = true;
      els2.selectedAssets.innerHTML = "";
      if (els2.sectionPageContent) els2.sectionPageContent.hidden = true;
      if (els2.selectedPageContent) els2.selectedPageContent.innerHTML = "";
      return;
    }
    if (els2.sectionParent) els2.sectionParent.hidden = true;
    els2.selectedInputs.innerHTML = padList(node.inputs || []);
    els2.selectedOutputs.innerHTML = padList(node.outputs || []);
    els2.selectedEvidence.textContent = node.evidence || "-";
    renderStageAssets(node, els2);
  }

  // js/canvas/viewport.js
  function updateTransform(els2) {
    els2.canvas.style.transform = `translate(${state.pan.x}px, ${state.pan.y}px) scale(${state.zoom})`;
    els2.zoomLabel.textContent = `${Math.round(state.zoom * 100)}%`;
  }
  function setZoom(nextZoom, els2, anchor = null) {
    const prev = state.zoom;
    const zoom = clamp(nextZoom, 0.22, 2);
    if (anchor) {
      const wx = (anchor.x - state.pan.x) / prev;
      const wy = (anchor.y - state.pan.y) / prev;
      state.pan.x = anchor.x - wx * zoom;
      state.pan.y = anchor.y - wy * zoom;
    }
    state.zoom = zoom;
    updateTransform(els2);
  }
  function fitView(els2) {
    const rect = els2.viewport.getBoundingClientRect();
    const zoom = Math.min(
      rect.width / state.workflow.canvas.width,
      rect.height / state.workflow.canvas.height
    );
    state.zoom = clamp(zoom * 0.92, 0.22, 1);
    state.pan = {
      x: (rect.width - state.workflow.canvas.width * state.zoom) / 2,
      y: (rect.height - state.workflow.canvas.height * state.zoom) / 2
    };
    updateTransform(els2);
  }
  function bindViewport(els2, onSelect) {
    els2.canvas.addEventListener("click", (e) => {
      const hit = e.target.closest("[data-node-id]");
      if (!hit) return;
      onSelect(hit.dataset.nodeId, {
        userClick: true,
        clickRole: hit.dataset.role || ""
      });
    });
    els2.viewport.addEventListener("pointerdown", (e) => {
      if (e.target.closest("[data-node-id]")) return;
      state.isPanning = true;
      state.panStart = { x: e.clientX, y: e.clientY };
      state.originStart = { ...state.pan };
      els2.viewport.classList.add("is-panning");
      els2.viewport.setPointerCapture(e.pointerId);
    });
    els2.viewport.addEventListener("pointermove", (e) => {
      if (!state.isPanning) return;
      state.pan = {
        x: state.originStart.x + e.clientX - state.panStart.x,
        y: state.originStart.y + e.clientY - state.panStart.y
      };
      updateTransform(els2);
    });
    els2.viewport.addEventListener("pointerup", (e) => {
      state.isPanning = false;
      els2.viewport.classList.remove("is-panning");
      els2.viewport.releasePointerCapture(e.pointerId);
    });
    els2.viewport.addEventListener(
      "wheel",
      (e) => {
        e.preventDefault();
        const rect = els2.viewport.getBoundingClientRect();
        setZoom(state.zoom + (e.deltaY > 0 ? -1 : 1) * 0.08, els2, {
          x: e.clientX - rect.left,
          y: e.clientY - rect.top
        });
      },
      { passive: false }
    );
    els2.zoomIn.addEventListener("click", () => setZoom(state.zoom + 0.1, els2));
    els2.zoomOut.addEventListener("click", () => setZoom(state.zoom - 0.1, els2));
    els2.fitView.addEventListener("click", () => fitView(els2));
    els2.resetView.addEventListener("click", () => {
      const iv = state.workflow.canvas.initialView;
      state.pan = { x: iv.x, y: iv.y };
      state.zoom = iv.zoom;
      updateTransform(els2);
    });
    if (els2.versionSelect) {
      els2.versionSelect.addEventListener("change", () => {
        localStorage.setItem("workflowManifestVersion", els2.versionSelect.value);
        const params = new URLSearchParams(location.search);
        params.set("version", els2.versionSelect.value);
        location.href = `${location.pathname}?${params.toString()}`;
      });
    }
  }

  // js/main.js
  var els = {
    title: document.querySelector("#boardTitle"),
    viewport: document.querySelector("#viewport"),
    canvas: document.querySelector("#canvas"),
    edges: document.querySelector("#edges"),
    groups: document.querySelector("#groups"),
    nodes: document.querySelector("#nodes"),
    stepNodes: document.querySelector("#stepNodes"),
    assetCards: document.querySelector("#assetCards"),
    peekBackdrop: document.querySelector("#peekBackdrop"),
    zoomLabel: document.querySelector("#zoomLabel"),
    zoomIn: document.querySelector("#zoomIn"),
    zoomOut: document.querySelector("#zoomOut"),
    fitView: document.querySelector("#fitView"),
    resetView: document.querySelector("#resetView"),
    selectedKind: document.querySelector("#selectedKind"),
    selectedId: document.querySelector("#selectedId"),
    selectedTitle: document.querySelector("#selectedTitle"),
    selectedDescription: document.querySelector("#selectedDescription"),
    selectedInputs: document.querySelector("#selectedInputs"),
    selectedOutputs: document.querySelector("#selectedOutputs"),
    selectedEvidence: document.querySelector("#selectedEvidence"),
    sectionDoc: document.querySelector("#sectionDoc"),
    selectedDocPath: document.querySelector("#selectedDocPath"),
    selectedDocContent: document.querySelector("#selectedDocContent"),
    copyDocMarkdown: document.querySelector("#copyDocMarkdown"),
    playbookSkillsSection: document.querySelector("#playbookSkillsSection"),
    playbookSkillsList: document.querySelector("#playbookSkillsList"),
    sectionAssets: document.querySelector("#sectionAssets"),
    selectedAssets: document.querySelector("#selectedAssets"),
    sectionPageContent: document.querySelector("#sectionPageContent"),
    selectedPageContent: document.querySelector("#selectedPageContent"),
    assetModal: document.querySelector("#assetModal"),
    assetModalBackdrop: document.querySelector("#assetModalBackdrop"),
    assetModalClose: document.querySelector("#assetModalClose"),
    assetModalMeta: document.querySelector("#assetModalMeta"),
    assetModalTitle: document.querySelector("#assetModalTitle"),
    assetModalSummary: document.querySelector("#assetModalSummary"),
    assetModalDetails: document.querySelector("#assetModalDetails"),
    assetModalDocSection: document.querySelector("#assetModalDocSection"),
    assetModalSkillsSection: document.querySelector("#assetModalSkillsSection"),
    assetModalSkillsList: document.querySelector("#assetModalSkillsList"),
    assetModalDocPath: document.querySelector("#assetModalDocPath"),
    assetModalDocContent: document.querySelector("#assetModalDocContent"),
    assetModalCopyMarkdown: document.querySelector("#assetModalCopyMarkdown"),
    skillModal: document.querySelector("#skillModal"),
    skillModalBackdrop: document.querySelector("#skillModalBackdrop"),
    skillModalClose: document.querySelector("#skillModalClose"),
    skillModalMeta: document.querySelector("#skillModalMeta"),
    skillModalTitle: document.querySelector("#skillModalTitle"),
    skillModalPlaybook: document.querySelector("#skillModalPlaybook"),
    skillModalPath: document.querySelector("#skillModalPath"),
    skillModalContent: document.querySelector("#skillModalContent"),
    skillModalCopyMarkdown: document.querySelector("#skillModalCopyMarkdown"),
    sectionOperatorGuide: document.querySelector("#sectionOperatorGuide"),
    selectedOperatorGuide: document.querySelector("#selectedOperatorGuide"),
    sectionParent: document.querySelector("#sectionParent"),
    parentMeta: document.querySelector("#parentMeta"),
    inspectorToggleExpand: document.querySelector("#inspectorToggleExpand"),
    inspectorBackdrop: document.querySelector("#inspectorBackdrop"),
    versionSelect: document.querySelector("#workflowVersion")
  };
  function refreshMicroStripUi() {
    renderMacros(els);
    renderMicros(els);
    renderEdges(els);
    renderPeekBackdrop(els);
  }
  function bindPeekBackdropInteractions() {
    const bd = els.peekBackdrop;
    if (!bd || bd.dataset.boundPeek === "1") return;
    bd.dataset.boundPeek = "1";
    bd.addEventListener("pointerdown", (e) => {
      const t = e.target;
      if (t instanceof SVGElement && t.classList.contains("peek-dim")) {
        e.stopPropagation();
      }
    });
    bd.addEventListener("click", (e) => {
      const t = e.target;
      if (!(t instanceof SVGElement) || !t.classList.contains("peek-dim")) return;
      state.microsPeekMacroId = null;
      refreshMicroStripUi();
    });
  }
  function selectNode(id, meta = {}) {
    const node = resolveNode(id);
    state.selectedId = id;
    const split = Boolean(state.workflow.micros?.length);
    if (split && meta.userClick && node) {
      const role = meta.clickRole || "";
      const isMicro = role === "micro" || node.role === "micro" || node.type === "micro";
      const isMacro = role === "macro" || node.role === "macro";
      if (isMicro) {
        state.microsPeekMacroId = node.parentId || null;
      } else if (isMacro) {
        state.microsPeekMacroId = null;
      }
    }
    refreshMicroStripUi();
    renderInspector(node, els);
  }
  function bindMicroStripEscUi() {
    document.addEventListener("keydown", (e) => {
      if (e.key !== "Escape") return;
      if (!state.microsPeekMacroId) return;
      state.microsPeekMacroId = null;
      refreshMicroStripUi();
      e.preventDefault();
    });
  }
  function renderWorkflow() {
    els.title.textContent = state.workflow.title;
    els.canvas.style.width = `${state.workflow.canvas.width}px`;
    els.canvas.style.height = `${state.workflow.canvas.height}px`;
    els.edges.style.width = `${state.workflow.canvas.width}px`;
    els.edges.style.height = `${state.workflow.canvas.height}px`;
    renderGroups(els);
    const first = state.workflow.macros[0];
    state.selectedId = first?.id ?? null;
    state.microsPeekMacroId = null;
    refreshMicroStripUi();
    renderInspector(resolveNode(state.selectedId), els);
    state.pan = { ...state.workflow.canvas.initialView };
    state.zoom = state.workflow.canvas.initialView.zoom;
    updateTransform(els);
  }
  async function loadManifestAndWorkflow() {
    const res = await fetch("./workflow.manifest.json");
    if (!res.ok) throw new Error(`workflow.manifest.json: ${res.status}`);
    state.manifest = await res.json();
    const qp = new URLSearchParams(location.search).get("version");
    const stored = localStorage.getItem("workflowManifestVersion");
    const activeId = qp || stored || state.manifest.defaultVersionId;
    const meta = state.manifest.versions.find((v) => v.id === activeId) || state.manifest.versions.find((v) => v.id === state.manifest.defaultVersionId);
    if (!meta) throw new Error("Nenhuma vers\xE3o encontrada no manifest");
    const rawRes = await fetch(meta.workflowFile);
    if (!rawRes.ok) throw new Error(`${meta.workflowFile}: ${rawRes.status}`);
    const rawJson = await rawRes.json();
    state.workflow = buildWorkflowView(rawJson, meta);
    if (els.versionSelect) {
      els.versionSelect.innerHTML = state.manifest.versions.map((v) => `<option value="${v.id}" ${v.id === meta.id ? "selected" : ""}>${v.label}</option>`).join("");
      els.versionSelect.disabled = state.manifest.versions.length < 2;
      localStorage.setItem("workflowManifestVersion", meta.id);
    }
    renderWorkflow();
  }
  async function boot() {
    bindInspectorModal(els);
    bindViewport(els, selectNode);
    bindMicroStripEscUi();
    bindPeekBackdropInteractions();
    try {
      await loadManifestAndWorkflow();
    } catch (error) {
      els.title.textContent = "Erro ao carregar workflow";
      els.selectedTitle.textContent = "Falha no carregamento";
      els.selectedDescription.textContent = error.message;
    }
  }
  boot();
})();
