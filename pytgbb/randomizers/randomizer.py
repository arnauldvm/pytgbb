from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from random import Random

T = TypeVar('T')


class Randomizer(ABC, Generic[T]):
    """
    A Randomizer is a component that generate results randomly.

    The results can be any type such as: an int, a color, a Card...
    """

    def __init__(self):
        """The constructor of th abstract class akes care of initializing the random generator."""
        self.random = Random()
        self.random.seed()

    def seed(self, *args, **kwargs):
        """Resets the random generator. Takes the same arguments as the `Random.seed(...)` method"""
        self.random.seed(*args, **kwargs)

    @abstractmethod
    def draw(self) -> T:
        """
        Generates **one** random result.

        This must be implemented by the subclasses.
        """
        pass

    def draws(self, count: int) -> List[T]:
        """
        Generates *count* random results.

        This should not be overriden by the subclasses.
        """
        return [self.draw() for _ in range(count)]

    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the count of possible result values.

        This must be implemented by the subclasses.
        """
        pass
