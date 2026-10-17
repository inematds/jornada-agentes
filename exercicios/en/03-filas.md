# Sequence 3 — Agent Queues (inemaccbot)

**Objective:** Send several tasks, step away, and find the work done, with an approval gate where you’re needed.
**Based on:** inemaccbot (https://inematds.github.io/inemaccbot/guia/) and course https://eventos.inema.pro/inemaccbot.html
**Prerequisite:** Sequences 1 and 2.

---

## E1. The Queue on Paper (15 min)

List 10 repetitive tasks from your work. For each one, mark:

| Task | Runs on its own? | Needs a gate (your approval)? | Where is the gate? |
|---|---|---|---|
| Transcribe the meeting | yes | no | — |
| Weekly post | yes | yes | before publishing |

**Done when:** all 10 rows are filled in and at least two have a gate.

## E2. A Homemade Queue in 30 Lines (30 min)

Before the bot, understand the idea with this repo’s `ferramentas/fila-caseira.sh`:

```bash
mkdir -p fila/entrada
echo "Summarize in 5 lines what a task queue is." > fila/entrada/01.md
echo "List 3 risks of letting an agent run on its own." > fila/entrada/02.md
./ferramentas/fila-caseira.sh fila
```

Each file in `entrada/` becomes a task. The response goes to `feito/`. If there’s an error, the task goes to `falhou/`. Running it again only picks up what’s left.

**Done when:** both tasks are in `fila/feito/` with their responses, and you interrupted a run (Ctrl+C) and saw the queue continue where it left off.

## E3. Install inemaccbot (1 h)

Follow the guide until `/ping` responds in Telegram. Then: `/ajuda` lists the commands and `/fila` shows the queues.

**Done when:** `/ping` responds in your Telegram.

## E4. Ten Tasks, Then Go to Sleep (1 night)

Send the bot 5 to 10 tasks from your E1 list (transcribe, summarize, explainer…). Go do something else.

**Done when:** the next day, you check the result of each one and note how many came out right on the first try.

## E5. The Gate (30 min)

Use a workflow with a gate (like `/promoavatar`): the bot writes the copy and **stops**. Read it, correct it if needed, and only then approve it.

**Done when:** you rejected or corrected at least one piece of copy before approving it. This is the moment when you manage instead of doing.

---

### Extra Challenge
Take the task that failed most in E4 and write a new rule for it (in AGENTS.md or in the skill prompt). Run it again and compare.