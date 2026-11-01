# Studies

Add each subject in its own folder, for example `studies/aws/plan.md`. Use the template at `../templates/study/plan.md` and give each topic a stable, unique ID within that study.

Topic format (first checkbox = studied; second = understanding demonstrated):

```markdown
- [ ] [ ] **AWS-001** — Concept or skill
```

After creating or editing a plan, run `python scripts/update_progress.py`. The root README dashboard counts only study folders that contain a `plan.md`.
