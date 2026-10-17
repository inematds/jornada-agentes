# Secuencia 3 — Colas de agentes (inemaccbot)

**Objetivo:** enviar varias tareas, alejarte y encontrar el trabajo hecho, con una puerta de aprobación cuando te necesite.
**Base:** inemaccbot (https://inematds.github.io/inemaccbot/guia/) y curso https://eventos.inema.pro/inemaccbot.html
**Requisito previo:** Secuencias 1 y 2.

---

## E1. La cola en papel (15 min)

Enumera 10 tareas repetitivas de tu trabajo. Para cada una, indica:

| Tarea | ¿Se ejecuta sola? | ¿Necesita una puerta (tu aprobación)? | ¿Dónde está la puerta? |
|---|---|---|---|
| Transcribir la reunión | sí | no | — |
| Publicación de la semana | sí | sí | antes de publicar |

**Listo cuando:** las 10 filas están completas y al menos dos tienen una puerta.

## E2. Una cola casera en 30 líneas (30 min)

Antes del bot, entiende la idea con `ferramentas/fila-caseira.sh` de este repo:

```bash
mkdir -p fila/entrada
echo "Resume en 5 líneas qué es una cola de tareas." > fila/entrada/01.md
echo "Enumera 3 riesgos de dejar un agente ejecutándose solo." > fila/entrada/02.md
./ferramentas/fila-caseira.sh fila
```

Cada archivo de `entrada/` se convierte en una tarea. La respuesta va a `feito/`. Si se produce un error, la tarea va a `falhou/`. Al ejecutarlo de nuevo, solo toma lo que quedó pendiente.

**Listo cuando:** las dos tareas están en `fila/feito/` con la respuesta, y detuviste (Ctrl+C) una ejecución y viste que la cola continuó desde donde quedó.

## E3. Instalar el inemaccbot (1 h)

Sigue la guía hasta que `/ping` responda en Telegram. Después: `/ajuda` muestra los comandos y `/fila` muestra las colas.

**Listo cuando:** `/ping` responde en tu Telegram.

## E4. Diez tareas y a dormir (1 noche)

Envía al bot entre 5 y 10 tareas de tu lista del E1 (transcribir, resumir, explicar…). Dedícate a otra cosa.

**Listo cuando:** al día siguiente revisas el resultado de cada una y anotas cuántas salieron bien a la primera.

## E5. La puerta de aprobación (30 min)

Usa un flujo con puerta de aprobación (como `/promoavatar`): el bot escribe los textos y **se detiene**. Léelos, corrígelos si hace falta y solo entonces aprueba.

**Listo cuando:** rechazaste o corregiste al menos un texto antes de aprobarlo. Ese es el momento en que gestionas, en vez de hacerlo tú.

---

### Desafío extra
Toma la tarea que más falló en E4 y escribe para ella una regla nueva (en AGENTS.md o en el prompt de la skill). Ejecútala de nuevo y compara.