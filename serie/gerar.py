#!/usr/bin/env python3
"""Gera as páginas da série "Do chat ao agente" em serie/<id>/ (PT) e serie/<id>/en|es/.

Fontes:
  serie/conteudo/{pt,en,es}.json   textos de cada página (PT é a fonte; EN/ES são traduções)
  serie/roteiros/<id>.json         roteiro do vídeo (cenas faladas, PT)
  serie/videos.json                vídeo publicado de cada página (url do MP4 + legenda); sem entrada = "em produção"
  serie/assets/serie-<id>.jpg      banner da hero
Uso: python3 serie/gerar.py
"""
import html, json, pathlib, re

AQUI = pathlib.Path(__file__).resolve().parent
ORDEM = ["jornada-ia", "seq1-oswork", "seq2-jarvis", "seq3-filas", "seq4-redes"]
LANGS = ["pt", "en", "es"]
BASE = "https://inematds.github.io/jornada-agentes/serie/"
EX_DIR = {"pt": "", "en": "en/", "es": "es/"}
AREA = {"pt": "https://eventos.inema.pro/do-chat-ao-agente/",
        "en": "https://eventos.inema.pro/do-chat-ao-agente/en/",
        "es": "https://eventos.inema.pro/do-chat-ao-agente/es/"}
ICON = {"jornada-ia": "🧭", "seq1-oswork": "💻", "seq2-jarvis": "🧠", "seq3-filas": "📋", "seq4-redes": "📣"}

CSS = (AQUI / "estilo.css").read_text(encoding="utf-8")
JS = """<script>
(function(){var b=document.body,k='jornada-tema';try{if(localStorage.getItem(k)==='light')b.classList.add('light')}catch(e){}
var t=document.getElementById('tgl');if(t)t.addEventListener('click',function(){b.classList.toggle('light');
try{localStorage.setItem(k,b.classList.contains('light')?'light':'dark')}catch(e){}});})();
</script>"""


def ban(p, lang):
    """banner do idioma; se ainda não existir, usa o PT"""
    nome = f"serie-{p}-{lang}.jpg"
    return nome if lang != "pt" and (AQUI / "assets" / nome).exists() else f"serie-{p}.jpg"


def links_lang(txt, lang):
    """links relativos entre páginas da série (../seqX/) apontam para o mesmo idioma"""
    if lang == "pt":
        return txt
    return re.sub(r'href="\.\./((?!en/|es/)[a-z0-9-]+)/"', lambda m: f'href="../../{m.group(1)}/{lang}/"', txt)


def esc(s):
    return html.escape(s, quote=True)


def bloco(b, ui, lang, pref):
    t = b["type"]
    if t == "p":
        return f'<p class="txt">{b["text"]}</p>'
    if t == "note":
        return f'<p class="note">{b["text"]}</p>'
    if t == "quote":
        return f'<blockquote class="pedido">{b["text"]}</blockquote>'
    if t == "code":
        return f'<pre>{b["text"]}</pre>'
    if t == "flow":
        partes = []
        for i, it in enumerate(b["items"]):
            if i:
                partes.append('<span class="arr" aria-hidden="true">→</span>')
            partes.append(f"<span>{it}</span>")
        return f'<div class="flow">{"".join(partes)}</div>'
    if t == "pills":
        return '<div class="pills">' + "".join(f'<span class="pill">{i}</span>' for i in b["items"]) + "</div>"
    if t == "cards":
        n = len(b["items"])
        g = "g3" if n == 3 else ("g2" if n in (2, 4) else "g3")
        cs = "".join(f'<div class="card"><h3>{c["title"]}</h3><p>{c["text"]}</p></div>' for c in b["items"])
        return f'<div class="grid {g}">{cs}</div>'
    if t == "steps":
        out = []
        for i, s in enumerate(b["items"], 1):
            out.append(f'<div class="step"><div class="b">{i}</div><div><h3>{s["title"]}</h3><p>{s["text"]}</p></div></div>')
        return '<div class="steps">' + "".join(out) + "</div>"
    if t == "compare":
        def col(tit, itens, cls):
            li = "".join(f"<li>{x}</li>" for x in itens)
            return f'<div class="card {cls}"><h3>{tit}</h3><ul>{li}</ul></div>'
        return '<div class="grid g2">' + col(b["left_title"], b["left"], "lado-a") + col(b["right_title"], b["right"], "lado-b") + "</div>"
    if t == "table":
        th = "".join(f"<th>{h}</th>" for h in b["head"])
        trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in b["rows"])
        return f'<div class="tabela"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'
    if t == "seqcards":
        return SEQCARDS[lang]
    raise ValueError(t)


