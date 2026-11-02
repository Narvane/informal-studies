# informal-studies

A simple workspace for studying any subject with Codex and tracking progress in version-controlled files.

## Study progress

The figures below are generated from topics in `studies/*/plan.md`. The study skills refresh this dashboard after each approved change.

<!-- STUDY_PROGRESS:START -->
### [AWS Fundamentals and Application Development](studies/aws/plan.md)
**128 proposed topics** · **6 studied** · **0 assessed**
Study: `▰▱▱▱▱▱▱▱▱▱` 5%  ·  Understanding: `▱▱▱▱▱▱▱▱▱▱` 0%

### [Design Systems](studies/design-systems/plan.md)
**74 proposed topics** · **0 studied** · **0 assessed**
Study: `▱▱▱▱▱▱▱▱▱▱` 0%  ·  Understanding: `▱▱▱▱▱▱▱▱▱▱` 0%
<!-- STUDY_PROGRESS:END -->

## How to use

1. Create a folder under `studies/` and add a `plan.md` for the subject. Use the template at `templates/study/plan.md`.
2. Open that folder in Codex and study through a normal conversation.
3. When you finish, invoke `$finish-study-session` to review which topics were covered.
4. Invoke `$assess-understanding` to check what you can explain and apply.
5. Review and approve the proposed changes. The skills update the plan, save a session summary, and regenerate this dashboard.
6. After a skill changes files, it will ask whether you want to commit and push. It will do so only after you confirm.

To regenerate the dashboard manually, run `python scripts/update_progress.py` from the repository root.

## Topic states

Each topic has two checkboxes: the first means the topic was covered; the second means sufficient understanding was demonstrated in an assessment. `[x] [ ]` means studied but not yet confirmed; `[x] [x]` means studied and assessed with sufficient understanding. Topics with partial understanding keep the second box unchecked and receive review guidance in the session note.
