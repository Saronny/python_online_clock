from PIL import Image, ImageDraw

def create_favicon():
    icon = Image.new('RGBA', (16, 16), (255, 0, 0, 0))
    draw = ImageDraw.Draw(icon)
    draw.rectangle([0, 0, 15, 15], fill=(255, 0, 0, 255), outline=(0, 0, 0, 255))
    icon.save("static/favicon.ico")
