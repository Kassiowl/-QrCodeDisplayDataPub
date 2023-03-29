from abc import ABC, abstractmethod

from ..entities.Person import Person
from ..entities.Github import Github
from ..entities.Linkedin import Linkedin


class PersonInfoInterface(ABC):
    @abstractmethod
    def get_person_info() -> Person:
        pass