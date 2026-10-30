"""Gera public/icon.png (ícone do canal RSS). Uso: python3 scripts/make_icon.py"""
from pathlib import Path

from PIL import Image, ImageDraw

SIZE = 512
BACKGROUND = (31, 42, 55)
RING = (94, 234, 212)
OUTPUT = Path(__file__).resolve().parents[1] / "public" / "icon.png"


def main() -> None:
    scale = 4
    canvas = Image.new("RGB", (SIZE * scale, SIZE * scale), BACKGROUND)
    draw = ImageDraw.Draw(canvas)
    center = SIZE * scale // 2
    for radius in (210, 140, 70):
        r = radius * scale
        draw.ellipse((center - r, center - r, center + r, center + r), outline=RING, width=10 * scale // 2)
    draw.line((center, center, center + 150 * scale, center - 150 * scale), fill=RING, width=12 * scale // 2)
    blip = 24 * scale
    bx, by = center + 105 * scale, center - 60 * scale
    draw.ellipse((bx - blip, by - blip, bx + blip, by + blip), fill=RING)
    canvas.resize((SIZE, SIZE), Image.LANCZOS).save(OUTPUT, optimize=True)


if __name__ == "__main__":
    main()
