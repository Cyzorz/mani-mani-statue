import qrcode
from path import Path
import io
from pyqrcode import QRCode
class qrGen:
    def create():
        img = qrcode.make('http://pogchampion.atwebpages.com/')
        img.save(Path.get('assets/qrcode_test.png'))