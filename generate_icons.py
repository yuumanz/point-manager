from PIL import Image, ImageDraw, ImageFont

BG = (28, 28, 26, 255)       # --text (dark)
FG = (245, 244, 240, 255)    # --bg (light text on dark)
ACCENT = (226, 75, 74, 255)  # --danger-border (alert dot)

FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

def make_icon(size, out_path, corner_ratio=0.22):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    radius = int(size * corner_ratio)
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=BG)

    font_size = int(size * 0.44)
    font = ImageFont.truetype(FONT_PATH, font_size)
    text = "pt"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1] - size * 0.03), text, font=font, fill=FG)

    dot_r = size * 0.07
    cx, cy = size * 0.775, size * 0.225
    draw.ellipse([cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r], fill=ACCENT)

    img.save(out_path)

make_icon(512, "icon-512.png")
make_icon(192, "icon-192.png")
make_icon(180, "apple-touch-icon.png", corner_ratio=0.0)
