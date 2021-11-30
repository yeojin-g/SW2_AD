class Player:

    def __init__(self, beads):
        self.numOfBeads = beads

    def addBeads(self, num):
        currentBeads = self.numOfBeads + num
        self.__init__(currentBeads)

    def subBeads(self, num):
        currentBeads = self.numOfBeads - num
        self.__init__(currentBeads)

    def currentBeadsDrawing(self):
        return "O " * self.numOfBeads

    def getNumOfBeads(self):  # numOfBeads 게터함수
        return self.numOfBeads

    def messageOutput(self):
        pass
