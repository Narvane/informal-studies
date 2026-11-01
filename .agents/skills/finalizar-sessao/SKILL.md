---
name: finalizar-sessao
description: Feche uma sessão de estudo identificando os tópicos realmente cobertos na conversa, proponha atualizações ao plano e registre um resumo após a confirmação do usuário.
---

# Finalizar sessão de estudo

Use esta skill quando a pessoa disser que quer finalizar, encerrar ou registrar uma sessão de estudo. Ela registra cobertura do conteúdo; não avalia domínio ou compreensão.

## Fluxo

1. Identifique o estudo ativo pela pasta de trabalho atual ou pelo contexto explícito da conversa. O plano deve estar em `studies/<slug>/plan.md`. Se houver mais de um estudo plausível ou nenhum plano, pergunte qual estudo usar ou ajude a pessoa a cadastrar um. Não crie tópicos por conta própria.
2. Leia o plano e compare seus tópicos com a conversa desta sessão. Proponha apenas tópicos que foram abordados de forma substantiva, com uma evidência curta da conversa. Distingua cobertura parcial de conteúdo que não foi abordado.
3. Mostre os IDs e títulos que pretende marcar como estudados, junto com qualquer sugestão de tópico novo ou ajuste de escopo. Não altere arquivos ainda. Peça uma confirmação clara para aplicar as mudanças propostas.
4. Se a pessoa confirmar, atualize somente as caixas de cobertura aprovadas na primeira posição (`[x] [ ]` ou `[x] [x]`, preservando a segunda caixa existente). Não marque compreensão nesta skill. Se a pessoa recusar ou ajustar a proposta, respeite a resposta; não faça alterações sem confirmação.
5. Após aplicar mudanças, registre um resumo em `studies/<slug>/sessions/AAAA-MM-DD-<slug-da-sessao>.md`. Inclua tópicos confirmados, evidências resumidas, dúvidas ou pontos a retomar e próximos passos. Não copie a conversa inteira. Use a data local disponível; se não estiver disponível, pergunte ou use apenas a data informada pelo usuário. Se o nome já existir, acrescente `-2`, `-3` e assim por diante para preservar o registro anterior.
6. Rode `python scripts/update_progress.py` na raiz do repositório para atualizar o painel do README. Se `python` não iniciar no Codex desktop, consulte `mcp__codex_app__load_workspace_dependencies` e use o Python empacotado informado; se não houver runtime disponível, preserve os outros arquivos e informe o erro.
7. Revise `git status` e mostre um resumo conciso do que foi alterado. Pergunte: **“Quer que eu faça commit e push dessas alterações?”**
8. Só se a pessoa responder afirmativamente a essa pergunta, faça commit e tente o push. Inspecione o diff e o remoto configurado; inclua no commit apenas as alterações relacionadas a esta sessão, sem incorporar trabalho alheio. Use uma mensagem de commit clara. Se não houver remoto, faça o commit local autorizado e explique que o push ainda depende de configurar um remoto. Se o push falhar, informe o motivo específico. Se a resposta for negativa, deixe as alterações locais.

Se não houver tópico novo para marcar, não force uma alteração de progresso. Você ainda pode criar um breve registro de sessão após confirmação da pessoa; em seguida, atualize o painel se algum plano mudou e ofereça commit/push para as alterações feitas pela skill.
