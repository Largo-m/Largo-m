"""Render the profile banner (assets/banner.png) without any external assets.

The banner is generated from code so it stays reproducible: run

    python tools/make_banner.py

and commit the refreshed PNG. Only fonts shipped with Windows are used.
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

WIDTH, HEIGHT = 1280, 360
BACKGROUND_TOP = (10, 14, 22)
BACKGROUND_BOTTOM = (17, 24, 39)
ACCENT = (56, 189, 248)
ACCENT_SOFT = (99, 230, 165)
MUTED = (148, 163, 184)
TEXT = (241, 245, 249)

FONT_DIR = Path("C:/Windows/Fonts")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    """Load a Windows font, falling back to the Pillow default."""
    path = FONT_DIR / name
    if path.is_file():
        return ImageFont.truetype(str(path), size)
    return ImageFont.load_default(size)


def gradient(size: tuple[int, int]) -> Image.Image:
    """Return a vertical gradient image."""
    width, height = size
    image = Image.new("RGB", size)
    pixels = image.load()
    for y in range(height):
        blend = y / max(height - 1, 1)
        red = int(BACKGROUND_TOP[0] + (BACKGROUND_BOTTOM[0] - BACKGROUND_TOP[0]) * blend)
        green = int(BACKGROUND_TOP[1] + (BACKGROUND_BOTTOM[1] - BACKGROUND_TOP[1]) * blend)
        blue = int(BACKGROUND_TOP[2] + (BACKGROUND_BOTTOM[2] - BACKGROUND_TOP[2]) * blend)
        for x in range(width):
            pixels[x, y] = (red, green, blue)
    return image


def glow(image: Image.Image, center: tuple[int, int], radius: int, color: tuple[int, int, int]) -> None:
    """Blur a soft circle into the image."""
    layer = Image.new("RGB", image.size, (0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.ellipse(
        (center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius),
        fill=color,
    )
    layer = layer.filter(ImageFilter.GaussianBlur(radius / 2))
    image.paste(Image.blend(image, Image.blend(image, layer, 0.55), 0.75), (0, 0))


def grid(draw: ImageDraw.ImageDraw) -> None:
    """Draw a faint technical grid."""
    for x in range(0, WIDTH, 40):
        draw.line([(x, 0), (x, HEIGHT)], fill=(30, 41, 59), width=1)
    for y in range(0, HEIGHT, 40):
        draw.line([(0, y), (WIDTH, y)], fill=(30, 41, 59), width=1)


def orbit(draw: ImageDraw.ImageDraw) -> None:
    """Draw the shield-and-orbit motif on the right side."""
    center = (1080, 180)
    for index, radius in enumerate((128, 168, 208)):
        alpha = 255 - index * 60
        color = (ACCENT[0] * alpha // 255, ACCENT[1] * alpha // 255, ACCENT[2] * alpha // 255)
        draw.ellipse(
            (center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius),
            outline=color,
            width=2,
        )
    points = []
    for step in range(0, 360, 6):
        angle = math.radians(step)
        points.append((center[0] + 168 * math.cos(angle), center[1] + 168 * math.sin(angle) * 0.42))
    draw.line(points, fill=ACCENT_SOFT, width=3, joint="curve")
    draw.ellipse(
        (center[0] - 46, center[1] - 52, center[0] + 46, center[1] + 52), fill=(15, 23, 42), outline=ACCENT, width=3
    )
    draw.polygon(
        [
            (center[0], center[1] - 34),
            (center[0] + 30, center[1] - 18),
            (center[0] + 30, center[1] + 10),
            (center[0], center[1] + 36),
            (center[0] - 30, center[1] + 10),
            (center[0] - 30, center[1] - 18),
        ],
        outline=ACCENT_SOFT,
        width=3,
    )


def main() -> None:
    image = gradient((WIDTH, HEIGHT))
    grid(ImageDraw.Draw(image))
    glow(image, (1120, 120), 220, (13, 60, 92))
    glow(image, (120, 320), 180, (10, 70, 60))

    draw = ImageDraw.Draw(image)
    orbit(draw)

    draw.text((72, 78), "LARGO-M", font=font("seguisb.ttf", 64), fill=TEXT)
    draw.line([(74, 168), (474, 168)], fill=ACCENT, width=4)
    draw.text(
        (72, 190),
        "Security and privacy tooling",
        font=font("seguisb.ttf", 30),
        fill=TEXT,
    )
    draw.text(
        (72, 230),
        "with honest interfaces",
        font=font("seguisb.ttf", 30),
        fill=ACCENT_SOFT,
    )
    draw.text(
        (72, 290),
        "Python  ·  Qt / PySide6  ·  Windows internals  ·  networking",
        font=font("segoeui.ttf", 20),
        fill=MUTED,
    )

    target = Path(__file__).resolve().parents[1] / "assets" / "banner.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target, optimize=True)
    print(f"wrote {target} ({target.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
