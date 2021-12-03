from player import Player


class Player2(Player):

    def __init__(self, beads, name, number):
        Player.__init__(self, beads)
        self.name = name
        self.number = number

    # player2이 수비자일 때 출력하는 메시지
    def messageOutput(self):
        note = f"""참가번호 {self.number}번 {self.name}님의 수비입니다.\n이번 게임에 걸 구슬의 개수를 입력한 다음 Enter 버튼을 눌러주세요.
               """
        return note

    # result 함수를 부르는 함수
    def callResult(self):
        return self.result(self.name)
