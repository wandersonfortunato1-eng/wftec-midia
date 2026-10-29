"""Monta um Reels da WFtec (1080x1920, 30 fps) com a voz do Antonio, legendas e trilha.

Uso (rode da raiz do repositório):
  python3 kit/video/build.py PASTA --analisar          # corta silêncio das falas e mostra durações e pausas (para os cues)
  python3 kit/video/build.py PASTA --preview 1,5,12    # gera quadros PNG em PASTA/_frames para conferir com Read
  python3 kit/video/build.py PASTA                     # gera PASTA/video.mp4 e PASTA/capa.jpg

PASTA contém:
  video.html  composição com window.render(t) determinística (modelo: kit/video/ref/novas/novas.html).
              Use /*BASE*/ dentro do <style> (vira kit/video/base.css), __LOGO__ e __TIMELINE__.
  video.json  {"voz": "voz/AAAA-MM-DD-tema", "min": {"1": 5.2, "6": 6.4}, "dest": ["palavra-chave", ...],
               "cues": {"nome": segundos_desde_o_inicio_da_fala, ...}, "capa": 12.5}
  A pasta "voz" (relativa à raiz) deve ter fala1.mp3..falaN.mp3 (gerados pela Action "Voz do Antonio").
Cada fala = uma cena (segmento). Duração da cena = max(0.25 + fala + 0.35, min[i]) (+1 s na última).
"""
import json, re, subprocess, sys, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parents[2]; KIT = ROOT/"kit"
P = pathlib.Path(sys.argv[1]).resolve(); CFG = json.loads((P/"video.json").read_text(encoding="utf-8"))
VOZ = ROOT/CFG["voz"]; TMP = P/"_voz"; TMP.mkdir(exist_ok=True)
FPS, INI, VW, VH = 30, .25, 1080, 1920
def run(*a): return subprocess.run(a, check=True, capture_output=True, text=True)
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",str(p)]).decode())
falas = sorted(VOZ.glob("fala*.mp3"), key=lambda p: int(re.findall(r"\d+", p.stem)[0])); N = len(falas)
if not N: raise SystemExit(f"sem falas em {VOZ}")
textos = [l.strip() for l in (VOZ/"falas.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
d = {}
for i, f in enumerate(falas, 1):
    w = TMP/f"fala{i}.wav"
    run("ffmpeg","-y","-v","error","-i",str(f),"-af","areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse",str(w))
    d[i] = dur(w)
if "--analisar" in sys.argv:
    for i in range(1, N+1):
        r = subprocess.run(["ffmpeg","-i",str(TMP/f"fala{i}.wav"),"-af","silencedetect=n=-40dB:d=0.12","-f","null","-"], capture_output=True, text=True).stderr
        print(f"fala{i} {d[i]:.2f}s  pausas terminam em: {re.findall(r'silence_end: ([0-9.]+)', r)}\n   {textos[i-1]}")
    sys.exit(0)
MIN = {int(k): v for k, v in CFG.get("min", {}).items()}
segs, t = [], 0.0
for i in range(1, N+1):
    L = max(INI + d[i] + .35, MIN.get(i, 0)) + (1.0 if i == N else 0)
    segs.append({"ini": round(t,3), "fim": round(t+L,3)}); t += L
TOTAL = t
if TOTAL > 60: raise SystemExit(f"vídeo com {TOTAL:.1f}s: passa de 60 s, encurte as falas")
def blocos(txt):
    out, cur = [], ""
    for p in re.split(r"(?<=[.?!,:])\s+", txt.strip()):
        if cur and len(cur)+1+len(p) > 72: out.append(cur); cur = p
        else: cur = (cur+" "+p).strip()
    if cur: out.append(cur)
    return out
leg = []
for i in range(1, N+1):
    bl = blocos(textos[i-1]); tot = sum(map(len, bl)); t0 = segs[i-1]["ini"]+INI
    for b in bl:
        dd = d[i]*len(b)/tot; h = b
        for k in CFG.get("dest", []): h = re.sub(re.escape(k), lambda m: f"<em>{m.group(0)}</em>", h, flags=re.I)
        leg.append({"ini": round(t0-.05,3), "fim": round(t0+dd+.1,3), "html": h}); t0 += dd
base = (KIT/"video"/"base.css").read_text().replace("url(../fonts/", f"url({(KIT/'fonts').as_uri()}/")
logo = (KIT/"wftec-simbolo.svg").read_text().strip()
html = (P/"video.html").read_text(encoding="utf-8").replace("/*BASE*/", base, 1)
html = html.replace("__LOGO__", logo).replace("__TIMELINE__", json.dumps({"seg": segs, "legendas": leg, "ini": INI, "cue": CFG.get("cues", {})}, ensure_ascii=False))
(P/"_b.html").write_text(html, encoding="utf-8")
print(f"duração {TOTAL:.1f}s", [round(s["fim"]-s["ini"],1) for s in segs])
fr = P/"_frames"; fr.mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(args=["--allow-file-access-from-files"]); pg = b.new_page(viewport={"width":VW,"height":VH})
    pg.goto((P/"_b.html").as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1200)
    if "--preview" in sys.argv:
        for tt in [float(x) for x in sys.argv[sys.argv.index("--preview")+1].split(",")]:
            pg.evaluate(f"render({tt})"); pg.wait_for_timeout(40); pg.screenshot(path=str(fr/f"p_{tt:06.2f}.png")); print(fr/f"p_{tt:06.2f}.png")
        b.close(); sys.exit(0)
    enc = subprocess.Popen(["ffmpeg","-y","-v","error","-f","image2pipe","-framerate",str(FPS),"-i","-","-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p",str(P/"_mudo.mp4")], stdin=subprocess.PIPE)
    n = int(TOTAL*FPS)
    for f in range(n):
        pg.evaluate(f"render({f/FPS})"); enc.stdin.write(pg.screenshot(type="png"))
        if f % 300 == 0: print(f"quadro {f}/{n}", flush=True)
    enc.stdin.close(); enc.wait()
    ct = float(CFG.get("capa", segs[1]["ini"] + 2.5 if N > 1 else 2)); pg.evaluate(f"render({ct})"); pg.screenshot(path=str(P/"_capa.png")); b.close()
ins, fil = [], []
for k in range(N):
    ins += ["-i", str(TMP/f"fala{k+1}.wav")]; ms = int((segs[k]["ini"]+INI)*1000)
    fil.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,adelay={ms}|{ms}[a{k}]")
ins += ["-i", str(KIT/"trilha.wav")]
fil.append("".join(f"[a{k}]" for k in range(N)) + f"amix=inputs={N}:normalize=0,highpass=f=70,acompressor=threshold=-20dB:ratio=3:attack=5:release=120,loudnorm=I=-15:TP=-2:LRA=7,apad=whole_dur={TOTAL},asplit=2[voz][sc]")
fil.append(f"[{N}:a]atrim=0:{TOTAL},asetpts=N/SR/TB,aresample=48000,highpass=f=60,volume=-13dB,afade=t=out:st={TOTAL-2.2}:d=2.2[m0]")
fil.append("[sc]aformat=channel_layouts=stereo[sc2];[m0][sc2]sidechaincompress=threshold=0.03:ratio=6:attack=30:release=450[mus]")
fil.append("[voz]aformat=channel_layouts=stereo[v2];[v2][mus]amix=inputs=2:normalize=0,alimiter=limit=0.84[mx]")
run("ffmpeg","-y","-v","error",*ins,"-filter_complex",";".join(fil),"-map","[mx]","-ac","2","-ar","48000","-c:a","aac","-b:a","192k","-t",f"{TOTAL}",str(P/"_audio.m4a"))
run("ffmpeg","-y","-v","error","-i",str(P/"_mudo.mp4"),"-i",str(P/"_audio.m4a"),"-c","copy","-shortest","-movflags","+faststart",str(P/"video.mp4"))
run("ffmpeg","-y","-v","error","-i",str(P/"_capa.png"),"-q:v","2",str(P/"capa.jpg"))
print("ok", P/"video.mp4", f"{TOTAL:.1f}s")
