import pyqrcode
import png
from pyqrcode import QRCode

s = "https://youtu.be/hTpfiw1i94I?si=oB4kn41zj1p0-Wbj"

url = pyqrcode.create(s)

url.svg("Song.svg",scale= 8)

url.png("Song.png",scale=6)
