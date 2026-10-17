# Sequence 1 — From chat to the terminal (OSWork)

**Goal:** leave the chat and put an agent to work inside one of your folders.
**Based on:** the OSWork course (https://inematds.github.io/oswork-quick/) and the area at https://eventos.inema.pro/oswork/
**You will need:** a computer, the terminal (cmd on Windows; Terminal on Mac and Linux), and Claude Code or Codex installed.

Follow the steps in order. Each exercise has a **Done when** criterion: move on only when it’s true.

---

## E1. Your first folder in the terminal (10 min)

1. Open the terminal.
2. Create the `projetos` folder and, inside it, `meu-primeiro-agente`.
3. Go into it and list its contents (it will be empty).
4. Open the same folder in File Explorer (or Finder) and compare.

**Done when:** you can get to the folder using only the terminal, without the mouse, and can say which folder you’re in.

## E2. The employee handbook: AGENTS.md (15 min)

Create an `AGENTS.md` file inside the folder with:

```markdown
# Who I am
<your name, your profession, who you work for>

# Project rules
- Write in English, using short sentences.
- Don’t delete files without asking.
- Before finishing, say what changed and how I can check it.

# What’s here
- index.html: my page
```

**Done when:** the file exists and has at least three rules you wrote yourself.

## E3. The first task (15 min)

Inside the folder, start the agent (`claude` or `codex`) and ask:

> Read AGENTS.md. Create an index.html with a simple page about me, using what’s in the file.

Open the page in your browser. Ask for a change (a color, some text, or a new section) and check again.

**Done when:** the page opens in the browser and you’ve asked the agent for at least **one correction**. Assigning the task, checking it, and making a decision: that’s management.

## E4. The safety net: Git (20 min)

1. In the folder: `git init`, then `git add .` and `git commit -m "primeira versão"`.
2. Ask the agent to make a major change to the page.
3. Don’t like it? Undo it: `git restore index.html` (or `git checkout -- index.html`).

**Done when:** you’ve undone an agent’s change with a command, without panicking.

## E5. Keep secrets out of text files (10 min)

1. Create a `.env` file with a fake line: `MINHA_CHAVE=teste123`.
2. Create a `.gitignore` file with the line `.env`.
3. Run `git status`: `.env` must **not** appear.
4. Add this to AGENTS.md: "Never write keys or passwords in a text file; keep them in .env".

**Done when:** `git status` does not show `.env`.

## E6. The agent reads your files (20 min)

Put three of your own text files in the folder (notes, meeting minutes, a long email). Ask:

> Read the .txt files in this folder and write resumo.md with 5 decisions and 5 pending items, citing which file each came from.

Check two citations against the original files.

**Done when:** you found at least two of the cited phrases in the original. If any phrase isn’t there, add the missing rule to AGENTS.md.

---

### Extra challenge
Repeat E3 with the **other** agent (if you used Claude Code, use Codex). Both agents read the same AGENTS.md. What changed in the result?