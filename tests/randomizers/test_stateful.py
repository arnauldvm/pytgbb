import unittest

from pytgbb.randomizers import Deck


class DeckTestCase(unittest.TestCase):

    def testDraw(self):
        deck = Deck(range(1, 101))
        self.assertEqual(len(deck), 100)
        deck.seed(0)
        count = 0
        while len(deck) > 0:
            card = deck.draw()
            count += 1
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
