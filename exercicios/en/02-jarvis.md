# Sequence 2 — Create Your Jarvis (INTELECTO)

**Objective:** Have a personal assistant of your own that talks through Telegram, remembers conversations, and has the personality you define.
**Base:** INTELECTO (https://inematds.github.io/intelecto/), course (https://inematds.github.io/intelecto-curso/) and area https://eventos.inema.pro/jarvis/
**Prerequisite:** Sequence 1 completed (terminal, folders, `.env`).

---

## E1. Design Your Jarvis Before Installing It (15 min)

In a `meu-jarvis.md` file, answer:

- The assistant’s name and how it speaks (formal, direct, humorous).
- Three things it **should** do for you every week.
- Three things it should **never** do.
- What it needs to remember about you (profession, routine, preferences).

**Done when:** The file fits on one screen and another person could understand who your assistant is.

## E2. The Telegram Bot (10 min)

In Telegram, open `@BotFather`, send `/newbot`, and choose a name and @username. Save the token **only** in `.env` (see the rule in Sequence 1).

**Done when:** You have the token and it does not appear in any file other than `.env`.

## E3. Install (30 min)

```bash
git clone https://github.com/inematds/intelecto.git
cd intelecto
./start.sh
```

The setup assistant asks for the Telegram token, model, and personality. Use your `meu-jarvis.md` to answer.

**Done when:** You send “hi” on Telegram and it replies with the name and style you defined.

## E4. Memory Test (2 days)

1. Day 1: Tell it three facts about yourself (e.g., “I close the sales report every Monday”).
2. Day 2, in a new conversation: Ask, “What do I do every Monday?”

**Done when:** It remembers without you repeating yourself. If it doesn’t, see the course to learn how memory is stored and adjust it.

## E5. Cloud or Local (20 min)

Ask the same question twice: once with a cloud model (OpenRouter) and once with a local model (Ollama), if your computer can handle it. Make a table with response time, quality, and cost.

**Done when:** You can say which model to use for what, based on your numbers.

## E6. A Real Routine (20 min)

Choose one of the three tasks from E1 and turn it into a recurring request (e.g., “Every morning, when I send ‘day,’ list my top three priorities based on what I told you yesterday”). Use it for a week.

**Done when:** You’ve used it 5 days in a row and noted what to improve.

---

### Extra Challenge
Write the list of tasks you’d like to send and then go to sleep in `meu-jarvis.md`. That list is the input for Sequence 3.