from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def make_thumbnail(headline, output_file="output/thumbnail.jpg"):
    bg = Image.open("assets/studio.jpg").convert("RGB")
    bg = bg.resize((1280, 720))

    draw = ImageDraw.Draw(bg)

    font_big = ImageFont.load_default()
    font_small = ImageFont.load_default()

    title = "TODAY'S NEWS SONG!"
    date_text = datetime.now().strftime("%b %d, %Y")

    draw.rectangle([0, 0, 1280, 140], fill=(0, 0, 0))
    draw.text((40, 40), title, font=font_big, fill=(255, 255, 255))

    draw.text((40, 160), "YoYo Beka News", font=font_small, fill=(255, 255, 255))
    draw.text((40, 200), date_text, font=font_small, fill=(255, 255, 255))

    draw.rectangle([40, 520, 1240, 680], fill=(0, 0, 0))
    draw.text((60, 560), headline[:70], font=font_small, fill=(255, 255, 0))

    bg.save(output_file)
