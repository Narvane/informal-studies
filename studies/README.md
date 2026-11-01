# Estudos

Adicione cada assunto em uma pasta própria, por exemplo `studies/aws/plan.md`. Use o modelo em `../templates/study/plan.md` e dê a cada tópico um ID estável e único dentro daquele estudo.

Formato dos tópicos (primeira caixa = estudado; segunda = compreensão demonstrada):

```markdown
- [ ] [ ] **AWS-001** — Conceito ou habilidade
```

Depois de criar ou editar o plano, rode `python scripts/update_progress.py`. O painel no README da raiz conta apenas pastas de estudo que tenham `plan.md`.
