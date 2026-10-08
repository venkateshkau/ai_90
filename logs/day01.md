# Day 01 — Log

## Session summary
- Oriented on Day 1 (Setup): goal, DoD, and the 6-step session plan.
- Walked the session plan step by step, verifying repo state after each "done".
- Ran the Build/Review/Close flow from CLAUDE.md.

## Commands run
- `ls -la`, `find src -maxdepth 3`, `cat pyproject.toml`, `git log --oneline -10`, `git remote -v` — initial repo scan
- `cat .env.example`, `git check-ignore -v .env`, `git status --short` — secrets hygiene checks
- `uv add anthropic python-dotenv pydantic`
- `uv add --dev pytest`
- `uv run pytest -v` → 2 passed
- `brew install poppler` (background) — for future on-demand PDF page reads, not run proactively against the guide

## Decisions / corrections made this session
- Caught a real-looking API key pasted into `.env.example` (should hold placeholders only, since `.env.example` is meant to be committed). Moved the real value to `.env` (git-ignored), cleared the example.
- Had duplicate package dirs `src/ai90` and `src/ai_90`; kept `src/ai_90`, adjusted the smoke test's import accordingly.
- Smoke test originally used `os.environ["ANTHROPIC_API_KEY"]` (raises `KeyError` if unset); changed to `os.getenv(..., "")` to match the guide's intended failure mode.
- README "Levels" section initially listed today's session steps as L1–L5; corrected to reflect the curriculum's actual L1–L7 tracks spanning all 90 days.
- Added the full guide at `plan/VK_90_Day_AI_Daily_Guide.pdf`; updated `CLAUDE.md` so the coach references it only on request, not proactively, and still only actively coaches the day VK opens with "start".
- Added this `logs/` folder convention (coach-maintained session log, separate from VK's own `notes/dayNN.md`).

## Open items at time of writing
- `notes/day01.md` not yet written (VK's own 3-line log).
- Today's work not yet committed/pushed.
- Stray `README.pdf` at repo root — intent unconfirmed.
