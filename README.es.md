# Jornada de Agentes — del chat al creador de agentes

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Del chat al creador de agentes](guia/assets/banner-es.jpg)](https://inematds.github.io/jornada-agentes/guia/es/)

## Qué es

Este repositorio reúne los ejercicios de la serie INEMA "Del chat al creador de agentes". Son cuatro secuencias, en orden: usar el agente en la terminal, crear un asistente personal en Telegram, poner tareas en una cola que funciona sola y automatizar redes sociales con tu aprobación. Es para quienes ya usan el chat de IA y quieren que trabaje por su cuenta. Cada ejercicio tiene un "listo cuando" que indica si lo terminaste. Necesitas una computadora, la terminal y Claude Code o Codex.

## 📖 Guía de uso

Guía completa (landing + paso a paso): **https://inematds.github.io/jornada-agentes/guia/es/**

## Las 4 secuencias

El orden importa: sin la secuencia 1, las demás no se sostienen. Sin milagros: el sistema tiene que funcionar bien antes de funcionar solo.

| # | Secuencia | Ejercicios | Base |
|---|---|---|---|
| 1 | Del chat a la terminal (OSWork) | [exercicios/es/01-oswork.md](exercicios/es/01-oswork.md) | [curso](https://inematds.github.io/oswork-quick/) · [área](https://eventos.inema.pro/oswork/) |
| 2 | Crea tu Jarvis (INTELECTO) | [exercicios/es/02-jarvis.md](exercicios/es/02-jarvis.md) | [INTELECTO](https://inematds.github.io/intelecto/) · [curso](https://inematds.github.io/intelecto-curso/) · [área](https://eventos.inema.pro/jarvis/) |
| 3 | Colas de agentes (inemaccbot) | [exercicios/es/03-filas.md](exercicios/es/03-filas.md) | [guía](https://inematds.github.io/inemaccbot/guia/) · [curso](https://eventos.inema.pro/inemaccbot.html) |
| 4 | Redes sociales en automático | [exercicios/es/04-redes.md](exercicios/es/04-redes.md) | [reel7etapas](https://inematds.github.io/reel7etapas/guia/) · [promoavatar](https://inematds.github.io/promoavatar/guia/) · [promoavatar3](https://inematds.github.io/promoavatar3/guia/) · [finviral](https://inematds.github.io/finviral/guia/) · [saudeviral](https://inematds.github.io/saudeviral/guia/) · [advviral](https://inematds.github.io/advviral/guia/) |

Página de la serie: https://eventos.inema.pro/do-chat-ao-agente/es/

## Cola casera

`ferramentas/fila-caseira.sh` es una cola mínima para entender la idea antes del inemaccbot: cada archivo en `entrada/` se convierte en una tarea, la respuesta va a `feito/` (hecho), el error va a `falhou/` (falló), y una ejecución interrumpida continúa desde donde quedó.

```bash
mkdir -p fila/entrada
echo "Resume en 5 líneas qué es una cola de tareas." > fila/entrada/01.md
echo "Enumera 3 riesgos de dejar un agente funcionando solo." > fila/entrada/02.md
./ferramentas/fila-caseira.sh fila          # motor predeterminado: claude
./ferramentas/fila-caseira.sh fila codex    # o Codex
```

## Videos

Cinco videos (apertura + uno por secuencia), cada uno con su página explicativa en [serie/](https://inematds.github.io/jornada-agentes/serie/jornada-ia/es/) (PT/EN/ES). Guiones (en portugués): [videos/roteiros.md](videos/roteiros.md).

## Estructura

```
exercicios/            ejercicios en PT (en/ y es/ traducidos)
ferramentas/           fila-caseira.sh
guia/                  página de la guía (PT, en/, es/)
videos/roteiros.md     guiones de los 5 videos
```

---

Todo abierto y gratuito en **[INEMA.CLUB](https://inema.club)**.
