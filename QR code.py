import pyqrcode
import png
from pyqrcode import QRCode
s=input("Enter a url: " )
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
url.png("myqr",scale=6)


