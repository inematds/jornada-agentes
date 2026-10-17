# FALHAS — jornada-agentes

Uma linha por falha, mais recente no topo.

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-10-17 | Tradução ES das páginas da série (codex gpt-6-luna) terminou com rc=0, mas ~200 textos ficaram em português | verificador de "texto igual ao PT" dentro do prompt, rodando até dar 0 | prompt |
| 2026-10-17 | Banner da capa esticado na vertical nas páginas da série | `height:auto` na imagem da hero (tinha `height=788` no HTML) | prompt |
| 2026-10-17 | Banner da visão geral com "degraıu" no texto desenhado pelo Codex | conferir o texto ampliado e regerar o banner | infra |
