from ..entities.Person import Person
from ..Repo.PersonRepo import PersonInfoInterface

class GetPersonInfo:
    
    def __init__(self,person_repo: PersonInfoInterface):
        self.repo = person_repo

    def run(self):
        return self.repo.get_person_info()


