import unittest

from guess import Guess


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess()

    def testGuess(self):
        self.assertTrue(self.g1.guess(13, '홀수'))
        self.assertTrue(self.g1.guess(16, '짝수'))

    def testFinished(self):
        self.assertFalse(self.g1.finished(3))
        self.assertTrue(self.g1.finished(-10))
        self.assertTrue(self.g1.finished(0))


if __name__ == '__main__':
    unittest.main()