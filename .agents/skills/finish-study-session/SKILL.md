---
name: finish-study-session
description: Review a study conversation, propose topics to mark as covered, and record a session summary after the user approves the changes.
---

# Finish a study session

Use this skill when the user wants to finish, close, or record a study session. It records which content was covered; it does not assess mastery or understanding.

## Workflow

1. Identify the active study from the current working folder or explicit conversation context. Its plan must be at `studies/<slug>/plan.md`. If multiple studies are plausible or no plan exists, ask which study to use or help the user create one. Do not invent topics.
2. Read the plan and compare its topics with this conversation. Propose only topics covered substantively, with brief evidence from the conversation. Distinguish partial coverage from topics that were not covered.
3. Show the IDs and titles you propose to mark as studied, along with any proposed new topics or scope changes. Do not edit files yet. Ask for clear approval before applying the proposed changes.
4. If the user approves, update only the approved coverage boxes in the first position (`[x] [ ]` or `[x] [x]`), preserving the existing second box. Do not mark understanding in this skill. Respect any rejection or requested adjustment; do not make changes without approval.
5. After applying changes, write a summary to `studies/<slug>/sessions/YYYY-MM-DD-<session-slug>.md`. Include approved topics, concise evidence, questions or points to revisit, and next steps. Do not copy the full conversation. Use the available local date; if it is unavailable, ask or use a date supplied by the user. If the filename already exists, append `-2`, `-3`, and so on to preserve the earlier note.
6. Run `python scripts/update_progress.py` from the repository root to refresh the README dashboard. If `python` cannot start in Codex desktop, call `mcp__codex_app__load_workspace_dependencies` and use the bundled Python path it returns. If no runtime is available, preserve the other files and report the error.
7. Review `git status` and summarize the changes. Ask: **“Would you like me to commit and push these changes?”**
8. Only if the user explicitly says yes, commit and attempt to push. Inspect the diff and configured remote; include only changes related to this session and do not include someone else's work. Use a clear commit message. If no remote is configured, make the authorized local commit and explain that pushing still requires a remote. If the push fails, report the specific reason. If the user says no, leave the changes local.

If there are no new topics to mark, do not force a progress change. You may still offer to write a brief session note after approval; then refresh the dashboard if a plan changed and offer commit/push for changes made by the skill.
