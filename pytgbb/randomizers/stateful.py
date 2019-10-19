from typing import Generic, Sequence, List

from .randomizer import Randomizer, T


class StatefulRandomizer(Randomizer, Generic[T]):
    """
    A Randomizer that has memory.

    The likelihood of a result value at a given time is dependent from the result values that were drawn in the past.

    Examples: a deck of cards, a bag of tokens
    """
    pass


class Deck(StatefulRandomizer, Generic[T]):
    """This class emulates a deck of cards. The draw order is predetermined."""
    # TODO: Deck: Similar to Bag, but it does take into account that some games make possible to peek
    #             at the top cards of the deck. The order must be predetermined.
    #             In other words, the next value can chosen at random befoe being drawn.
    #             Once chosen, it won't change until drawn.
    # Performance optimization: we do not shuffle the whole deck at start.
    # We only pick  card at random when needed, and use a cache when peeking at cards.

    def __init__(self, cards: Sequence[T]):
        """Initializes a Deck. Accepts a sequence of cards."""
        self.cards = list(cards)
        self.cache: List[T] = []
        super(Deck, self).__init__()

    def peek(self) -> T:
        """
        Shows (a copy of) the next card from the deck. The card is **not** removed from the deck.
        """
        if not self.cache:
            self.cache.append(self._preselect())
        return self.cache[0]

    def peeks(self, count: int) -> Sequence[T]:
        """
        Shows (copies of) the next *count* cards from the deck. The cards are **not** removed from the deck.
        """
        while len(self.cache) < count:
            self.cache.append(self._preselect())
        return self.cache[0:count]

    def _preselect(self) -> T:
        # Private method for chosing a card at random
        i = self.random.randrange(len(self.cards))
        return self.cards.pop(i)

    def draw(self) -> T:
        """
        Draws the next card from the deck. The card is removed from the deck.
        """
        if self.cache:
            return self.cache.pop(0)
        return self._preselect()

    def __len__(self) -> int:
        """
        Returns the count of possible result values.

        This does not need to be overriden by the subclasses.
        """
        return len(self.cards) + len(self.cache)

    # TODO: put cards back in the deck


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

    # TODO: put tokens back in the bag
