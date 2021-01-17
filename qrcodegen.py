import qrcode
import io
from pyqrcode import QRCode
class qrGen:
    def create():
        img = qrcode.make('https://questybot.xyz/')
        img.save('qrcode_test.png')