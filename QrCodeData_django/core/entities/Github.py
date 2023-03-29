from dataclasses import dataclass


@dataclass
class Github:
    url: str
    username: str
    contribuitions: int