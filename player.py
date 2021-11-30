class Player:

    def __init__(self, beads):
        self.numOfBeads = beads

    def addBeads(self, num):
        currentBeads = self.numOfBeads + num
        self.numOfBeads = currentBeads

    def subBeads(self, num):
        currentBeads = self.numOfBeads - num
        self.numOfBeads = currentBeads

    def currentBeadsDrawing(self):  # 구슬을 화면에 그리기
        result = []
        i = 0
        while i < self.numOfBeads:  # 10개씩 끊어서 그리기
            result.append("O ")
            i += 1
            if i % 10 == 0:
                result.append("\n")
        return "".join(result)

    def getNumOfBeads(self):  # numOfBeads 게터함수
        return self.numOfBeads
