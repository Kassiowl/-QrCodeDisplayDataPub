from dataclasses import dataclass
from .Github import Github
from .Linkedin import Linkedin

@dataclass
class Person:
    name: str
    surname: str
    lastName: str
    aboutMe: str
    age: int
    github: Github
    linkedin: Linkedin

