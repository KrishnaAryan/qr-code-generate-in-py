import qrcode as qr
from PIL import Image

qrcode=qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=4,)
qrcode.add_data("hi Krishna")
qrcode.make(fit=True)
img=qrcode.make_image(fill_color="red", back_color="blue")
img.save("adv-qrcode.png")
