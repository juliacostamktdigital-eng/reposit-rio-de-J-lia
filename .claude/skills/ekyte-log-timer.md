---
name: ekyte-log-timer
description: Registra apontamento de tempo (timer) em uma task do Ekyte. Uso: "timer task X das HH:MM às HH:MM [do dia DD/MM]". Chame quando o usuário quiser logar horas, apontar tempo, registrar timer ou atualizar timer de uma task.
argument-hint: "[nome ou ID da task] das [HH:MM] às [HH:MM] [do dia DD/MM]"
---

# Skill: Registrar Timer no Ekyte

Você vai registrar um apontamento de tempo em uma task do Ekyte via API REST.

---

## CREDENCIAIS (não exibir ao usuário)

- **Company ID:** 3597
- **Bearer Token:** eyJhbGciOiJSUzI1NiIsImtpZCI6IjhBOTg4MzdFNjcyNEZBMzNBNUNENjdERUE4MEI1NDlFRUFDQUE5REFSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6ImlwaURmbWNrLWpPbHpXZmVxQXRVbnVyS3FkbyJ9.eyJuYmYiOjE3NzkxMzY1NjgsImV4cCI6MTc5NDY4ODU2OCwiaXNzIjoiaHR0cHM6Ly9hcGkuZWt5dGUuY29tIiwiY2xpZW50X2lkIjoicmVhY3RKU0NsaWVudCIsInN1YiI6IjE0Mjg0ZmEzLTM4NTAtNDRjMi04OWY3LTdkNTcwODQ3ZjUxZSIsImF1dGhfdGltZSI6MTc3OTEzNjU2NywiaWRwIjoibG9jYWwiLCJqdGkiOiJCNDMyOTVDODMzQzdFMDREMUU2MkZGMzUxMTlCMzFDOSIsImlhdCI6MTc3OTEzNjU2OCwic2NvcGUiOlsiZWt5dGVhcGkiXSwiYW1yIjpbInB3ZCJdfQ.ekGhrg_zWu8bL3Hq5DXRcddMgt1Mv-F67XeqghHg6ynuNxaWdReRI_dzveo35NaP_Shh5DjsKXT_MoI8zH10iVq4nOsb7FYw-k64C-qu9ymsKdU4MQ1fvP2Aqpve6D1snqTJqJlIvN58vpZz69ywkF0XiJbEY137bEdiImCRd85BDZHRwSOeVQfpdppZ2UAaMZpvb8ypvJNDE-uXX9XieYujJGj0F1ENyxtOYz_td6vIm6d_ofNQOEPtcGP24rML3POdLoEeK9QjBlSvYVhkY4zaiWlMM6fyHhvTVhXLIvRxL91aqC_JXsOcKzpeHHS__c3jgI6qDz_Riiny7Scapg
- **Token expira:** ~2026-12-01. Se a API retornar 401, avisar o usuário para renovar o token aqui no skill.

---

## PASSO 1 — INTERPRETAR O PEDIDO

Extrair do input do usuário:

| Campo | Exemplos aceitos |
|-------|-----------------|
| **Task** | nome parcial ("Verificar redes") ou ID numérico (9485238) |
| **Início** | "08:30", "8h30", "8:30" |
| **Fim** | "09:04", "9h04", "9:04" |
| **Data** | "hoje", "02/06", "02/06/2026" — padrão: data atual |

Se faltar algum dado obrigatório (task, início, fim), perguntar antes de continuar.

---

## PASSO 2 — BUSCAR DADOS DA TASK

**Se o usuário passou um ID numérico:**
Usar `ekyte_get_task` com `task_id` = ID informado.

**Se o usuário passou um nome:**
Usar `ekyte_list_tasks` com `title` = nome parcial, demais campos como string vazia.
Exibir lista resumida se houver mais de 1 resultado e pedir confirmação antes de continuar.

Da resposta da task, extrair:
- `id` → ctcTaskId
- `workspaceId` → workspaceId
- `workspace.name` → workspaceName
- `ctcTaskTypeId` → ctcTaskTypeId
- `ctcTaskType` → objeto completo
- `phaseId` → phaseId
- `phase` → objeto completo

---

## PASSO 3 — CALCULAR O ESFORÇO

```
effort = (endHour * 60 + endMin) - (startHour * 60 + startMin)
```

Se `effort <= 0`, avisar o usuário que o horário de fim é antes do início.

---

## PASSO 4 — MONTAR E ENVIAR A REQUISIÇÃO

Montar o body JSON mínimo e executar via **PowerShell `Invoke-WebRequest`**:

```powershell
$token = "<BEARER_TOKEN>"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
    "Accept"        = "*/*"
}

$body = "{`"typeTimeTracking`":2,`"startDate`":`"<YYYY-MM-DD>T<HH:mm>:00`",`"startDateTime`":`"<HH:mm>`",`"endDate`":`"<YYYY-MM-DD>T<HH:mm>:00`",`"endDateTime`":`"<HH:mm>`",`"effort`":<MINUTOS>,`"comment`":`"`",`"workspaceId`":<WORKSPACE_ID>,`"type`":1,`"ctcTaskId`":<TASK_ID>,`"ctcTaskTypeId`":<CTCTASKTYPE_ID>,`"phaseId`":<PHASE_ID>,`"manualTime`":`"<HH:mm>`"}"

try {
    $resp = Invoke-WebRequest `
        -Uri "https://api.ekyte.com/api/companies/3597/workspaces/<WORKSPACE_ID>/time-trackings" `
        -Method POST -Headers $headers -Body $body -ErrorAction Stop
    Write-Output "SUCESSO $($resp.StatusCode): $($resp.Content)"
} catch {
    $code = $_.Exception.Response.StatusCode.value__
    $stream = $_.Exception.Response.GetResponseStream()
    $reader = New-Object System.IO.StreamReader($stream)
    Write-Output "HTTP $code | $($reader.ReadToEnd())"
}
```

> Body mínimo (JSON inline) funciona para todos os tipos de task. Nao usar hashtable + ConvertTo-Json para evitar problemas de serialização.

---

## PASSO 5 — CONFIRMAR RESULTADO

**Sucesso (HTTP 200/201):**
Exibir confirmação resumida:

```
Timer registrado com sucesso!
Task: <nome da task>
Período: <HH:mm> às <HH:mm> — <DD/MM/YYYY>
Duração: <X>h<MM>
```

**Erro 401:** Token expirado. Pedir ao usuário que abra o Ekyte, capture uma nova requisição no DevTools e atualize o token neste skill.

**Outro erro:** Exibir a mensagem de erro da API para diagnóstico.

---

## EXEMPLOS DE USO

- `/ekyte-log-timer timer task 9485238 das 08:30 às 09:04 de hoje`
- `/ekyte-log-timer timer da task Verificar redes sociais das 10:00 às 11:30 do dia 02/06`
- `/ekyte-log-timer apontar 1h na task Reunião semanal, 14:00 às 15:00`
