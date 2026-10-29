"""Renderiza cada <section class="slide"> de um HTML em PNG 1080x1350.
Uso: python3 kit/render.py caminho/post.html saida_prefixo
O HTML deve linkar ../kit/base.css (ou caminho relativo correto) e pode usar
<span class="logo"></span> que vira o símbolo da WFtec. Gera saida_prefixo-1.png, -2.png..."""
import sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve(); out = sys.argv[2]
KIT = pathlib.Path(__file__).resolve().parent
logo = (KIT/"wftec-simbolo.svg").read_text()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(src.as_uri()); pg.evaluate("""(l)=>{document.querySelectorAll('.logo').forEach(e=>e.innerHTML=l);
      const W=['FGTS','INSS','CCT','ACT','eSocial','piso','13º','férias','DSR','IRRF'];let s='';for(let r=0;r<50;r++){let t='';for(let c=0;c<8;c++)t+=(((r*7+c*13)%5===0)?W[(r+c)%W.length]:String((r*9301+c*49297)%99999).padStart(5,'0'))+'   ';s+=t+'\\n'}
      document.querySelectorAll('.bg').forEach(e=>e.textContent=s)}""", logo)
    pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(600)
    sl = pg.query_selector_all("section.slide")
    for i, s in enumerate(sl, 1):
        s.screenshot(path=f"{out}-{i}.png"); print(f"{out}-{i}.png")
    b.close()
