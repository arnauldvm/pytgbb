from collections import Sequence

from .randomizer import Randomizer


class StatelessRandomizer(Randomizer):

    def __init__(self, values):
        if isinstance(values, int):
            self.values = range(values)
        elif isinstance(values, Sequence):
            self.values = values
        else:
            raise TypeError("StatelessRandomizer constructor expects an int or a Sequence, got {}".format(type(values)))
        super(StatelessRandomizer, self).__init__()

    def draw(self):
        return self.random.choice(self.values)

    def draws(self, count=1):
        return [self.draw() for _ in range(count)]

    def __len__(self):
        return len(self.values)


class Die(StatelessRandomizer):

    def __init__(self, sides):
        if not isinstance(sides, int):
            raise TypeError("Die constructor expects an int, got {}".format(type(sides)))
        super(Die, self).__init__(sides)

    def draw(self):
        return super(Die, self).draw()+1
