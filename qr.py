import qrcode

image = qrcode.make("https://localhost:8000")
image.save("qr.png")
