from PIL import Image

img = Image.open("static/images/logo.png")
img.save("static/images/logo.ico")
