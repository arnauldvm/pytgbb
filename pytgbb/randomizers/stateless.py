from typing import Generic, Union, Sequence, List

from .randomizer import Randomizer, T


class StatelessRandomizer(Randomizer, Generic[T]):
    """
    A Randomizer that has no memory.

    The likelihood of a result value at a given time is independent from the result values that were drawn in the past.

    Examples: a die, a fistful of dice, a spinner/Wheel
    """

    def __init__(self, values: Union[int, Sequence[T]]):
        """Initializes a StatelessRandomizer. Accepts either a sequence of values, or an int.
        In the latter case, the possible value are 0 ... n-1."""
        self.values: Union[Sequence[int], Sequence[T]]
        if isinstance(values, int):
            self.values = range(values)
        elif isinstance(values, Sequence):
            self.values = values
        else:
            raise TypeError("StatelessRandomizer constructor expects an int or a Sequence, got {}".format(type(values)))
        super(StatelessRandomizer, self).__init__()

    def draw(self) -> T:
        """
        Generates **one** random result.

        This should not be overriden by the subclasses.
        """
        return self.random.choice(self.values)

    def draws(self, count: int) -> List[T]:
        """
        Generates *count* random results.

        This should not be overriden by the subclasses.
        """
        return [self.draw() for _ in range(count)]

    def __len__(self) -> int:
        """
        Returns the count of possible result values.

        This should not be overriden by the subclasses.
        """
        return len(self.values)


class Die(StatelessRandomizer, Generic[T]):
    """This class emulates rolling a die."""

    def __init__(self, sides: Union[int, Sequence]):
        """Initializes a Die. Accepts either a sequence of values, or an int.
        In the latter case, the possible value are 1 ... n."""
        if isinstance(sides, int):
            sides = range(1, sides+1)
        super(Die, self).__init__(sides)


class Spinner(StatelessRandomizer):
    """This class emulates spinning the arrow of a wheel. Alias: Wheel"""

    def __init__(self, sectors: Union[int, Sequence]):
        """Initializes a Spinner. Accepts either a sequence of values, or an int.
        In the latter case, the possible value are 1 ... n."""
        if isinstance(sectors, int):
            sectors = range(1, sectors+1)
        super(Spinner, self).__init__(sectors)

    spin = StatelessRandomizer.draw

    spins = StatelessRandomizer.draws


Wheel = Spinner
