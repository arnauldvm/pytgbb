from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from random import Random

T = TypeVar('T')


class Randomizer(ABC, Generic[T]):

    def __init__(self):
        self.random = Random()
        self.random.seed()

    def seed(self, *args, **kwargs):
        self.random.seed(*args, **kwargs)

    @abstractmethod
    def draw(self) -> T:
        pass

    @abstractmethod
    def draws(self, count: int) -> List[T]:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass
