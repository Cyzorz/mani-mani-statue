import qrcode
import io
from pyqrcode import QRCode
class qrGen:
    def create():
        img = qrcode.make('http://pogchampion.atwebpages.com/')
        img.save('assets/qrcode_test.png')