import gevent
import time
import os
import binascii
import qrcode
from qrcode.image.pure import PymagingImage


def generate_qr_codes(end_event, account):

    while not end_event.is_set():
        signed_bytes = account.create_qr_sign(int(time.time()))
        signed_bytes = bytearray.fromhex('03') + signed_bytes

        img = qrcode.make(
            b'0x' + binascii.hexlify(signed_bytes),
            image_factory=PymagingImage
        )
        rootpath = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(rootpath, 'ui', 'static', 'qrcode.png'), 'wb') as f:
            img.save(f)

        gevent.sleep(10)
