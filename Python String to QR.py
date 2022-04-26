import pyqrcode

def qr_code():
    s='Your String here'
    d=pyqrcode.create(s)
    d.png('filename.png',scale=6)
    print("Done")

if __name__ == '__main__':
    qr_code()
