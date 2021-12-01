"""
Player1, Player2에서 중복되는 함수가 있어, Player1 class와 player2 class가 상속받는 상위 클래스를 만듦.
"""


class Player:

    def __init__(self, beads):
        self.numOfBeads = beads  # 구슬의 개수(beads)를 저장

    # player가 이겼을 경우 구슬 수(num)를 더해주는 함수
    def addBeads(self, num):
        currentBeads = self.numOfBeads + num
        self.numOfBeads = currentBeads

    # player가 졌을 경우 구슬 수(num)를 빼주는 함수
    def subBeads(self, num):
        currentBeads = self.numOfBeads - num
        self.numOfBeads = currentBeads

    # 구슬을 화면에 그리는 함수
    def currentBeadsDrawing(self):
        result = []
        i = 0
        while i < self.numOfBeads:  # 구슬을 10개씩 끊어서 그리기
            result.append("O ")
            i += 1
            if i % 10 == 0:
                result.append("\n")
        return "".join(result)

    # numOfBeads 게터함수
    def getNumOfBeads(self):
        return self.numOfBeads

    # 한 라운드를 한 뒤 플레이어의 남은 구슬 수 프린트하는 함수
    def result(self, name):
        pRes = self.currentBeadsDrawing()
        res = f'''{name}님 남은 구슬: {self.getNumOfBeads()}개\n{pRes}'''
        return res

