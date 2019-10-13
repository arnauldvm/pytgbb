import unittest

from pytgbb.randomizers import StatelessRandomizer, Die

class StatelessRandomizerTestCase(unittest.TestCase):

    def testFromInt(self):
        r = StatelessRandomizer(10)
        self.assertEqual(len(r), 10)
        r.seed(0)
        for _ in range(100):
            self.assertIn(r.draw(), range(10))
        for d in r.draws(100):
            self.assertIn(d, range(10))

    def testFromSequence(self):
        seq = ('a', 'b', 'c', 1, 2, 3, 1.1, 2.2, 3.3)
        r = StatelessRandomizer(seq)
        self.assertEqual(len(r), 9)
        r.seed(0)
        for _ in range(100):
            self.assertIn(r.draw(), seq)
        for d in r.draws(100):
            self.assertIn(d, seq)

    def testFromFloat(self):
        self.assertRaises(TypeError, StatelessRandomizer, 1.1)

    def testFromDict(self):
        self.assertRaises(TypeError, StatelessRandomizer, {})

class DieTestCase(unittest.TestCase):

    def testFromInt(self):
        die = Die(10)
        self.assertEqual(len(die), 10)
        die.seed(0)
        for _ in range(100):
            self.assertIn(die.draw(), range(1, 11))
        for d in die.draws(100):
            self.assertIn(d, range(1, 11))

    def testFromSequence(self):
        seq = ('a', 'b', 'c', 1, 2, 3, 1.1, 2.2, 3.3)
        self.assertRaises(TypeError, Die, seq)
