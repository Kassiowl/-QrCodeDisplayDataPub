

from ..Repo.PersonRepo import PersonInfoInterface
from ..entities.Person import Person
from ..entities.Github import Github
from ..entities.Linkedin import Linkedin


class PersonInfo(PersonInfoInterface):

    def __init__ (self, person: Person):
        self.person = person

    def get_person_info(self) -> dict:
        return {
                "Name": self.person.name, "Surname":self.person.surname,
                "lastname": self.person.lastName, "age": self.person.age, 
                "about_me" : self.person.aboutMe, "github_url": self.person.github.url,
                "linkedin_url": self.person.linkedin.url
               }


