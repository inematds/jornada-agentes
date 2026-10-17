# Secuencia 2 — Crea tu propio Jarvis (INTELECTO)

**Objetivo:** tener un asistente personal propio que hable por Telegram, recuerde las conversaciones y tenga la personalidad que tú definas.  
**Base:** INTELECTO (https://inematds.github.io/intelecto/), curso (https://inematds.github.io/intelecto-curso/) y área https://eventos.inema.pro/jarvis/  
**Requisito previo:** haber completado la Secuencia 1 (terminal, carpetas, `.env`).

---

## E1. Diseña tu Jarvis antes de instalarlo (15 min)

En un archivo `meu-jarvis.md`, responde:

- Nombre del asistente y cómo habla (formal, directo, con buen humor).
- Tres cosas que **debe** hacer por ti cada semana.
- Tres cosas que **nunca** debe hacer.
- Qué necesita recordar sobre ti (profesión, rutina, preferencias).

**Listo cuando:** el archivo cabe en una pantalla y otra persona podría entender cómo es tu asistente.

## E2. El bot en Telegram (10 min)

En Telegram, abre `@BotFather`, envía `/newbot` y elige un nombre y un @usuario. Guarda el token **solo** en `.env` (regla de la Secuencia 1).

**Listo cuando:** tienes el token y no aparece en ningún archivo aparte de `.env`.

## E3. Instalar (30 min)

```bash
git clone https://github.com/inematds/intelecto.git
cd intelecto
./start.sh
```

El asistente de configuración te pide el token de Telegram, el modelo y la personalidad. Usa tu `meu-jarvis.md` para responder.

**Listo cuando:** envías «hola» por Telegram y te responde con el nombre y el estilo que definiste.

## E4. Prueba de memoria (2 días)

1. Día 1: cuéntale tres cosas sobre ti (por ejemplo: «todos los lunes cierro el informe de ventas»).
2. Día 2, en una conversación nueva: pregunta «¿qué hago todos los lunes?».

**Listo cuando:** lo recuerda sin que tengas que repetirlo. Si no lo recuerda, consulta en el curso cómo se guarda la memoria y haz los ajustes necesarios.

## E5. Nube o local (20 min)

Haz la misma pregunta dos veces: una con un modelo en la nube (OpenRouter) y otra con un modelo local (Ollama), si tu computadora puede soportarlo. Anota en una tabla: tiempo de respuesta, calidad y costo.

**Listo cuando:** sabes decir qué modelo usar para cada tarea, con tus propios datos.

## E6. Una rutina real (20 min)

Elige una de las tres tareas de E1 y conviértela en una solicitud fija (por ejemplo: «todas las mañanas, cuando te diga “día”, enumera mis tres prioridades a partir de lo que te conté ayer»). Úsala durante una semana.

**Listo cuando:** la usaste durante 5 días seguidos y anotaste qué se puede mejorar.

---

### Desafío extra
Escribe en `meu-jarvis.md` la lista de tareas que te gustaría encargarle antes de irte a dormir. Esa lista es la entrada de la Secuencia 3.