import random
from player import Player


class Player1(Player):

    def __init__(self, beads):
        Player.__init__(self, beads)
        self.numOfBeadsList = [i for i in range(1, beads + 1)]  # 총 구슬의 개수 리스트 저장

    def addBeads(self, num):
        currentBeads = self.numOfBeads + num
        self.__init__(currentBeads)

    def subBeads(self, num):
        currentBeads = self.numOfBeads - num
        self.__init__(currentBeads)

    def randomNumberOfBeads(self):
        r = random.randrange(self.numOfBeads)
        return self.numOfBeadsList[r]

    def randomChooseOddEven(self):
        return random.choice(["홀수", "짝수"])

    def messageOutput(self):
        note = """
               플레이어1(수비자)가 구슬을 걸었습니다.
               홀수/짝수 중 하나를 입력하세요.
               """
        return note

