from pyzbar.pyzbar import decode

from PIL import Image


img = Image.open('D:/pic/myqrcode.png')

result = decode(img)

print(result)
