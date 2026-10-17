# Sequence 4 — Social media on autopilot (r7e, promoavatar, xviral)

**Objective:** build a channel in your niche that posts regularly, with numbers, sources, and your face, while you approve what matters.
**Based on:** reel7etapas (https://inematds.github.io/reel7etapas/guia/), promoavatar (https://inematds.github.io/promoavatar/guia/), promoavatar3 (https://inematds.github.io/promoavatar3/guia/), finviral (https://inematds.github.io/finviral/guia/), saudeviral (https://inematds.github.io/saudeviral/guia/) and advviral (https://inematds.github.io/advviral/guia/).
**Prerequisite:** Sequences 1, 2 and 3. Without a queue and a gate, automating social media just lets you post the wrong thing faster.

---

## E1. A reel in 7 steps, on paper (20 min)

Write a 30 to 45-second reel in your niche using the r7e model:

| # | Step | Your line |
|---|---|---|
| 1 | Hook (the result in 2 s) | |
| 2 | Desire | |
| 3 | Fear | |
| 4 | Ease | |
| 5 | Discovery (the solution's name) | |
| 6 | Benefit | |
| 7 | Comment (“comment WORD”) | |

**Done when:** you can read it aloud in under 45 s and the first line already states the benefit.

## E2. The 5 channels in your niche (20 min)

Choose 5 reference channels in your niche (real estate, agriculture, beauty, education…). For each one: name, link, video frequency, topic that performs best. Also write the **rules for your niche**: what counts as fact, the required disclaimer (e.g., “not investment advice,” “not a substitute for professional care”), and what you never publish.

**Done when:** you have `canais.md` and `regras.md` for your niche.

## E3. The source-backed knowledge base (30 min)

Get the transcript of a video from one of the 5 channels (inemavox or another local transcription tool will do). Create `base.md`:

| Number or fact | Who said it | Video | Verbatim excerpt |
|---|---|---|---|

**Done when:** every row has a verbatim excerpt and you found each excerpt in the transcript. That’s exactly what finviral’s `checar.py` does automatically.

## E4. A 60-second script with sources on screen (30 min)

Using `base.md`, ask the agent for a 60-second script: an opening with the strongest number, three facts with attribution, the niche disclaimer, and a closing invitation. Spell out numbers in the spoken lines.

**Done when:** every number in the script appears in `base.md`. If any number is missing, send the script back.

## E5. The schedule (20 min)

Decide how often to post (e.g., Monday to Friday every 2 hours, one longer video on Saturday) and write the schedule (cron or systemd timer), as finviral does. Rule: **a slow day doesn’t become a video**, and failures notify you on Telegram.

**Done when:** the schedule is written and you know what happens on a day with no topic.

## E6. The approval gate before publishing (one week)

Run for a week with manual approval before each post. Note what you rejected and why. Each rejection becomes a rule in `regras.md`.

**Done when:** you’ve gone 3 days in a row without needing to reject anything. Only then consider removing the gate from any step.

---

### Extra challenge
Create a promoavatar for your niche: 3 videos for the same audience (reach, authority, and promotional) and compare which one gets more comments.