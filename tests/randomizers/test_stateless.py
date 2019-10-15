import unittest

from pytgbb.randomizers import StatelessRandomizer, Die, Spinner, Wheel


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
        seq = (9, 10, 'J', 'Q', 'K', 'A')
        die = Die(seq)
        self.assertEqual(len(die), 6)
        die.seed(0)
        for _ in range(100):
            self.assertIn(die.draw(), seq)
        for d in die.draws(100):
            self.assertIn(d, seq)


class SpinnerTestCase(unittest.TestCase):

    def testFromInt(self):
        spinner = Spinner(10)
        self.assertEqual(len(spinner), 10)
        spinner.seed(0)
        for _ in range(100):
            self.assertIn(spinner.spin(), range(1, 11))
        for d in spinner.spins(100):
            self.assertIn(d, range(1, 11))

    def testFromSequence(self):
        seq = (9, 10, 'J', 'Q', 'K', 'A')
        spinner = Spinner(seq)
        self.assertEqual(len(spinner), 6)
        spinner.seed(0)
        for _ in range(100):
            self.assertIn(spinner.spin(), seq)
        for d in spinner.spins(100):
            self.assertIn(d, seq)


class WheelTestCase(unittest.TestCase):

    def testFromInt(self):
        wheel = Wheel(15)
        self.assertEqual(len(wheel), 15)
        wheel.seed(0)
        for _ in range(100):
            self.assertIn(wheel.spin(), range(1, 16))
        for d in wheel.spins(100):
            self.assertIn(d, range(1, 16))
