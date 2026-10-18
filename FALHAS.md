# FALHAS — jornada-agentes

Uma linha por falha, mais recente no topo.

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-10-17 | Baixador só-estúdio parou o vídeo jornada-ia com "ID não existe" (leitura passageira da página; o vídeo estava na fila do HeyGen em 0%) e, no meio, o motor trocou o baixador para API (explicavideos 2.13.9) | cópia fixa do baixador só-estúdio em output/.../producao/baixar-estudio.mjs, com "não existe" valendo só 3 vezes seguidas; conferir Projetos antes de qualquer reenvio | infra |
| 2026-10-17 | Tradução ES das páginas da série (codex gpt-6-luna) terminou com rc=0, mas ~200 textos ficaram em português | verificador de "texto igual ao PT" dentro do prompt, rodando até dar 0 | prompt |
| 2026-10-17 | Banner da capa esticado na vertical nas páginas da série | `height:auto` na imagem da hero (tinha `height=788` no HTML) | prompt |
| 2026-10-17 | Banner da visão geral com "degraıu" no texto desenhado pelo Codex | conferir o texto ampliado e regerar o banner | infra |
