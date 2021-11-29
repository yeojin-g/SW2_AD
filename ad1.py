import sys
from PyQt5.QtWidgets import *


class SqGame(QWidget):
    def __init__(self): #생성자
        super().__init__()
        self.initUI()

    def initUI(self):
        #문자열
        title = QLabel("구슬 게임")
        name = QLabel("이름:")
        ptcNumber = QLabel("\t참가번호:")
        pickBeadNum = QLabel("개의 구슬로 게임 플레이")
        gameRuleTitle = QLabel("< 게임 방법 >")
        gameRule = QLabel("""\t\t각 참가자들은 선택한 개수만큼 구슬을 가지고 시작합니다.\n
                           수비자는 자신의 구슬 중 자신이 원하는만큼 손에 쥡니다.\n
                           공격자는 수비자의 손에 쥐어진 구슬의 개수가 홀수인지, 짝수인지 맞춥니다.\n
                           공격자가 홀짝 여부를 맞췄을 경우, 수비자의 손에 쥐어진 모든 구슬을 갖게되고,\n
                           공격자가 틀렸을 경우, 수비자가 쥐고있던 구슬 개수의 2배에 해당하는 구슬을 수비자에게 주게됩니다.\n
                           공수교대는 한 턴마다 이루어지고, 구슬을 모두 잃게 되는 자가 게임에서 패배하게 됩니다.\n 
                           게임에서 살아남지 못할 경우, 그 대가를 치르게 됩니다.\n
                           진행요원들이 여러분을 항시 감시하고 있으니 반칙은 삼가해주시기 바랍니다.\n
                           그럼 행운을 빕니다.""")

        #입출력창
        self.nameEdit = QLineEdit()
        self.ptcNumberEdit = QLineEdit()
        self.pickBeadNumEdit = QLineEdit('10 이상 20 이하')

        #버튼
        self.startButton = QPushButton('Game Start!')

        # 가로 1열 - 타이틀
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(title)
        hbox1.addStretch(1)

        #가로 2열 - 이름, 참가번호
        hbox2 = QHBoxLayout()
        hbox2.addWidget(name)
        hbox2.addWidget(self.nameEdit)
        hbox2.addWidget(ptcNumber)
        hbox2.addWidget(self.ptcNumberEdit)

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

        #가로 6열 - 버튼
        hbox6 = QHBoxLayout()
        hbox6.addWidget(self.startButton)

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
        vbox.addLayout(hbox6)

        #버튼 연결
        self.startButton.clicked.connect(self.start_clicked)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('구슬 게임')
        self.show()

    def start_clicked(self):
        self.hide() # 메인 윈도우 숨김
        self.second = game()
        self.second.exec() #두번째 창 닫을 때까지 기다림
        self.show() # 두번째 창 닫으면 첫 번째 창 보여짐

class game(QDialog, QWidget):
    def __init__(self): #생성자
        super(game, self).__init__()
        self.initUI()


    def initUI(self):
       # 문자열
        remainBead = QLabel('남은 구슬 수: ')
        choiceNum = QLabel('손에 쥘 구슬 수: ')
        round_ = QLabel('라운드')


       # 입출력창
        self.resultEdit = QTextEdit()
        self.remainBeadEdit = QLineEdit()
        self.choiceNumEdit = QLineEdit()
        self.messageEdit = QTextEdit()
        self.round_Edit = QLineEdit()

        # 버튼
        self.homeButton = QPushButton('Go Home')
        self.oddNumButton = QPushButton('홀')
        self.evenNumButton = QPushButton('짝')
        self.enterEventButton = QPushButton('Enter')

        # 라운드 알림 배치
        hbox = QHBoxLayout()
        hbox.addWidget(self.round_Edit)
        hbox.addWidget(round_)

        # 홀짝 + 엔터 버튼 배치
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.oddNumButton)
        hbox1.addStretch(1)
        hbox1.addWidget(self.evenNumButton)
        hbox1.addStretch(1)
        hbox1.addWidget(self.enterEventButton)

        #세로 1열 배치 - 결과창 + 메세지창
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.resultEdit)
        vbox1.addStretch(1)
        vbox1.addWidget(self.messageEdit)

        #세로 2열 배치(1) - 남은 구슬, 손에 쥘 구슬
        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox)
        vbox2.addStretch(1)
        vbox2.addWidget(remainBead)
        vbox2.addStretch(1)
        vbox2.addWidget(self.remainBeadEdit)
        vbox2.addStretch(1)
        vbox2.addWidget(choiceNum)
        vbox2.addStretch(1)
        vbox2.addWidget(self.choiceNumEdit)
        vbox2.addStretch(1)
        vbox2.addLayout(hbox1)
        vbox2.addStretch(3)
        vbox2.addWidget(self.homeButton)

        #세로열 병합
        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1)
        vbox1.addStretch(1)
        hbox2.addLayout(vbox2)

        # 버튼 연결
        self.homeButton.clicked.connect(self.Home)

        # 레이아웃, 사이즈, 윈도우 이름 설정
        self.setLayout(hbox2)
        self.resize(700, 700)
        self.setWindowTitle('구슬 게임')
        self.show()

    def Home(self): # go home 버튼 눌렀을 때 함수
        self.close() #창 닫기

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    gm = SqGame()
    sys.exit(app.exec_())