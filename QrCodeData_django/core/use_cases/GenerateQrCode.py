from ..Repo.QrCodeGenRepo import QrCodeGenInterface

class GenerateQrCodeUseCase:
    
    def __init__(self,person_repo: QrCodeGenInterface):
        self.repo = person_repo

    def run(self):
        return self.repo.gen()


