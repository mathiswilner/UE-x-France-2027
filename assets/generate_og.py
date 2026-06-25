from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGB", (1200, 630), "#000091")
draw = ImageDraw.Draw(img)

# Barre rouge en bas
draw.rectangle([(0, 620), (1200, 630)], fill="#E1000F")

font_big = ImageFont.load_default(size=72)
font_med = ImageFont.load_default(size=32)
font_small = ImageFont.load_default(size=24)

# Titre
draw.text((60, 50), "LE PRIX DU", fill="#FFFFFF", font=font_med)
draw.text((60, 90), "FREXIT", fill="#E1000F", font=font_big)

# 10 milliards en gris discret
draw.text((60, 210), "10 milliards.", fill="#666699", font=font_med)
draw.text((60, 250), "C'est ce que la France verse a l'UE.", fill="#666699", font=font_small)

# 151 milliards en blanc bien visible
draw.text((60, 320), "151 milliards.", fill="#FFFFFF", font=font_big)
draw.text((60, 400), "C'est ce que l'UE rapporte a la France.", fill="#CCCCCC", font=font_small)

# Punchline
draw.text((60, 500), "Pour 1 euro verse, 15 euros de retour, directs et indirects.", fill="#FFFFFF", font=font_med)

img.save("assets/og-image.png")
print("Image sauvegardee")