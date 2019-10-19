import unittest

from pytgbb.randomizers import Deck, Bag


class DeckTestCase(unittest.TestCase):

    def testDrawPeekLen(self):
        deck = Deck(range(1, 101))
        self.assertEqual(len(deck), 100)
        deck.seed(0)
        count = 0
        while len(deck) > 0:
            self.assertIn(deck.peek(), range(1, 101))
            card = deck.draw()
            count += 1
            self.assertEqual(len(deck), 100-count)
            self.assertIn(card, range(1, 101))
        self.assertEqual(count, 100)

    def testDraws(self):
        deck = Deck(range(1, 101))
        self.assertEqual(len(deck), 100)
        deck.seed(0)
        count = 0
        while len(deck) > 0:
            cards = deck.draws(10)
            count += len(cards)
            for card in cards:
                self.assertIn(card, range(1, 101))
        self.assertEqual(count, 100)

    def testPeeks(self):
        seq = (9, 10, 'J', 'Q', 'K', 'A')
        deck = Deck(seq)
        self.assertEqual(len(deck), 6)
        deck.seed(0)
        cards = deck.peeks(2)
        self.assertEqual(len(deck), 6)
        for card in cards:
            self.assertIn(card, seq)
        cards = deck.draws(3)
        self.assertEqual(len(deck), 3)
        for card in cards:
            self.assertIn(card, seq)
        cards = deck.peeks(3)
        self.assertEqual(len(deck), 3)
        for card in cards:
            self.assertIn(card, seq)
        card = deck.draw()
        self.assertEqual(len(deck), 2)
        self.assertIn(card, seq)
        cards = deck.draws(2)
        self.assertEqual(len(deck), 0)
        for card in cards:
            self.assertIn(card, seq)


class BagTestCase(unittest.TestCase):

    def testDraw(self):
        bag = Bag(range(1, 101))
        self.assertEqual(len(bag), 100)
        bag.seed(0)
        count = 0
        while len(bag) > 0:
            token = bag.draw()
            count += 1
            self.assertIn(token, range(1, 101))
        self.assertEqual(count, 100)

    def testDraws(self):
        bag = Bag(range(1, 101))
        self.assertEqual(len(bag), 100)
        bag.seed(0)
        count = 0
        while len(bag) > 0:
            tokens = bag.draws(10)
            count += len(tokens)
            for token in tokens:
                self.assertIn(token, range(1, 101))
        self.assertEqual(count, 100)
