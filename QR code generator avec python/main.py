# pip install pyqrcode
# pip install pypng
# pip install pyzbar
# pip install pillow

import pyqrcode

from pyzbar.pyzbar import decode

# pillow permet de manipuler les images
from PIL import Image

qr = pyqrcode.create("coding with AZIZ")
qr.png("myCode.png", scale=8)

d = decode(Image.open("myCode.png"))

print(d[0].data.decode("ascii"))
