---
name: avaliar-compreensao
description: Avalie a compreensão dos tópicos estudados usando explicações e aplicações demonstradas na conversa, proponha mudanças no plano e registre o resultado após confirmação.
---

# Avaliar compreensão

Use esta skill quando a pessoa pedir para avaliar, testar ou revisar o quanto compreendeu um estudo. Avaliar significa procurar evidência de compreensão suficiente; perguntas feitas pela pessoa, por si só, não provam domínio.

## Fluxo

1. Identifique o estudo ativo e leia `studies/<slug>/plan.md`. Considere os tópicos já marcados como estudados. Se o estudo estiver ambíguo, pergunte qual usar.
2. Revise a conversa desta sessão procurando explicações com as próprias palavras, conexões entre conceitos, previsões e aplicações. Não trate uma resposta dada depois de explicação completa do assistente como evidência independente.
3. Para cada tópico, classifique a evidência como **compreensão demonstrada**, **parcial / revisar** ou **evidência insuficiente**. Se a conversa não fornecer evidência adequada, faça perguntas curtas, uma de cada vez, e espere as respostas antes de concluir. Prefira pedir explicação e aplicação a perguntas de mera memorização.
4. Mostre a proposta por ID, com evidência concisa e resultado. Peça confirmação antes de gravar qualquer avaliação. Nunca marque tópico como estudado nesta skill; se a cobertura ainda não estiver registrada, peça que a pessoa use `finalizar-sessao` antes de registrar a avaliação.
5. Após confirmação, marque a segunda caixa (`[x] [x]`) apenas nos tópicos já estudados cuja compreensão foi demonstrada. Para os demais, deixe a segunda caixa vazia e registre no resumo o que deve ser revisado. Uma avaliação inconclusiva não deve ser apresentada como domínio.
6. Registre o resultado em `studies/<slug>/sessions/AAAA-MM-DD-avaliacao-<slug>.md`: tópicos avaliados, evidências resumidas, pontos fortes, lacunas e recomendações de revisão. Não copie a conversa inteira. Use a data local disponível; se não estiver disponível, pergunte ou use apenas a data informada pelo usuário. Se o nome já existir, acrescente `-2`, `-3` e assim por diante para preservar o registro anterior.
7. Rode `python scripts/update_progress.py` na raiz do repositório para atualizar o painel. Se `python` não iniciar no Codex desktop, consulte `mcp__codex_app__load_workspace_dependencies` e use o Python empacotado informado; se não houver runtime disponível, preserve os outros arquivos e informe o erro. Revise `git status` e mostre um resumo conciso das mudanças.
8. Pergunte: **“Quer que eu faça commit e push dessas alterações?”** Só após um “sim” explícito, faça commit e tente o push apenas das alterações ligadas à avaliação nesta sessão. Antes, confira o diff e o remoto configurado. Se não houver remoto, faça o commit local autorizado e explique que o push ainda depende de configurar um remoto. Se o push falhar, informe o motivo específico; se a resposta for negativa, deixe tudo local.

\n