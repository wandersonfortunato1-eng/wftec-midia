"""Stories de um carrossel: um Story por slide (pedido do Wanderson, 06/11/2026).
Uso: python3 kit/story.py AAAA-MM/AAAA-MM-DD-tema   -> gera AAAA-MM-DD-tema-story-1.jpg ... -story-N.jpg (1080x1920)
Cada slide 1080x1350 vai centralizado (y=285) sobre o fundo da marca, com a contagem "2 / 6" embaixo."""
import sys, glob, re
from PIL import Image, ImageDraw, ImageFont
pref = sys.argv[1]
slides = sorted(glob.glob(pref + "-[0-9]*.jpg"), key=lambda f: int(re.findall(r"-(\d+)\.jpg$", f)[0]))
slides = [f for f in slides if "-story" not in f]
n = len(slides)
try: fonte = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
except Exception: fonte = ImageFont.load_default()
for i, f in enumerate(slides, 1):
    bg = Image.new("RGB", (1080, 1920), "#F6F2EF")
    bg.paste(Image.open(f).convert("RGB").resize((1080, 1350)), (0, 285))
    d = ImageDraw.Draw(bg); t = f"{i} / {n}"
    w = d.textlength(t, font=fonte); d.rounded_rectangle(((1080 - w) / 2 - 28, 1700, (1080 + w) / 2 + 28, 1764), 32, fill="#F15A25")
    d.text(((1080 - w) / 2, 1712), t, font=fonte, fill="white")
    out = f"{pref}-story-{i}.jpg"; bg.save(out, quality=90); print(out)
