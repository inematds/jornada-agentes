# Jornada dos Agentes — do chat ao criador de agentes

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Do chat ao criador de agentes](guia/assets/banner.jpg)](https://inematds.github.io/jornada-agentes/guia/)

## O que é

Este repositório reúne os exercícios da série INEMA "Do chat ao criador de agentes". São quatro sequências, em ordem: usar o agente no terminal, montar um assistente pessoal pelo Telegram, colocar tarefas numa fila que roda sozinha e automatizar redes sociais com aprovação sua. Serve para quem já usa o chat da IA e quer que ela trabalhe por conta própria. Cada exercício tem um "pronto quando" que diz se você terminou. Você precisa de um computador, do terminal e do Claude Code ou do Codex.

## 📖 Guia de uso

Guia completo (landing + passo a passo): **https://inematds.github.io/jornada-agentes/guia/**

## As 4 sequências

A ordem importa: sem a sequência 1, as outras não ficam de pé. Sem milagre: o sistema precisa rodar correto antes de rodar sozinho.

| # | Sequência | Exercícios | Base |
|---|---|---|---|
| 1 | Do chat para o terminal (OSWork) | [exercicios/01-oswork.md](exercicios/01-oswork.md) | [curso](https://inematds.github.io/oswork-quick/) · [área](https://eventos.inema.pro/oswork/) |
| 2 | Crie o seu Jarvis (INTELECTO) | [exercicios/02-jarvis.md](exercicios/02-jarvis.md) | [INTELECTO](https://inematds.github.io/intelecto/) · [curso](https://inematds.github.io/intelecto-curso/) · [área](https://eventos.inema.pro/jarvis/) |
| 3 | Filas de agentes (inemaccbot) | [exercicios/03-filas.md](exercicios/03-filas.md) | [guia](https://inematds.github.io/inemaccbot/guia/) · [curso](https://eventos.inema.pro/inemaccbot.html) |
| 4 | Redes sociais no automático | [exercicios/04-redes.md](exercicios/04-redes.md) | [reel7etapas](https://inematds.github.io/reel7etapas/guia/) · [promoavatar](https://inematds.github.io/promoavatar/guia/) · [promoavatar3](https://inematds.github.io/promoavatar3/guia/) · [finviral](https://inematds.github.io/finviral/guia/) · [saudeviral](https://inematds.github.io/saudeviral/guia/) · [advviral](https://inematds.github.io/advviral/guia/) |

Página da série: https://eventos.inema.pro/do-chat-ao-agente/

## Fila caseira

`ferramentas/fila-caseira.sh` é uma fila mínima para entender a ideia antes do inemaccbot: cada arquivo em `entrada/` vira uma tarefa, a resposta vai para `feito/`, o erro vai para `falhou/`, e uma rodada interrompida retoma de onde parou.

```bash
mkdir -p fila/entrada
echo "Resuma em 5 linhas o que é uma fila de tarefas." > fila/entrada/01.md
echo "Liste 3 riscos de deixar um agente rodando sozinho." > fila/entrada/02.md
./ferramentas/fila-caseira.sh fila          # motor padrão: claude
./ferramentas/fila-caseira.sh fila codex    # ou o Codex
```

## Vídeos

Cinco vídeos (abertura + um por sequência), cada um com a sua página explicativa em [serie/](https://inematds.github.io/jornada-agentes/serie/jornada-ia/) (PT/EN/ES). Roteiros: [videos/roteiros.md](videos/roteiros.md).

## Estrutura

```
exercicios/            exercícios em PT (en/ e es/ traduzidos)
ferramentas/           fila-caseira.sh
guia/                  página do guia (PT, en/, es/)
videos/roteiros.md     roteiros dos 5 vídeos
```

---

Tudo aberto e gratuito no **[INEMA.CLUB](https://inema.club)**.
