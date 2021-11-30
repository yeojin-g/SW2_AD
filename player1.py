import random
from player import Player


class Player1(Player):

    def __init__(self, beads):
        Player.__init__(self, beads)
        self.numOfBeadsList = [i for i in range(1, beads + 1)]  # 총 구슬의 개수 리스트 저장 [1, 2, 3, 4, ..., beads]

    def addBeads(self, num):  # player1이 이겼을 경우 구슬 수를 더해준다.
        Player.addBeads(self, num)
        self.numOfBeadsList = [i for i in range(1, self.numOfBeads + 1)]

    def subBeads(self, num):  # player1이 졌을 경우 구슬 수를 빼준다.
        Player.subBeads(self, num)
        self.numOfBeadsList = [i for i in range(1, self.numOfBeads + 1)]

    def randomNumberOfBeads(self):  # 랜덤으로 구슬 고르기
        weight = list(reversed(self.numOfBeadsList))  # 구슬 수가 증가할수록 가중치 작아지게 하기 위해, 구슬 리스트 reverse해서 가중치 리스트로 만듦
        rlist = random.choices(self.numOfBeadsList, weights=weight, k=1)  # 가중치 다르게해서 랜덤으로 구슬 수 뽑기
        return rlist[0]

    def randomChooseOddEven(self):
        return random.choice(["홀수", "짝수"])  # 홀수, 짝수 둘 중 하나 고르기

    def messageOutput(self):
        note = """
               플레이어1(수비자)가 구슬을 걸었습니다.
               홀수/짝수 중 하나를 입력하세요.
               """
        return note

