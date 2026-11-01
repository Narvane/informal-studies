# informal-studies

This repository tracks personal study plans and progress in Markdown and Git.

- Keep each study in `studies/<slug>/`, with its topic list in `plan.md`.
- Follow the topic format documented in `studies/README.md` and `templates/study/plan.md`.
- Use `$finish-study-session` to propose which topics were covered in the conversation. Ask for approval before changing progress checkboxes.
- Use `$assess-understanding` to evaluate understanding. Do not infer mastery from questions alone; look for demonstrated explanations and applications.
- After a study plan changes, run `python scripts/update_progress.py` to keep the README dashboard in sync.
- After a skill changes files, ask whether the user wants a commit and push. Commit or push only after an explicit yes to that question, and limit the commit to files related to this session in this repository.
- Do not invent study topics or mark progress without evidence from the conversation and the user's approval.
