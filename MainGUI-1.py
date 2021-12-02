import sys
from guess import Guess
from player1 import Player1  # player1: 컴퓨터
from player2 import Player2  # player2: 사용자
import time
from PyQt5.QtWidgets import *

# 두 개의 창이 공유하는 변수를 저장하는 상위클래스
class Main:
    name = ''
    playerNum = ''
    beadNum = 0


class SqGame(QWidget, Main):
    def __init__(self):  # 생성자
        super().__init__()
        self.mainVariables = Main()
        self.initUI()

    def initUI(self):
        #문자열
        title = QLabel("구슬 게임")
        name = QLabel("이름:")
        ptcNumber = QLabel("참가번호:")
        pickBeadNum = QLabel("개의 구슬로 게임 플레이")
        gameRuleTitle = QLabel("< 게임 방법 >")
        gameRule = QLabel("""\t\t각 참가자들은 선택한 개수만큼 구슬을 가지고 시작합니다.\n
                           수비자는 자신의 구슬 중 자신이 원하는만큼 손에 쥡니다.\n
                           공격자는 수비자의 손에 쥐어진 구슬의 개수가 홀수인지, 짝수인지 맞춥니다.\n
                           공격자가 홀짝 여부를 맞췄을 경우, 공격자는 수비자의 손에 쥐어진 모든 구슬을 갖게되고,\n
                           공격자가 틀렸을 경우, 수비자에게 수비자가 쥐고있던 구슬의 2배만큼 주어야 합니다.\n
                           공수교대는 한 턴마다 이루어지고, 구슬을 먼저 모두 잃게 되는 자가 게임에서 패배하게 됩니다.\n 
                           모든 참가자들은 게임에서 살아남지 못할 경우, 그 대가를 치르게 됩니다.\n
                           진행요원들이 여러분을 항시 감시하고 있으니 반칙은 삼가해주시기 바랍니다.\n
                           그럼 행운을 빕니다.""")

        #입출력창
        self.nameEdit = QLineEdit()
        self.ptcNumberEdit = QLineEdit()
        self.pickBeadNumEdit = QLineEdit()

        #버튼
        self.nextButton = QPushButton('Next Page!')

        # 가로 1열 - 타이틀
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(title)
        hbox1.addStretch(1)

        #가로 2열 - 이름, 참가번호
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(name)
        hbox2.addWidget(self.nameEdit)
        hbox2.addStretch(1)
        hbox2.addWidget(ptcNumber)
        hbox2.addWidget(self.ptcNumberEdit)
        hbox2.addStretch(1)

        #가로 3열 - 구슬 개수
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.pickBeadNumEdit)
        hbox3.addWidget(pickBeadNum)
        hbox3.addStretch(1)

        #가로 4열 - 게임룰 타이틀
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(gameRuleTitle)
        hbox4.addStretch(1)

        #가로 5열 - 게임 설명문
        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        hbox5.addWidget(gameRule)
        hbox5.addStretch(1)

        #세로
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        vbox.addLayout(hbox5)
        vbox.addStretch(1)
        vbox.addWidget(self.nextButton)
        vbox.addStretch(1)

        #버튼 연결
        self.nextButton.clicked.connect(self.settingInfo)
        self.nextButton.clicked.connect(self.next_clicked)

        #윈도우 위치 및 타이틀, 메인 레이아웃 설정
        self.setLayout(vbox)
        self.move(570, 220)
        self.setFixedSize(800, 550)
        self.setWindowTitle('구슬 게임')
        self.show()

    def next_clicked(self):
        self.hide()  # 메인 윈도우 숨김
        self.second = SecGame()
        self.second.exec() #두번째 창 닫을 때까지 기다림
        self.show()  # 두번째 창 닫으면 첫 번째 창 보여짐

    def settingInfo(self):
        Main.name = self.nameEdit.text()
        Main.playerNum = self.ptcNumberEdit.text()
        Main.beadNum = int(self.pickBeadNumEdit.text())


