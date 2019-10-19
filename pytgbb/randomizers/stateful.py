from typing import Generic, Sequence

from .randomizer import Randomizer, T


class StatefulRandomizer(Randomizer, Generic[T]):
    """
    A Randomizer that has memory.

    The likelihood of a result value at a given time is dependent from the result values that were drawn in the past.

    Examples: a deck of cards, a bag of tokens
    """
    pass


# TODO: Deck: Similar to Bag, but it does take into account that some games make possible to peek
#             at the top cards of the deck. The order must be predetermined.

class Bag(StatefulRandomizer, Generic[T]):
    """This class emulates bag of chips/counters/tokens. The draw order is not predetermined."""
    # The next value is chosen at random when drawn.

    def __init__(self, tokens: Sequence[T]):
        """Initializes a Bag. Accepts a sequence of tokens."""
        self.tokens = list(tokens)
        super(Bag, self).__init__()

    def draw(self) -> T:
        """
        Draws **one** token at random from the bag. The token is removed from the bag.
        """
        i = self.random.randrange(len(self.tokens))
        return self.tokens.pop(i)

    def __len__(self) -> int:
        """
        Returns the count of possible result values.

        This does not need to be overriden by the subclasses.
        """
        return len(self.tokens)
