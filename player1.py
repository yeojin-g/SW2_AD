import random
from player import Player


class Player1(Player):

    def __init__(self, beads):
        Player.__init__(self, beads)
        self.numOfBeadsList = [i for i in range(1, beads + 1)]  # 총 구슬의 개수 리스트 저장 [1, 2, 3, 4, ..., beads]
        # randomNumberOfBeads method에서 필요한 리스트

    def addBeads(self, num):
        Player.addBeads(self, num)
        self.numOfBeadsList = [i for i in range(1, self.numOfBeads + 1)]

    def subBeads(self, num):
        Player.subBeads(self, num)
        self.numOfBeadsList = [i for i in range(1, self.numOfBeads + 1)]

    # player1이 수비자일 때 랜덤으로 구슬 고르는 함수
    def randomNumberOfBeads(self):
        weight = list(reversed(self.numOfBeadsList))  # 구슬 수가 증가할수록 가중치 작아지게 하기 위해, 구슬 리스트 reverse해서 가중치 리스트로 만듦
        randomList = random.choices(self.numOfBeadsList, weights=weight, k=1)  # 가중치 다르게 해서 랜덤으로 구슬 수 뽑기
        return randomList[0]

    # player1이 공격자일 때 홀수, 짝수 둘 중 하나를 랜덤으로 고르는 함수
    def randomChooseOddEven(self):
        return random.choice(["홀수", "짝수"])

    # player1이 수비자일 때 출력하는 메시지
    def messageOutput(self):
        note = f"""플레이어1(수비자)가 {self.numOfBeads}개 중 몇 개의 구슬을 걸었습니다.\n홀수/짝수 중 하나를 선택한 다음 Enter 버튼을 눌러주세요.
               """
        return note

    # result 함수를 부르는 함수
    def callResult(self):
        return self.result('player1')
