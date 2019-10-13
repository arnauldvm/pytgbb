import unittest

from pytgbb.randomizers import StatelessRandomizer

class StatelessRandomizerTestCase(unittest.TestCase):

    def testFromInt(self):
        r = StatelessRandomizer(10)
        for _ in range(100):
            self.assertIn(r.draw(), range(10))

    def testFromSequence(self):
        seq = ('a', 'b', 'c', 1, 2, 3, 1.1, 2.2, 3.3)
        r = StatelessRandomizer(seq)
        for _ in range(100):
            self.assertIn(r.draw(), seq)
    
    def testFromFloat(self):
        self.assertRaises(TypeError, StatelessRandomizer, 1.1)
    
    def testFromDict(self):
        self.assertRaises(TypeError, StatelessRandomizer, {})