def pagina(pid, lang, C, roteiro, videos):
    ui, P = C["ui"], C["pages"][pid]
    sub = "" if lang == "pt" else f"{lang}/"
    pref = "../" if lang == "pt" else "../../"          # de serie/<id>/[lang/] até serie/
    assets = pref + "assets/"
    i = ORDEM.index(pid)
    url = f"{BASE}{pid}/{sub}"

    # navegação entre páginas da série
    def link(p):
        return f"{pref}{p}/{sub}"
    seqnav = "".join(
        f'<a href="{link(p)}"{" class=\"on\" aria-current=\"page\"" if p == pid else ""}>{C["pages"][p]["nav"]}</a>'
        for p in ORDEM)
    langs = "".join(
        f'<a href="{("../" * (0 if lang == "pt" else 1) + ("" if l == "pt" else l + "/")) or "./"}" hreflang="{l}"{" class=\"on\"" if l == lang else ""}>{l.upper()}</a>'
        for l in LANGS)
    hreflang = "".join(f'<link rel="alternate" hreflang="{"pt-BR" if l == "pt" else l}" href="{BASE}{pid}/{"" if l == "pt" else l + "/"}">' for l in LANGS)

    # vídeo
    v = videos.get(pid)
    if v:
        # legenda no idioma da página quando existir serie/vtt/<id>-<lang>.vtt (o áudio continua PT)
        vtt, sl, rot = v.get("vtt", ""), "pt", ui["subtitles"]
        if vtt and lang != "pt" and (AQUI / "vtt" / f"{pid}-{lang}.vtt").exists():
            vtt, sl, rot = vtt[:-4] + f"-{lang}.vtt", lang, {"en": "English", "es": "Español"}[lang]
        track = f'<track default kind="subtitles" src="{esc(vtt)}" srclang="{sl}" label="{rot}">' if vtt else ""
        player = (f'<div class="player"><video controls preload="metadata" playsinline poster="{assets}{ban(pid, lang)}">'
                  f'<source src="{esc(v["url"])}" type="video/mp4">{track}</video></div>')
    else:
        player = (f'<div class="player pendente"><img src="{assets}{ban(pid, lang)}" alt="" loading="lazy">'
                  f'<div class="aviso"><b>{ui["video_pending_title"]}</b><span>{ui["video_pending_text"]}</span></div></div>')
    cenas = "".join(
        f'<li><span class="cn">{ui["scene"]} {n}</span><b>{esc(c["title"])}</b><p>{esc(c["speech"])}</p></li>'
        for n, c in enumerate(roteiro, 1))
    roteiro_html = f'<details class="roteiro"><summary>{ui["script_title"]}</summary><ol>{cenas}</ol></details>' if roteiro else ""

    secs = []
    for s in P["sections"]:
        corpo = "".join(bloco(b, ui, lang, pref) for b in s["blocks"])
        secs.append(f'<section id="{s["id"]}"><div class="wrap"><span class="chip">{s["chip"]}</span>'
                    f'<h2>{s["h2"]}</h2><p class="sub">{s["sub"]}</p>{corpo}</div></section>')

    ex = ""
    if P.get("exercises"):
        exurl = ui["ex_base"] + EX_DIR[lang] + P["exercises_file"]
        itens = "".join(
            f'<li class="card"><span class="num">{e["n"]}</span><div><h3>{e["title"]} <small>· {e["time"]}</small></h3>'
            f'<p><b>{ui["ready"]}:</b> {e["ready"]}</p></div></li>' for e in P["exercises"])
        ex = (f'<section id="exercicios"><div class="wrap"><span class="chip">{ui["ex_chip"]}</span><h2>{ui["ex_h2"]}</h2>'
              f'<p class="sub">{ui["ex_sub"]}</p><ol class="exs">{itens}</ol>'
              f'<p><a class="btn ghost" href="{exurl}" target="_blank" rel="noopener">{ui["ex_open"]} →</a></p></div></section>')

    mats = "".join(f'<a class="card mat" href="{m["href"]}" target="_blank" rel="noopener"><h3>{m["label"]} →</h3><p>{m["note"]}</p></a>'
                   for m in P["materials"])
    mats += f'<a class="card mat" href="{AREA[lang]}" target="_blank" rel="noopener"><h3>{ui["area"]} →</h3><p>eventos.inema.pro</p></a>' if pid != "jornada-ia" else ""

    prev = f'<a class="pn" href="{link(ORDEM[i-1])}"><small>← {ui["prev"]}</small><b>{C["pages"][ORDEM[i-1]]["nav"]}</b></a>' if i > 0 else "<span></span>"
    nxt = f'<a class="pn dir" href="{link(ORDEM[i+1])}"><small>{ui["next"]} →</small><b>{C["pages"][ORDEM[i+1]]["nav"]}</b></a>' if i < len(ORDEM) - 1 else "<span></span>"
    chip = P["chip"] if pid == "jornada-ia" else ui["seq_of"].replace("{n}", str(i)) + " · " + P["chip"].split("·")[-1].strip()
    cta_href = P["cta_href"] if P["cta_href"].startswith("http") else link(P["cta_href"].strip("./").strip("/"))
    ext = ' target="_blank" rel="noopener"' if P["cta_href"].startswith("http") else ""

    return f"""<!DOCTYPE html>
<html lang="{ui['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(P['title'])}</title>
<meta name="description" content="{esc(P['description'])}">
<link rel="canonical" href="{url}">
{hreflang}
<meta property="og:title" content="{esc(P['title'])}">
<meta property="og:description" content="{esc(P['description'])}">
<meta property="og:image" content="{BASE}assets/{ban(pid, lang)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<a class="pular" href="#conteudo">↓</a>
<nav class="topo"><div class="wrap">
  <a class="brand" href="{link('jornada-ia')}"><span class="emoji">{ICON[pid]}</span> {ui['brand']}</a>
  <span class="sep">|</span>
  <a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a>
  <div class="links">
    <a class="sec" href="#video">{ui['nav_video']}</a>
    <a class="sec" href="#como-funciona">{ui['nav_how']}</a>
    {'<a class="sec" href="#exercicios">' + ui['nav_ex'] + '</a>' if ex else ''}
    <a class="sec" href="#materiais">{ui['nav_mat']}</a>
    <span class="lang">{langs}</span>
    <button class="tgl" id="tgl" type="button" aria-label="{ui['theme']}" title="{ui['theme']}">◐</button>
  </div>
</div></nav>
<div class="seqnav"><div class="wrap">{seqnav}</div></div>

<header class="hero" id="top"><div class="glow"></div><div class="wrap">
  <div>
    <span class="chip">{chip}</span>
    <h1>{P['h1']}</h1>
    <p class="lead">{P['lead']}</p>
    <div class="cta"><a class="btn" href="#video">{ui['watch']} ↓</a><a class="btn ghost" href="{cta_href}"{ext}>{P['cta_label']} →</a></div>
  </div>
  <figure><img src="{assets}{ban(pid, lang)}" alt="{esc(P['title'])}" width="1400" height="788"></figure>
</div></header>

<main id="conteudo">
<div class="resumo" id="resumo"><div class="wrap"><p>{P['resumo']}</p></div></div>

<section id="video"><div class="wrap">
  <span class="chip">{ui['video_chip']}</span>
  <h2>{esc(P['title'])}</h2>
  {player}
  {roteiro_html}
</div></section>

{''.join(secs)}
{ex}
<section id="materiais"><div class="wrap"><span class="chip">{ui['mat_chip']}</span><h2>{ui['mat_h2']}</h2>
<p class="sub">{ui['mat_sub']}</p><div class="grid g3">{mats}</div></div></section>

<section class="cta-final"><div class="wrap"><h2>{P['cta_title']}</h2><p>{P['cta_text']}</p>
<a class="btn" href="{cta_href}"{ext}>{P['cta_label']} →</a></div></section>

<div class="prevnext"><div class="wrap">{prev}{nxt}</div></div>
</main>
<footer><div class="wrap">{ui['footer']} · <a href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a> · <a href="https://github.com/inematds/jornada-agentes" target="_blank" rel="noopener">GitHub</a></div></footer>
{JS}
</body>
</html>
"""


