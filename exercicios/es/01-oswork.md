# Secuencia 1 — Del chat a la terminal (OSWork)

**Objetivo:** salir del chat y poner a un agente a trabajar dentro de una carpeta tuya.
**Base:** curso OSWork (https://inematds.github.io/oswork-quick/) y área https://eventos.inema.pro/oswork/
**Vas a necesitar:** una computadora, la terminal (cmd en Windows; Terminal en Mac y Linux) y Claude Code o Codex instalados.

Hazlo en orden. Cada ejercicio tiene un **Listo cuando**: pasa al siguiente solo cuando se cumpla.

---

## E1. Tu primera carpeta desde la terminal (10 min)

1. Abre la terminal.
2. Crea la carpeta `projetos` y, dentro de ella, `meu-primeiro-agente`.
3. Entra en ella y lista el contenido (estará vacía).
4. Abre la misma carpeta desde el Explorador de archivos (o Finder) y compara.

**Listo cuando:** llegas a la carpeta solo desde la terminal, sin el mouse, y sabes decir en qué carpeta estás.

## E2. El manual del empleado: AGENTS.md (15 min)

Crea, dentro de la carpeta, un archivo `AGENTS.md` con:

```markdown
# Quién soy
<tu nombre, tu profesión, para quién trabajas>

# Reglas de este proyecto
- Escribe en portugués, con frases cortas.
- No borres archivos sin preguntar.
- Antes de terminar, di qué cambió y cómo puedo comprobarlo.

# Qué hay aquí
- index.html: mi página
```

**Listo cuando:** el archivo existe y tiene al menos tres reglas tuyas, escritas por ti.

## E3. La primera tarea (15 min)

Dentro de la carpeta, llama al agente (`claude` o `codex`) y pídele:

> Lee el AGENTS.md. Crea un index.html con una página sencilla sobre mí, usando lo que está ahí.

Abre la página en el navegador. Pídele un cambio (color, texto, una sección nueva) y vuelve a comprobarla.

**Listo cuando:** la página se abre en el navegador y le pediste al agente al menos **una corrección**. Dar la tarea, comprobar y decidir: eso es gestión.

## E4. La red de seguridad: Git (20 min)

1. En la carpeta: `git init`, luego `git add .` y `git commit -m "primeira versão"`.
2. Pídele al agente un cambio grande en la página.
3. ¿No te gustó? Vuelve atrás: `git restore index.html` (o `git checkout -- index.html`).

**Listo cuando:** deshiciste un cambio del agente con un comando, sin entrar en pánico.

## E5. Los secretos no van en el texto (10 min)

1. Crea un archivo `.env` con una línea falsa: `MINHA_CHAVE=teste123`.
2. Crea un `.gitignore` con la línea `.env`.
3. Ejecuta `git status`: `.env` **no** debe aparecer.
4. Añade al AGENTS.md: "Nunca escribas claves o contraseñas en un archivo de texto; deben estar en .env".

**Listo cuando:** `git status` no muestra `.env`.

## E6. El agente lee tus archivos (20 min)

Coloca en la carpeta tres archivos de texto tuyos (apuntes, un acta, un correo largo). Pídele:

> Lee los archivos .txt de esta carpeta y escribe resumen.md con 5 decisiones y 5 asuntos pendientes, citando de qué archivo proviene cada una.

Comprueba dos citas en el archivo original.

**Listo cuando:** encontraste en el original al menos dos de las frases citadas. Si alguna no existe, anota en AGENTS.md la regla que faltó.

---

### Desafío extra
Repite E3 con el **otro** agente (si usaste Claude Code, usa Codex). Ambos leen el mismo AGENTS.md. ¿Qué cambió en el resultado?