import unittest

from player2 import Player2


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.p1 = Player2(5, "Yeojin", 123)
        self.p2 = Player2(15, "Bomi", 234)

    def testAddBeads(self):
        self.assertEqual(self.p1.getNumOfBeads(), 5)
        self.p1.addBeads(12)
        self.assertEqual(self.p1.getNumOfBeads(), 17)

    def testSubBeads(self):
        self.assertEqual(self.p2.getNumOfBeads(), 15)
        self.p2.subBeads(15)
        self.assertEqual(self.p2.getNumOfBeads(), 0)

    def testCurrentBeadsDrawing(self):
        self.assertEqual(self.p1.currentBeadsDrawing(), "O O O O O ")
        self.assertEqual(self.p2.currentBeadsDrawing(), "O O O O O O O O O O \nO O O O O ")

    def testGetNumOfBeads(self):
        self.assertEqual(self.p1.getNumOfBeads(), 5)
        self.assertEqual(self.p2.getNumOfBeads(), 15)

    def testMessageOutput(self):
        p1Note = """
               참가번호 123번 Yeojin님의 수비입니다.
               이번 게임에 걸 구슬의 개수를 입력하세요.
               """
        p2Note = """
               참가번호 234번 Bomi님의 수비입니다.
               이번 게임에 걸 구슬의 개수를 입력하세요.
               """
        self.assertEqual(self.p1.messageOutput(), p1Note)
        self.assertEqual(self.p2.messageOutput(), p2Note)


if __name__ == '__main__':
    unittest.main()
