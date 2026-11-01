# informal-studies

Este repositório acompanha estudos pessoais em arquivos Markdown e Git.

- Cada estudo fica em `studies/<slug>/` e sua lista de tópicos é `plan.md`.
- Preserve o formato de tópico documentado em `studies/README.md` e no modelo `templates/study/plan.md`.
- Use `$finalizar-sessao` para propor quais tópicos da conversa foram cobertos. Peça confirmação antes de alterar as caixas de progresso.
- Use `$avaliar-compreensao` para verificar o entendimento. Não conclua domínio apenas porque a pessoa fez perguntas; use explicações e aplicações demonstradas.
- Quando um plano mudar, execute `python scripts/update_progress.py` para manter o painel do README alinhado.
- Depois de uma skill alterar arquivos, pergunte se a pessoa quer commit e push. Só faça commit ou push após um “sim” explícito para essa pergunta; limite o commit aos arquivos desta sessão e deste repositório.
- Não invente tópicos de estudo nem marque progresso sem evidência na conversa e confirmação da pessoa.
