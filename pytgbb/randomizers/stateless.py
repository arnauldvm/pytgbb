from typing import Generic, Union, Sequence, List

from .randomizer import Randomizer, T


class StatelessRandomizer(Randomizer, Generic[T]):

    def __init__(self, values: Union[int, Sequence[T]]):
        self.values: Union[Sequence[int], Sequence[T]]
        if isinstance(values, int):
            self.values = range(values)
        elif isinstance(values, Sequence):
            self.values = values
        else:
            raise TypeError("StatelessRandomizer constructor expects an int or a Sequence, got {}".format(type(values)))
        super(StatelessRandomizer, self).__init__()

    def draw(self) -> T:
        return self.random.choice(self.values)

    def draws(self, count: int) -> List[T]:
        return [self.draw() for _ in range(count)]

    def __len__(self) -> int:
        return len(self.values)


class Die(StatelessRandomizer, Generic[T]):

    def __init__(self, sides: Union[int, Sequence]):
        if isinstance(sides, int):
            sides = range(1, sides+1)
        super(Die, self).__init__(sides)


class Spinner(StatelessRandomizer):

    def __init__(self, sectors: Union[int, Sequence]):
        if isinstance(sectors, int):
            sectors = range(1, sectors+1)
        super(Spinner, self).__init__(sectors)

    spin = StatelessRandomizer.draw

    spins = StatelessRandomizer.draws


Wheel = Spinner
