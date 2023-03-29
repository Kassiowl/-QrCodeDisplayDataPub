from ..QrCodeData_django.core.Repo_impl.QrCodeGenRepo_impl import QrCodeGenRepoImpl
from ..QrCodeData_django.core.entities.Github import Github
from ..QrCodeData_django.core.entities.Linkedin import Linkedin
from ..QrCodeData_django.core.entities.Person import Person

import qrcode

def test_qr_code_gen():
    
    person_user = 'jkkoe'
    github = Github('url', person_user, 22)
    linkedin = Linkedin('url', person_user)


    person = Person('john', 'kled', 'wallace', 'Lorem', 22, github, linkedin)

    qrcode_person = QrCodeGenRepoImpl(person)

    assert(isinstance(qrcode_person.gen(), qrcode.image.pil.PilImage))
