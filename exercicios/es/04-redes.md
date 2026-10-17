# Secuencia 4 — Redes sociales en automático (r7e, promoavatar, xviral)

**Objetivo:** crear el canal de tu nicho que publica con regularidad, con cifras, fuentes y tu rostro, y con tu aprobación en lo que importa.
**Base:** reel7etapas (https://inematds.github.io/reel7etapas/guia/), promoavatar (https://inematds.github.io/promoavatar/guia/), promoavatar3 (https://inematds.github.io/promoavatar3/guia/), finviral (https://inematds.github.io/finviral/guia/), saudeviral (https://inematds.github.io/saudeviral/guia/) y advviral (https://inematds.github.io/advviral/guia/).
**Requisito previo:** Secuencias 1, 2 y 3. Sin cola ni puerta de control, automatizar las redes sociales solo hace que publiques mal más rápido.

---

## E1. Un reel en 7 etapas, sobre el papel (20 min)

Escribe un reel de 30 a 45 segundos de tu nicho con el modelo r7e:

| # | Etapa | Tu frase |
|---|---|---|
| 1 | Gancho (el resultado en 2 s) | |
| 2 | Deseo | |
| 3 | Miedo | |
| 4 | Facilidad | |
| 5 | Descubrimiento (el nombre de la solución) | |
| 6 | Beneficio | |
| 7 | Comentario («comenta PALABRA») | |

**Listo cuando:** lo lees en voz alta en menos de 45 s y la primera frase ya dice cuál es el beneficio.

## E2. Los 5 de tu nicho (20 min)

Elige 5 canales de referencia de tu nicho (inmuebles, agro, belleza, educación…). Para cada uno: nombre, enlace, frecuencia de videos, tema que más rinde. Escribe también las **reglas del nicho**: qué cuenta como hecho, el aviso obligatorio (por ejemplo: «no es una recomendación de inversión», «no reemplaza una consulta») y qué nunca publicas.

**Listo cuando:** tienes `canais.md` y `regras.md` de tu nicho.

## E3. La base con fuentes (30 min)

Toma la transcripción de un video de uno de los 5 canales (inemavox u otro transcriptor local se encarga). Arma `base.md`:

| Número o hecho | Quién lo dijo | Video | Fragmento literal |
|---|---|---|---|

**Listo cuando:** cada fila tiene el fragmento literal y lo encontraste en la transcripción. Es exactamente lo que hace por sí solo el `checar.py` de finviral.

## E4. Guion de 60 s con la fuente en pantalla (30 min)

Con `base.md`, pídele al agente un guion de 60 s: apertura con la cifra más contundente, tres hechos con quién los dijo, el aviso del nicho y la invitación final. Escribe los números con palabras en lo que se dice.

**Listo cuando:** todas las cifras del guion están en `base.md`. Si alguna no está, el guion se devuelve.

## E5. El calendario (20 min)

Decide la frecuencia (por ejemplo: de lunes a viernes cada 2 h, uno largo el sábado) y escribe la programación (cron o timer de systemd), como lo hace finviral. Regla: **un día flojo no se convierte en video**, y un fallo te avisa por Telegram.

**Listo cuando:** la programación está escrita y sabes qué pasa un día sin tema.

## E6. La puerta antes de publicar (una semana)

Haz una semana con aprobación manual antes de cada publicación. Anota qué rechazaste y por qué. Cada rechazo se convierte en una regla en `regras.md`.

**Listo cuando:** pasaste 3 días seguidos sin tener que rechazar nada. Solo entonces piensa en quitar la puerta de control de alguna etapa.

---

### Desafío extra
Haz un promoavatar de tu nicho: 3 videos para el mismo público (alcance, autoridad y promocional) y compara cuál recibe más comentarios.