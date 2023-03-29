from abc import ABC, abstractmethod



class QrCodeGenInterface(ABC):
    @abstractmethod
    def gen() -> str:
        pass
    def get_url():
        pass