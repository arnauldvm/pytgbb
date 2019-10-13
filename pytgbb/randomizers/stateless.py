from collections import Sequence

from .randomizer import Randomizer


class StatelessRandomizer(Randomizer):

    def __init__(self, values):
        if isinstance(values, int):
            self.values = range(values)
        elif isinstance(values, Sequence):
            self.values = values
        else:
            raise TypeError("Stateless constructor expects an int or a Sequence, got {}".format(type(values)))
        super(StatelessRandomizer, self).__init__()

    def draw(self):
        return self.random.choice(self.values)
