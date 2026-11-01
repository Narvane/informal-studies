# informal-studies

Um espaço simples para estudar assuntos com apoio do Codex e acompanhar o progresso em arquivos versionados.

## Progresso dos estudos

Os números abaixo são gerados a partir dos tópicos em `studies/*/plan.md`. As skills de estudo atualizam este painel depois de cada alteração confirmada.

<!-- STUDY_PROGRESS:START -->
_Nenhum estudo cadastrado ainda. Veja `studies/README.md` para adicionar o primeiro._
<!-- STUDY_PROGRESS:END -->

## Como usar

1. Crie uma pasta em `studies/` e um `plan.md` para o assunto. Veja o modelo em `templates/study/plan.md`.
2. Abra essa pasta no Codex e estude conversando normalmente.
3. Ao terminar, invoque `$finalizar-sessao` para revisar quais tópicos foram cobertos.
4. Invoque `$avaliar-compreensao` para verificar o que você consegue explicar e aplicar.
5. Revise e confirme as alterações propostas. As skills atualizam o plano, registram um resumo da sessão e regeneram este painel.
6. Ao final de cada skill que alterou arquivos, ela perguntará se você quer fazer commit e push. Só executará essas ações após sua confirmação.

Para regenerar o painel manualmente, rode `python scripts/update_progress.py` na raiz do repositório.

## Estados dos tópicos

Cada tópico tem duas caixas: a primeira indica que o assunto foi coberto; a segunda indica que a compreensão foi demonstrada na avaliação. Assim, `[x] [ ]` significa estudado, mas ainda sem compreensão confirmada; `[x] [x]` significa estudado e avaliado com compreensão suficiente. Tópicos parcialmente compreendidos ficam sem a segunda marca e recebem orientação para revisão no registro da sessão.

\n