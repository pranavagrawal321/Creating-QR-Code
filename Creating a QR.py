import pyqrcode


def qr_code():
    s = "Text"
    d = pyqrcode.create(s)
    d.png('qr_code.png', scale=6)


qr_code()
