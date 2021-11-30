class Guess:
    def __init__(self):
        pass

    # 홀수/짝수 맞췄으면 true, 틀렸으면 false를 return하는 함수
    def guess(self, selectedBeads, chosenEvenOdd):  # selectedBeads: 선택한 구슬의 개수 / chosenEvenOdd: 짝 or 홀
        if (((selectedBeads % 2 == 1) and (chosenEvenOdd == "홀수")) or  # 맞춤
           ((selectedBeads % 2 == 0) and (chosenEvenOdd == "짝수"))):
            return True
        else:
            return False

    # player가 구슬이 없는지 확인하는 함수 (게임이 끝났는지 확인하는 함수)
    def finished(self, beads):  # beads: 구슬의 개수
        if beads <= 0:
            return True
        else:
            return False
