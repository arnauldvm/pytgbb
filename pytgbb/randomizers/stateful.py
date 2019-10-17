from typing import Generic, Sequence

from .randomizer import Randomizer, T


class StatefulRandomizer(Randomizer, Generic[T]):
    """
    A Randomizer that has memory.

    The likelihood of a result value at a given time is dependent from the result values that were drawn in the past.

    Examples: a deck of cards, a bag of tokens
    """
    pass


class Deck(StatefulRandomizer, Generic[T]):
    """This class emulates deck of cards."""
    # This is a first naïve implementation where the next value is chosen at random when drawn.
    # It does not take into account that some games make possible to peek at the top cards of the deck.

    def __init__(self, cards: Sequence[T]):
        """Initializes a Deck. Accepts a sequence of cards."""
        self.cards = list(cards)
        super(Deck, self).__init__()

    def draw(self) -> T:
        """
        Draws **one** card at random from the deck. The card is removed from the deck.
        """
        i = self.random.randrange(len(self.cards))
        card = self.cards[i]
        del self.cards[i]
        return card

    def __len__(self) -> int:
        """
        Returns the count of possible result values.

        This does not need to be overriden by the subclasses.
        """
        return len(self.cards)
