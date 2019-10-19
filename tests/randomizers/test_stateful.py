import unittest

from pytgbb.randomizers import Bag


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