def seqcards(C, lang):
    sub = "" if lang == "pt" else f"{lang}/"
    pref = "../" if lang == "pt" else "../../"
    out = []
    for n, p in enumerate(ORDEM[1:], 1):
        P = C["pages"][p]
        out.append(f'<a class="card seqcard" href="{pref}{p}/{sub}"><img src="{pref}assets/{ban(p, lang)}" alt="" loading="lazy">'
                   f'<span class="num">{n}</span><h3>{P["card_title"]}</h3><p>{P["card_text"]}</p></a>')
    return '<div class="grid g4 seqs">' + "".join(out) + "</div>"


SEQCARDS = {}

if __name__ == "__main__":
    videos = json.loads((AQUI / "videos.json").read_text(encoding="utf-8")) if (AQUI / "videos.json").exists() else {}
    roteiros = {p: json.loads((AQUI / "roteiros" / f"{p}.json").read_text(encoding="utf-8")) for p in ORDEM}
    feitos = 0
    for lang in LANGS:
        f = AQUI / "conteudo" / f"{lang}.json"
        if not f.exists():
            print(f"(sem {f.name}, pulando {lang})")
            continue
        C = json.loads(f.read_text(encoding="utf-8"))
        SEQCARDS[lang] = seqcards(C, lang)
        for pid in ORDEM:
            # o vídeo é em português: o roteiro aparece só na página PT
            html_ = pagina(pid, lang, C, roteiros[pid] if lang == "pt" else [], videos)
            d = AQUI / pid / ("" if lang == "pt" else lang)
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(links_lang(html_, lang), encoding="utf-8")
            feitos += 1
    print(f"{feitos} páginas geradas")
