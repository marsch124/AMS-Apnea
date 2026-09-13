#!/usr/bin/env python3
"""AMS Apnea app icons: flat calm blue, one hand-drawn white glyph —
a held breath: a big bubble with two small ones rising. No glow, no gradient."""
import math, os, random
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(__file__), "..", "icons")
BG = (28, 72, 110)
INK = (246, 249, 252)
random.seed(7)

def wobbly_circle(d, cx, cy, r, w, S):
    pts, n = [], 160
    ph = random.random() * 6.28
    start = random.uniform(-0.3, 0.3)
    for i in range(n + 6):                      # overshoots a little: a drawn loop that doesn't quite close
        a = start + i / n * 2 * math.pi
        rr = r * (1 + 0.018 * math.sin(3 * a + ph) + 0.012 * math.sin(5 * a + ph * 2))
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a) + i * 0.02 * S / 1024))
    stamp(d, pts, w)

def stamp(d, pts, w):
    """Stamped round dabs along the path — clean edges, no joint spikes."""
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        steps = max(1, int(math.hypot(x1 - x0, y1 - y0) / 3))
        for j in range(steps):
            x, y = x0 + (x1 - x0) * j / steps, y0 + (y1 - y0) * j / steps
            d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=INK)
    x, y = pts[-1]; d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=INK)

def render(size, maskable=False):
    S = 1024 * 2
    im = Image.new("RGB", (S, S), BG)
    d = ImageDraw.Draw(im)
    k = 0.78 if maskable else 1.0
    c = S / 2
    def P(x, y): return (c + (x - 512) * 2 * k, c + (y - 512) * 2 * k)
    w = 46 * 2 * k
    x, y = P(460, 590); wobbly_circle(d, x, y, 225 * 2 * k, w, S)
    x, y = P(690, 300); wobbly_circle(d, x, y, 78 * 2 * k, w * 0.85, S)
    x, y = P(790, 175); wobbly_circle(d, x, y, 38 * 2 * k, w * 0.7, S)
    # a small highlight stroke inside the big bubble
    hx, hy = P(460, 590); r = 150 * 2 * k
    arc = [(hx + r * math.cos(a), hy + r * math.sin(a)) for a in [math.radians(t) for t in range(200, 252, 3)]]
    stamp(d, arc, w * 0.7)
    return im.resize((size, size), Image.LANCZOS)

os.makedirs(OUT, exist_ok=True)
render(180).save(os.path.join(OUT, "icon-180.png"))
render(192).save(os.path.join(OUT, "icon-192.png"))
render(512).save(os.path.join(OUT, "icon-512.png"))
render(512, True).save(os.path.join(OUT, "icon-512-maskable.png"))
print("icons written")
