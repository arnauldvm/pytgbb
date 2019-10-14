from abc import ABC, abstractmethod
from random import Random


class Randomizer(ABC):

    def __init__(self):
        self.random = Random()
        self.random.seed()

    def seed(self, *args, **kwargs):
        self.random.seed(*args, **kwargs)

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def draws(self, count):
        pass

    @abstractmethod
    def __len__(self):
        pass
