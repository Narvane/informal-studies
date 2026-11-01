---
name: assess-understanding
description: Assess understanding of studied topics using explanations and applications demonstrated in the conversation, then propose plan updates and record the result after approval.
---

# Assess understanding

Use this skill when the user asks to assess, test, or review their understanding of a study. The goal is to find evidence of sufficient understanding; questions asked by the user alone do not prove mastery.

## Workflow

1. Identify the active study and read `studies/<slug>/plan.md`. Focus on topics already marked as studied. If the study is ambiguous, ask which one to use.
2. Review this conversation for explanations in the user's own words, connections between concepts, predictions, and applications. Do not treat an answer given after the assistant has fully explained the topic as independent evidence.
3. For each topic, classify the evidence as **understanding demonstrated**, **partial / revisit**, or **insufficient evidence**. If the conversation does not provide enough evidence, ask short questions one at a time and wait for the answers before deciding. Prefer explanations and applications over simple recall questions.
4. Show the proposed result by topic ID, with concise evidence. Ask for approval before recording any assessment. Never mark a topic as studied in this skill; if coverage has not been recorded yet, ask the user to run `finish-study-session` first.
5. After approval, mark the second box (`[x] [x]`) only for topics that are already marked as studied and whose understanding was demonstrated. Leave the second box unchecked for other topics and record what should be revisited. Do not present an inconclusive assessment as mastery.
6. Record the result in `studies/<slug>/sessions/YYYY-MM-DD-assessment-<slug>.md`: assessed topics, concise evidence, strengths, gaps, and review recommendations. Do not copy the full conversation. Use the available local date; if it is unavailable, ask or use a date supplied by the user. If the filename already exists, append `-2`, `-3`, and so on to preserve the earlier note.
7. Run `python scripts/update_progress.py` from the repository root to refresh the dashboard. If `python` cannot start in Codex desktop, call `mcp__codex_app__load_workspace_dependencies` and use the bundled Python path it returns. If no runtime is available, preserve the other files and report the error. Review `git status` and summarize the changes.
8. Ask: **“Would you like me to commit and push these changes?”** Only after an explicit yes, commit and attempt to push only changes related to this assessment. Inspect the diff and configured remote first. If no remote is configured, make the authorized local commit and explain that pushing still requires a remote. If the push fails, report the specific reason. If the user says no, leave everything local.
