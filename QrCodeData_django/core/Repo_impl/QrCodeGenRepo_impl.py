from ..Repo.QrCodeGenRepo import QrCodeGenInterface
from ..entities.Person import Person

import qrcode

class QrCodeGenRepoImpl(QrCodeGenInterface):

    def __init__(self, data):
        self.data = data

    def gen(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        qr_code = qr.make_image(fill_color="black", back_color="white")

        return qr_code
    def get_url(self) -> str:
        return (f'url/${self.person}')