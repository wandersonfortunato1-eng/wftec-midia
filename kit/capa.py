"""Capa de Reels da WFtec (1080x1920), pensada para o recorte da grade do perfil (3:4, faixa central y=240..1680).
Uso: python3 kit/capa.py saida.jpg "KICKER" "Título com <em>destaque</em>?" "Subtítulo curto" [tema]
tema: claro (padrão) ou escuro. Regras: pergunta curta (até ~7 palavras), destaque laranja, sem legenda de vídeo."""
import sys, pathlib
from playwright.sync_api import sync_playwright
KIT = pathlib.Path(__file__).resolve().parent
out, kicker, titulo, sub = sys.argv[1:5]; escuro = len(sys.argv) > 5 and sys.argv[5] == "escuro"
logo = (KIT/"wftec-simbolo.svg").read_text().replace("<svg ", '<svg style="width:120px;height:120px" ', 1)
html = f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{(KIT/'base.css').as_uri()}">
<style>body{{margin:0}}#c{{position:relative;width:1080px;height:1920px;overflow:hidden;background:{'#141312' if escuro else 'var(--paper)'};color:{'#F1ECE8' if escuro else 'var(--ink)'}}}
#in{{position:absolute;left:80px;right:80px;top:330px;height:1260px;display:flex;flex-direction:column;justify-content:center}}
.lg{{display:flex;align-items:center;gap:22px;font:italic 900 64px Archivo}}.lg b{{color:var(--ac)}}
.kk{{font:600 34px Mono;letter-spacing:4px;color:{'#FF8A5C' if escuro else 'var(--act)'};margin-top:90px}}
h1{{font:italic 900 150px/0.98 Archivo;letter-spacing:-3px;margin-top:26px}}
.sb{{font:500 46px/1.3 Plex;color:{'#A89F99' if escuro else 'var(--muted)'};margin-top:44px}}
.bar{{width:180px;height:16px;border-radius:8px;background:var(--ac);margin-top:60px}}</style></head><body>
<div id="c"><div class="bg"></div><div id="in"><div class="lg">{logo}<span>WF<b>tec</b></span></div>
<div class="kk">{kicker}</div><h1>{titulo}</h1><div class="sb">{sub}</div><div class="bar"></div></div></div></body></html>"""
tmp = KIT/"_capa.html"; tmp.write_text(html, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1920}); pg.goto(tmp.as_uri())
    pg.evaluate("""()=>{const W=['CLT','FGTS','INSS','CCT','ACT','piso','folha','ponto','verba','13º'];let s='';for(let r=0;r<60;r++){let t='';for(let c=0;c<8;c++)t+=(((r*7+c*13)%5===0)?W[(r+c)%W.length]:String((r*9301+c*49297)%99999).padStart(5,'0'))+'   ';s+=t+'\\n'}document.querySelector('.bg').textContent=s}""")
    pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500); pg.screenshot(path="/tmp/_capa.png"); b.close()
from PIL import Image; Image.open("/tmp/_capa.png").convert("RGB").save(out, quality=92); tmp.unlink(); print(out)
