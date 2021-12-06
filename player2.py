from player import Player


class Player2(Player):

    def __init__(self, beads, name, number):
        Player.__init__(self, beads)
        self.name = name
        self.number = number

    # player2이 수비자일 때 출력하는 메시지
    def messageOutput(self):
        note = f"""참가번호 {self.number}번 {self.name}. 자네가 수비할 차례네.\n몇 개를 걸텐가? 다 고르면 Enter 버튼을 누르게나.
               """
        return note
