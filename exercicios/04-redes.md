# Sequência 4 — Redes sociais no automático (r7e, promoavatar, xviral)

**Objetivo:** montar o canal do seu nicho que publica com regularidade, com números, fontes e o seu rosto, e com você aprovando o que importa.
**Base:** reel7etapas (https://inematds.github.io/reel7etapas/guia/), promoavatar (https://inematds.github.io/promoavatar/guia/), promoavatar3 (https://inematds.github.io/promoavatar3/guia/), finviral (https://inematds.github.io/finviral/guia/), saudeviral (https://inematds.github.io/saudeviral/guia/) e advviral (https://inematds.github.io/advviral/guia/).
**Pré-requisito:** Sequências 1, 2 e 3. Sem fila e sem portão, automatizar rede social vira postar errado mais rápido.

---

## E1. Um reel em 7 etapas, no papel (20 min)

Escreva um reel de 30 a 45 segundos do seu nicho no modelo r7e:

| # | Etapa | Sua frase |
|---|---|---|
| 1 | Gancho (o resultado em 2 s) | |
| 2 | Desejo | |
| 3 | Medo | |
| 4 | Facilidade | |
| 5 | Descoberta (o nome da solução) | |
| 6 | Benefício | |
| 7 | Comentário ("comenta PALAVRA") | |

**Pronto quando:** você lê em voz alta em menos de 45 s e a primeira frase já diz o ganho.

## E2. Os 5 do seu nicho (20 min)

Escolha 5 canais de referência do seu nicho (imóveis, agro, beleza, educação…). Para cada um: nome, link, frequência de vídeos, assunto que mais rende. Escreva também as **regras do nicho**: o que conta como fato, o aviso obrigatório (ex.: "não é recomendação de investimento", "não substitui consulta") e o que você nunca publica.

**Pronto quando:** você tem `canais.md` e `regras.md` do seu nicho.

## E3. A base com fonte (30 min)

Pegue a transcrição de um vídeo de um dos 5 canais (o inemavox ou outro transcritor local resolve). Monte `base.md`:

| Número ou fato | Quem disse | Vídeo | Trecho literal |
|---|---|---|---|

**Pronto quando:** cada linha tem o trecho literal e você achou cada trecho na transcrição. É exatamente o que o `checar.py` do finviral faz sozinho.

## E4. Roteiro de 60 s com fonte na tela (30 min)

Com a `base.md`, peça ao agente um roteiro de 60 s: abertura com o número mais forte, três fatos com quem disse, o aviso do nicho e o convite final. Números por extenso na fala.

**Pronto quando:** todo número do roteiro está na `base.md`. Se algum não estiver, o roteiro volta.

## E5. A agenda (20 min)

Decida a frequência (ex.: segunda a sexta às 2 h, um longo no sábado) e escreva o agendamento (cron ou timer do systemd), como o finviral faz. Regra: **dia fraco não vira vídeo**, e falha avisa você no Telegram.

**Pronto quando:** o agendamento está escrito e você sabe o que acontece num dia sem assunto.

## E6. O portão antes de publicar (uma semana)

Rode uma semana com aprovação manual antes de cada publicação. Anote o que você recusou e por quê. Cada recusa vira uma regra em `regras.md`.

**Pronto quando:** você passou 3 dias seguidos sem precisar recusar. Só então pense em tirar o portão de alguma etapa.

---

### Desafio extra
Faça um promoavatar do seu nicho: 3 vídeos para o mesmo público (alcance, autoridade e promocional) e compare qual traz mais comentários.