class SecGame(QDialog, QWidget, Main): #게임창, 2번째 창

    def __init__(self): #생성자
        super().__init__()
        self.player1 = Player1(Main.beadNum)
        self.player2 = Player2(Main.beadNum, Main.name, Main.playerNum)
        self.guess = Guess()
        self.gameRound = 1
        self.initUI()
        self.showInfo()  # 라운드, 구슬의 개수 정보를 보여줌

    def initUI(self):
       # 문자열
        remainBead1 = QLabel('player1 남은 구슬 수: ')
        remainBead2 = QLabel('player2 남은 구슬 수: ')
        choiceNum = QLabel('손에 쥘 구슬 수: ')
        round_ = QLabel('라운드')

       # 입출력창(read only 설정)
        self.round_Edit = QLineEdit()
        self.round_Edit.setReadOnly(True)
        self.messageEdit = QTextEdit()
        self.messageEdit.setReadOnly(True)
        self.choiceNumEdit = QLineEdit()
        self.remainBead1Edit = QTextEdit()
        self.remainBead1Edit.setReadOnly(True)
        self.remainBead2Edit = QTextEdit()
        self.remainBead2Edit.setReadOnly(True)

        # 버튼
        self.backButton = QPushButton('Back')
        self.oddNumButton = QPushButton('홀')
        self.evenNumButton = QPushButton('짝')
        self.enterEventButton = QPushButton('Enter')
        self.startButton = QPushButton('Game Start')

        # 라운드 알림 배치
        hboxR = QHBoxLayout()
        hboxR.addStretch(1)
        hboxR.addWidget(self.round_Edit)
        hboxR.addWidget(round_)
        hboxR.addStretch(1)

        # 홀짝 + 엔터 버튼 배치
        hboxB = QHBoxLayout()
        hboxB.addStretch(1)
        hboxB.addWidget(self.oddNumButton)
        hboxB.addStretch(1)
        hboxB.addWidget(self.evenNumButton)
        hboxB.addStretch(1)
        hboxB.addWidget(self.enterEventButton)
        hboxB.addStretch(1)

        #1-2열 - 시작 버튼, 구슬 수, 홀짝 및 엔터버튼
        grid1_2 = QGridLayout()
        grid1_2.setSpacing(15)
        grid1_2.addWidget(self.startButton, 0, 0, 1, 2)
        grid1_2.addWidget(choiceNum, 1, 0, 1, 2)
        grid1_2.addWidget(self.choiceNumEdit, 2, 0, 1, 2)
        grid1_2.addLayout(hboxB, 3, 0, 2, 2)

        # 2-1열 - player1 남은 구슬 출력 창
        grid2_1 = QGridLayout()
        grid2_1.setSpacing(15)
        grid2_1.addWidget(remainBead1, 0, 0)
        grid2_1.addWidget(self.remainBead1Edit, 1, 0, 4, 1)

        # 2-2열 - player2 남은 구슬 출력 창
        grid2_2 = QGridLayout()
        grid2_2.setSpacing(15)
        grid2_2.addWidget(remainBead2, 0, 0)
        grid2_2.addWidget(self.remainBead2Edit, 1, 0, 4, 1)

        # Grid 병합
        grid = QGridLayout()
        grid.setSpacing(15)
        grid.addLayout(hboxR, 0, 0, 1, 2)
        grid.addWidget(self.messageEdit, 1, 0, 5, 1)
        grid.addLayout(grid1_2, 1, 1, 5, 1)
        grid.addLayout(grid2_1, 7, 0)
        grid.addLayout(grid2_2, 7, 1)
        grid.addWidget(self.backButton, 10, 0, 1, 2)

        # 버튼 연결
        self.backButton.clicked.connect(self.Back)
        self.startButton.clicked.connect(self.startBeadGame)
        self.evenNumButton.clicked.connect(self.buttonClicked)
        self.oddNumButton.clicked.connect(self.buttonClicked)

        # 레이아웃, 사이즈, 윈도우 이름 설정
        self.setLayout(grid)
        self.move(600, 200)
        self.setFixedSize(700, 600)
        self.setWindowTitle('구슬 게임')
        self.show()

    def Back(self): # Back 버튼 눌렀을 때 함수
        self.close() #창 닫기
        self.close() #창 닫기

    def buttonClicked(self):
        if self.evenNumButton.isChecked():
            return "짝수"
        if self.oddNumButton.isChecked():
            return "홀수"

    # 라운드, 현재 가지고 있는 구슬을 보여주는 함수
    def showInfo(self):
        self.round_Edit.setText(str(self.gameRound))
        self.remainBead1Edit.setText(self.player1.callResult())
        self.remainBead2Edit.setText(self.player2.callResult())

    def startBeadGame(self):  # <-- 내가 차근차근 구현하려던 그 시작 부분 물론 여기부터 안돼
        self.round_Edit.setText(str(self.gameRound))
        self.remainBead1Edit.setText(self.player1.callResult())
        self.remainBead2Edit.setText(self.player2.callResult())

    def mainBeadGame(self):
        while 1:
            if SqGame.gameRound % 2 == 1:  # 홀수 판: player2(사용자)-공격, player1(컴퓨터)-수비
                selectedBeads = SqGame.player1.randomNumberOfBeads()  # player1(컴퓨터)-수비자.랜덤으로 구슬 고르기
                self.resultEdit.setText(f"<<{SqGame.gameRound}라운드>> 공격자입니다.")
                display = SqGame.player1.messageOutput()  # player1이 수비자일 때 출력하는 메시지
                self.resultEdit.setText(display)
                chosenEvenOdd = self.buttonClicked()
                if SqGame.guess.guess(selectedBeads, chosenEvenOdd):  # True일 때 = 사용자가 이겼을 때
                    SqGame.player1.subBeads(selectedBeads)  # player1 구슬 개수 감소
                    SqGame.player2.addBeads(selectedBeads)  # player2 구슬 개수 증가
                    if SqGame.guess.finished(SqGame.player1.getNumOfBeads()):  # player1가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 승리)
                        display = f"""
                                  player1은 {selectedBeads}개의 구슬을 선택했습니다.
                                  {chosenEvenOdd}를 선택했으므로 참가번호 {SqGame.number}번 {SqGame.name}님의 공격 성공입니다.
                                  이번 판에서 {selectedBeads}개의 구슬을 얻었습니다.
                                  플레이어1에게서 모든 구슬을 따냈으므로 승리입니다~~~!
                                  """
                        self.resultEdit.setText(display)
                        break
                    else:  # 계속 게임 진행
                        display = f"""
                                  player1은 {selectedBeads}개의 구슬을 선택했습니다.
                                  {chosenEvenOdd}를 선택했으므로 참가번호 {SqGame.number}번 {SqGame.name}님의 공격 성공입니다.
                                  이번 판에서 {selectedBeads}개의 구슬을 얻었습니다.
                                  """
                        self.resultEdit.setText(display)
                        # 결과 출력
                        self.remainBead1Edit.setText(SqGame.player1.result())
                        self.remainBead1Edit.setText(SqGame.player2.result())
                        self.gameRound += 1
                        self.round_Edit.setText(SqGame.gameRound)
                        continue

                else:  # False = 사용자가 졌다면
                    SqGame.player1.addBeads(selectedBeads * 2)  # player1 구슬 개수 감소
                    SqGame.player2.subBeads(selectedBeads * 2)  # player2 구슬 개수 증가
                    if SqGame.guess.finished(SqGame.player2.getNumOfBeads()):  # player2가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 패배)
                        display = f"""
                                  player1은 {selectedBeads}개의 구슬을 선택했습니다.
                                  {chosenEvenOdd}를 선택했으므로 참가번호 {SqGame.number}번 {SqGame.name}님의 공격 실패입니다.
                                  이번 판에서 {selectedBeads * 2}개의 구슬을 잃었습니다.
                                  남은 구슬이 없으므로 패배입니다.....ㅠㅠ
                                  """
                        self.resultEdit.setText(display)
                        break

                    else:  # 계속 게임 진행
                        display = f"""
                                  player1은 {selectedBeads}개의 구슬을 선택했습니다.
                                  {chosenEvenOdd}를 선택했으므로 참가번호 {SqGame.number}번 {SqGame.name}님의 공격 실패입니다.
                                  이번 판에서 {selectedBeads * 2}개의 구슬을 잃었습니다.
                                  """
                        self.resultEdit.setText(display)
                        # 결과 출력
                        self.remainBead1Edit.setText(self.player1.callResult())
                        self.remainBead1Edit.setText(SqGame.player2.result())
                        self.gameRound += 1
                        self.round_Edit.setText(SqGame.gameRound)
                        continue

            else:  # 짝수 판: player1(컴퓨터)-공격, player2(사용자)-공격
                self.resultEdit.setText(f"<<{SqGame.gameRound}라운드>> 공격자입니다.")
                display = SqGame.player2.messageOutput()  # player2가 수비자일 때 출력하는 메시지
                self.resultEdit.setText(display)
                selectedBeads = int(self.choiceNumEdit.text())  # 사용자가 건 구슬 수
                chosenEvenOdd = SqGame.player1.randomChooseOddEven()  # player1(컴퓨터)-수비자. 홀수, 짝수 둘 중 하나 랜덤으로 고르기
                self.resultEdit.setText("\t\tplayer1이 짝수/홀수를 고르는 중입니다. 잠시만 기다려주세요.")
                time.sleep(2)  # 2초 기다림

                if not SqGame.guess.guess(selectedBeads, chosenEvenOdd):  # 사용자가 이겼을 때
                    SqGame.player1.subBeads(selectedBeads * 2)  # player1 구슬 개수 감소
                    SqGame.player2.addBeads(selectedBeads * 2)  # player2 구슬 개수 증가
                    if SqGame.guess.finished(SqGame.player1.getNumOfBeads()):  # player1이 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 승리)
                        display = f"""
                                  당신은 {selectedBeads}개의 구슬을 선택했습니다.
                                  player1은 {chosenEvenOdd}를 선택했으므로 참가번호 {SqGame.number}번 {SqGame.name}님의 수비 성공입니다.
                                  이번 판에서 {selectedBeads * 2}개의 구슬을 얻었습니다.
                                  플레이어1에게서 모든 구슬을 따냈으므로 승리입니다~~~!
                                  """
                        self.resultEdit.setText(display)
                        break

                    else:  # 계속 게임 진행
                        display = f"""
                                  당신은 {selectedBeads}개의 구슬을 선택했습니다.
                                  player1은 {chosenEvenOdd}를 선택했으므로 참가번호 {SqGame.number}번 {SqGame.name}님의 수비 성공입니다.
                                  이번 판에서 {selectedBeads * 2}개의 구슬을 얻었습니다.
                                  """
                        self.resultEdit.setText(display)
                        # 결과 출력
                        self.remainBead1Edit.setText(SqGame.player1.result())
                        self.remainBead1Edit.setText(SqGame.player2.result())
                        SqGame.gameRound += 1
                        self.round_Edit.setText(SqGame.gameRound)
                        continue

                else:  # False라면 = 사용자가 졌다면
                    SqGame.player1.addBeads(selectedBeads)  # player1 구슬 개수 감소
                    SqGame.player2.subBeads(selectedBeads)  # player2 구슬 개수 증가
                    if SqGame.guess.finished(SqGame.player2.getNumOfBeads()):  # player2가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 패배)
                        display = f"""
                                  당신은 {selectedBeads}개의 구슬을 선택했습니다.
                                  player1은 {chosenEvenOdd}를 선택했으므로 참가번호 {SqGame.number}번 {SqGame.name}님의 수비 실패입니다.
                                  이번 판에서 {selectedBeads}개의 구슬을 잃었습니다.
                                  남은 구슬이 없으므로 패배입니다.....ㅠㅠ
                                  """
                        self.resultEdit.setText(display)
                        break
                    else:  # 계속 게임 진행
                        display = f"""
                                  당신은 {selectedBeads}개의 구슬을 선택했습니다.
                                  player1은 {chosenEvenOdd}를 선택했으므로 참가번호 {SqGame.number}번 {SqGame.name}님의 수비 실패입니다.
                                  이번 판에서 {selectedBeads}개의 구슬을 잃었습니다.
                                  """
                        self.resultEdit.setText(display)
                        # 결과 출력
                        self.remainBead1Edit.setText(SqGame.player1.result())
                        self.remainBead1Edit.setText(SqGame.player2.result())
                        SqGame.gameRound += 1
                        self.round_Edit.setText(SqGame.gameRound)
                        continue


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    gm = SqGame()
    sys.exit(app.exec_())
