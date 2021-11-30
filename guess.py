class Guess:
    def __init__(self):
        pass

    def guess(self, selectedBeads, chosenEvenOdd):
        if (((selectedBeads % 2 == 1) and (chosenEvenOdd == "홀수")) or  # 맞춤
           ((selectedBeads % 2 == 0) and (chosenEvenOdd == "짝수"))):
            return True
        else:
            return False

    def finished(self, beads):
        if beads <= 0:
            return True
        else:
            return False

