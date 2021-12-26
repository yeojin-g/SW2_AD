import unittest

from player1 import Player1


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.p1 = Player1(10)
        self.p2 = Player1(20)

    def testAddBeads(self):
        self.assertEqual(self.p1.getNumOfBeads(), 10)
        self.p1.addBeads(12)
        self.assertEqual(self.p1.getNumOfBeads(), 22)

    def testSubBeads(self):
        self.assertEqual(self.p1.getNumOfBeads(), 10)
        self.p1.subBeads(12)
        self.assertEqual(self.p1.getNumOfBeads(), -2)

    def testCurrentBeadsDrawing(self):
        self.assertEqual(self.p1.currentBeadsDrawing(), "O O O O O O O O O O \n")
        self.assertEqual(self.p2.currentBeadsDrawing(), "O O O O O O O O O O \nO O O O O O O O O O \n")

    def testGetNumOfBeads(self):
        self.assertEqual(self.p1.getNumOfBeads(), 10)
        self.assertEqual(self.p2.getNumOfBeads(), 20)

    def testRandomNumberOfBeads(self):
        self.assertIn(self.p1.randomNumberOfBeads(), [i for i in range(1, 11)])
        self.assertIn(self.p2.randomNumberOfBeads(), [i for i in range(1, 21)])

    def testRandomChooseOddEven(self):
        self.assertIn(self.p1.randomChooseOddEven(), ["홀수", "짝수"])
        self.assertIn(self.p2.randomChooseOddEven(), ["홀수", "짝수"])

    def testMessageOutput(self):
        p1note = """
               플레이어1(수비자)가 10개 중 몇 개의 구슬을 걸었습니다.
               홀수/짝수 중 하나를 입력하세요.
               """
        p2note = """
               플레이어1(수비자)가 20개 중 몇 개의 구슬을 걸었습니다.
               홀수/짝수 중 하나를 입력하세요.
               """
        self.assertEqual(self.p1.messageOutput(), p1note)
        self.assertEqual(self.p2.messageOutput(), p2note)

    def testResult(self):
        self.assertEqual(self.p1.result("Yeojin"), "")


if __name__ == '__main__':
    unittest.main()