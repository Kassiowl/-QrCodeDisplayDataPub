from ..QrCodeData_django.core.Repo_impl.PersonRepo_impl import PersonInfo

from ..QrCodeData_django.core.entities.Person import Person
from ..QrCodeData_django.core.entities.Github import Github
from ..QrCodeData_django.core.entities.Linkedin import Linkedin


def test_PersonInfo():


    person_user = 'jkkoe'
    github = Github('url', person_user, 22)
    linkedin = Linkedin('url', person_user)


    person_entity = Person('john', 'kled', 'wallace', 'lorem ipsum', 22, github, linkedin)

    person_test = PersonInfo(person_entity)
   
    assert(person_test.get_person_info() ==
            {
                'Name': person_entity.name, 'Surname': person_entity.surname, 'lastname': person_entity.lastName, 
                'about_me': person_entity.aboutMe,
                'age': person_entity.age,
                'github_url': person_entity.github.url, 
                'linkedin_url': person_entity.linkedin.url
            }
            )