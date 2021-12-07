import sys
from guess import Guess
from player1 import Player1  # player1: 컴퓨터
from player2 import Player2  # player2: 사용자
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


# 두 개의 창이 공유하는 변수를 저장하는 상위클래스
class Main:
    name = None
    playerNum = None
    beadNum = 0


class SqGame(QWidget, Main):
    def __init__(self):  # 생성자
        super().__init__()
        self.initUI()
        self.setWidgetStyle()

    def setWidgetStyle(self):
        # 배경색 설정
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(0, 0, 0))  # 검은색
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        # 글씨색 설정
        pal.setColor(QPalette.WindowText, QColor(255, 255, 255))  # 흰색
        self.setPalette(pal)

        # 폰트 변경
        font = QFontDatabase()
        font.addApplicationFont('./나눔손글씨 할아버지의나눔.ttf')
        app.setFont(QFont('나눔손글씨 할아버지의나눔', 14))

    def initUI(self):
        # 이미지
        titleImgLabel = QLabel(self)  # 오징어게임 타이틀 이미지 라벨
        titleImg = QPixmap('./title.png')  # 오징어게임 타이틀 이미지
        titleImg = titleImg.scaledToWidth(300)  # 이미지 사이즈 조정
        titleImgLabel.setPixmap(titleImg)  # 라벨과 연결
        titleImgLabel.setAlignment(Qt.AlignCenter)  # 가운데 정렬

        # 문자열
        title = QLabel("- 구슬 게임 -")
        name = QLabel("이름:")
        ptcNumber = QLabel("참가번호:")
        pickBeadNum = QLabel("개의 구슬로 게임 플레이")
        gameRuleTitle = QLabel("< 게임 방법 >")
        gameRule = QLabel("""각 참가자들은 선택한 개수만큼 구슬을 가지고 시작합니다.\n수비자는 자신의 구슬 중 자신이 원하는만큼 손에 쥡니다.\n공격자는 수비자의 손에 쥐어진 구슬의 개수가 홀수인지, 짝수인지 맞춥니다.\n공격자가 홀짝 여부를 맞췄을 경우, 공격자는 수비자의 손에 쥐어진 모든 구슬을 갖게되고,\n공격자가 틀렸을 경우, 수비자에게 수비자가 쥐고있던 구슬의 2배만큼 주어야 합니다.\n공수교대는 한 턴마다 이루어지고, 구슬을 먼저 모두 잃게 되는 자가 게임에서 패배하게 됩니다.\n 모든 참가자들은 게임에서 살아남지 못할 경우, 그 대가를 치르게 됩니다.\n진행요원들이 여러분을 항시 감시하고 있으니 반칙은 삼가해주시기 바랍니다.\n그럼 행운을 빕니다.""")

        # 게임 룰 글씨 가운데 정렬
        gameRule.setAlignment(Qt.AlignCenter)
        gameRuleTitle.setAlignment(Qt.AlignCenter)

        # 입출력창
        self.nameEdit = QLineEdit()
        self.ptcNumberEdit = QLineEdit()
        self.pickBeadNumEdit = QLineEdit("10개 이상, 15개 이하")
        self.ErrorEdit = QLineEdit()  # 에러메시지 적는 칸
        self.ErrorEdit.setReadOnly(True)
        self.ErrorEdit.setStyleSheet("color: rgb(233, 075, 134);")  # '오징어게임' 타이틀과 색상이 같게

        # 버튼
        self.nextButton = QPushButton('Next Page!')

        # 가로 1열 - 타이틀
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(title)
        hbox1.addStretch(1)

        # 가로 2열 - 이름, 참가번호
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(name)
        hbox2.addWidget(self.nameEdit)
        hbox2.addStretch(1)
        hbox2.addWidget(ptcNumber)
        hbox2.addWidget(self.ptcNumberEdit)
        hbox2.addStretch(1)

        # 가로 3열 - 구슬 개수
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.pickBeadNumEdit)
        hbox3.addWidget(pickBeadNum)
        hbox3.addStretch(1)

        # 가로 4열 - 게임룰 타이틀
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(gameRuleTitle)
        hbox4.addStretch(1)

        # 가로 5열 - 게임 설명문
        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        hbox5.addWidget(gameRule)
        hbox5.addStretch(1)

        # 세로
        vbox = QVBoxLayout()
        vbox.addWidget(titleImgLabel)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addStretch(1)
        vbox.addWidget(self.ErrorEdit)
        vbox.addStretch(1)
        vbox.addWidget(self.nextButton)
        vbox.addStretch(1)

        # 버튼 연결
        self.nextButton.clicked.connect(self.settingInfo)
        self.nextButton.clicked.connect(self.next_clicked)

        # 윈도우 위치 및 타이틀, 메인 레이아웃 설정
        self.setLayout(vbox)
        self.move(570, 220)
        self.setFixedSize(800, 600)
        self.setWindowTitle('구슬 게임')
        self.show()

    def next_clicked(self):
        self.hide()  # 메인 윈도우 숨김
        self.second = SecGame()
        self.second.exec()  # 두번째 창 닫을 때까지 기다림
        self.show()  # 두번째 창 닫으면 첫 번째 창 보여짐

    def settingInfo(self):
        # 예외 처리
        if not self.ptcNumberEdit.text().isdecimal():
            self.ErrorEdit.setText("참가번호에는 숫자만 입력해주십시오.")
        elif not self.pickBeadNumEdit.text().isdecimal():
            self.ErrorEdit.setText("총 구슬의 개수는 숫자만 입력해주십시오.")
        elif not (10 <= int(self.pickBeadNumEdit.text()) <= 15):
            self.ErrorEdit.setText("총 구슬의 개수는 10에서 15까지의 숫자만 입력해주십시오.")
        else:
            Main.name = self.nameEdit.text()
            Main.playerNum = self.ptcNumberEdit.text()
            Main.beadNum = int(self.pickBeadNumEdit.text())
            self.next_clicked()


class SecGame(QDialog, QWidget, Main):  # 게임창, 2번째 창

    def __init__(self):  # 생성자
        super().__init__()
        self.setWidgetStyle()

        # 객체 및 변수 설정
        self.player1 = Player1(Main.beadNum)
        self.player2 = Player2(Main.beadNum, Main.name, Main.playerNum)
        self.guess_Ob = Guess()
        self.gameRound = 1
        self.initUI()
        self.showInfo()  # 구슬의 개수 정보를 보여줌
        self.oddOrEven = ''  # 사용자가 공격하는 경우, 즉 홀수판의 경우 사용자가 홀/짝 중 고른 것을 저장하는 변수

    def setWidgetStyle(self):
        # 배경색 설정
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(0, 0, 0))  # 검은색
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        # 글씨색 설정
        pal.setColor(QPalette.WindowText, QColor(255, 255, 255)) # 흰색
        self.setPalette(pal)

        # 폰트 변경
        font = QFontDatabase()
        font.addApplicationFont('./나눔손글씨 할아버지의나눔.ttf')
        app.setFont(QFont('나눔손글씨 할아버지의나눔', 13))

    def initUI(self):
        # 이미지
        titleImgLabel = QLabel(self)  # 오징어게임 타이틀 이미지 라벨
        titleImg = QPixmap('./title.png')  # 오징어게임 타이틀 이미지
        titleImg = titleImg.scaledToWidth(200)  # 이미지 사이즈 조정
        titleImgLabel.setPixmap(titleImg)  # 라벨과 연결
        titleImgLabel.setAlignment(Qt.AlignCenter)  # 왼쪽 정렬

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
        self.restartButton = QPushButton('Restart')

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

        # 1-2열 - 시작 버튼, 구슬 수, 홀짝 및 엔터버튼, 재시작 버튼
        grid1_2 = QGridLayout()
        grid1_2.setSpacing(15)
        grid1_2.addWidget(self.startButton, 0, 0, 1, 2)
        grid1_2.addWidget(choiceNum, 1, 0, 1, 2)
        grid1_2.addWidget(self.choiceNumEdit, 2, 0, 1, 2)
        grid1_2.addLayout(hboxB, 3, 0, 2, 2)
        grid1_2.addWidget(self.restartButton, 4, 0, 1, 2)

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
        grid.addWidget(titleImgLabel, 0, 0, 1, 1)
        grid.addLayout(hboxR, 0, 1, 1, 1)
        grid.addWidget(self.messageEdit, 1, 0, 5, 1)
        grid.addLayout(grid1_2, 1, 1, 5, 1)
        grid.addLayout(grid2_1, 7, 0)
        grid.addLayout(grid2_2, 7, 1)
        grid.addWidget(self.backButton, 10, 0, 1, 2)

        # 버튼 연결
        self.backButton.clicked.connect(self.Back)
        self.startButton.clicked.connect(self.startBeadGame)
        self.oddNumButton.clicked.connect(self.oddNumButtonClicked)
        self.evenNumButton.clicked.connect(self.evenNumButtonClicked)
        self.enterEventButton.clicked.connect(self.enterEventButtonClicked)

        # 레이아웃, 사이즈, 윈도우 이름 설정
        self.setLayout(grid)
        self.move(600, 150)
        self.setFixedSize(700, 700)
        self.setWindowTitle('구슬 게임')
        self.show()

        # 게임 시작버튼을 누르라는 메시지 출력
        self.messageEdit.setText("게임을 시작할까?\n그렇다면 Game Start 버튼을 누르게.")

    def Back(self):  # Back 버튼 눌렀을 때 함수
        self.close()  # 창 닫기
        self.close()  # 창 닫기

    def oddNumButtonClicked(self):
        self.oddOrEven = "홀수"

    def evenNumButtonClicked(self):
        self.oddOrEven = "짝수"

    def enterEventButtonClicked(self):  # gameRound의 홀/짝에 따라 다른 함수 실행하게 함
        if self.gameRound % 2 == 1:  # 홀수판이면
            self.guessWhenRoundOdd(self.oddOrEven)
        else:
            self.guessWhenRoundEven()

    def guessWhenRoundOdd(self, answer):  # 홀수판 / player1(컴퓨터): 수비자, player2(사용자): 공격자
        selectedBeads = self.player1.randomNumberOfBeads()  # player1(컴퓨터)-수비자.랜덤으로 구슬 고르기
        if self.guess_Ob.guess(selectedBeads, answer):  # True일 때 = 사용자가 이겼을 때
            if selectedBeads > self.player1.getNumOfBeads():
                selectedBeads = self.player1.getNumOfBeads()
            self.player1.subBeads(selectedBeads)  # player1 구슬 개수 감소
            self.player2.addBeads(selectedBeads)  # player2 구슬 개수 증가
            if self.guess_Ob.finished(self.player1.getNumOfBeads()):  # player1가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 승리)
                display = f"""자, 나는 {selectedBeads}개를 쥐었었네.\n자네가 {answer}라고 했으니\n참가번호 {Main.playerNum}번 {Main.name},\n자네의 공격이 먹혔구만.\n여기 {selectedBeads}개의 구슬을 주겠네.\n\n이런, 내 구슬을 다 잃었구만..!\n괜찮네. 다 가져, 자네꺼야. 우린 깐부잖아. 
                          """
                self.messageEdit.setText(display)
                self.showInfo()

            else:  # 계속 게임 진행
                display = f"""자, 나는 {selectedBeads}개를 쥐었었네.\n자네가 {answer}라고 했으니\n참가번호 {Main.playerNum}번 {Main.name},\n자네의 공격이 먹혔구만.\n여기 {selectedBeads}개의 구슬을 주겠네.
                          """
                self.messageEdit.setText(display)
                # 결과 출력
                self.showInfo()
                self.gameRound += 1
                self.messageEdit.append("\n다음 판을 할 준비가 됐나?\n됐다면 Game Start 버튼을 누르게.")

        else:  # False = 사용자가 졌다면
            changeBeads = selectedBeads * 2
            if changeBeads > self.player2.getNumOfBeads():
                changeBeads = self.player2.getNumOfBeads()
            self.player1.addBeads(changeBeads)  # player1 구슬 개수 증가
            self.player2.subBeads(changeBeads)  # player2 구슬 개수 감소
            if self.guess_Ob.finished(self.player2.getNumOfBeads()):  # player2가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 패배)
                display = f"""자, 나는 {selectedBeads}개를 쥐었었네.\n자네가 {answer}라고 했으니\n이런! 참가번호 {Main.playerNum}번 {Main.name},\n자네가 졌구만. 허허.\n어서 {selectedBeads * 2}개의 구슬을 나에게 주게.\n\n아니, 설마 자네 구슬을 다 잃은겐가?\n너무 그렇게 보지 말게나. 우린 깐부잖아~
                          """
                self.messageEdit.setText(display)
                self.showInfo()

            else:  # 계속 게임 진행
                display = f"""자, 나는 {selectedBeads}개를 쥐었었네.\n자네가 {answer}라고 했으니\n이런! 참가번호 {Main.playerNum}번 {Main.name},\n자네가 졌구만. 허허.\n어서 {selectedBeads * 2}개의 구슬을 나에게 주게.
                          """
                self.messageEdit.setText(display)
                # 결과 출력
                self.showInfo()
                self.gameRound += 1
                # self.round_Edit.setText(str(self.gameRound))
                self.messageEdit.append("\n다음 라운드로 가보자고!\nGame Start 버튼을 누르게.")

    def guessWhenRoundEven(self):  # 짝수판 / player1(컴퓨터): 공격자, player2(사용자): 수비자
        selectedBeads = int(self.choiceNumEdit.text())  # 사용자가 건 구슬 수
        chosenEvenOdd = self.player1.randomChooseOddEven()  # player1(컴퓨터)-수비자. 홀수, 짝수 둘 중 하나 랜덤으로 고르기
        display = "잠깐.. 고민할 시간을 좀 주게나.."
        self.messageEdit.setText(display)
        time.sleep(2)  # 2초 기다림

        if not self.guess_Ob.guess(selectedBeads, chosenEvenOdd):  # 사용자가 이겼을 때
            changeBeads = selectedBeads * 2
            if changeBeads > self.player1.getNumOfBeads():
                changeBeads = self.player1.getNumOfBeads()
            self.player1.subBeads(changeBeads)  # player1 구슬 개수 감소
            self.player2.addBeads(changeBeads)  # player2 구슬 개수 증가
            if self.guess_Ob.finished(
                    self.player1.getNumOfBeads()):  # player1이 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 승리)
                display = f"""흠, 자네는 {selectedBeads}개를 쥐고있었구만.\n내가 방금 뭐라 그랬더라..?\n아, 나는 {chosenEvenOdd}라 했네!\n이런! 참가번호 {Main.playerNum}번 {Main.name}, 자네가 수비에 성공했구만.\n여기 {selectedBeads * 2}개의 구슬을 주지.\n\n이런, 내 구슬을 다 잃었구만..!\n괜찮네. 다 가져, 자네꺼야. 우린 깐부잖아.
                          """
                self.messageEdit.setText(display)
                self.showInfo()

            else:  # 계속 게임 진행
                display = f"""흠, 자네는 {selectedBeads}개를 쥐고있었구만.\n내가 방금 뭐라 그랬더라..?\n아, 나는 {chosenEvenOdd}라 했네!\n이런! 참가번호 {Main.playerNum}번 {Main.name}, 자네가 수비에 성공했구만.\n여기 {selectedBeads * 2}개의 구슬을 주지.
                          """
                self.messageEdit.setText(display)
                # 결과 출력
                self.showInfo()
                self.gameRound += 1
                # self.round_Edit.setText(str(self.gameRound))
                self.messageEdit.append("\n다음 라운드로 가보자고!\nGame Start 버튼을 누르게.")

        else:  # False라면 = 사용자가 졌다면
            if selectedBeads > self.player2.getNumOfBeads():
                selectedBeads = self.player2.getNumOfBeads()
            self.player1.addBeads(selectedBeads)  # player1 구슬 개수 증가
            self.player2.subBeads(selectedBeads)  # player2 구슬 개수 감소
            if self.guess_Ob.finished(
                    self.player2.getNumOfBeads()):  # player2가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 패배)
                display = f"""흠, 자네는 {selectedBeads}개를 쥐고있었구만.\n내가 방금 뭐라 그랬더라..?\n아, 나는 {chosenEvenOdd}라 했네!\n허허! 참가번호 {Main.playerNum}번 {Main.name}, 자네가 졌구만!\n어서 {selectedBeads}개의 구슬을 나에게 주게.\n\n아니, 설마 자네 구슬을 다 잃은겐가?\n너무 그렇게 보지 말게나. 우린 깐부잖아~
                          """
                self.messageEdit.setText(display)
                self.showInfo()

            else:  # 계속 게임 진행
                display = f"""흠, 자네는 {selectedBeads}개를 쥐고있었구만.\n내가 방금 뭐라 그랬더라..?\n아, 나는 {chosenEvenOdd}라 했네!\n허허! 참가번호 {Main.playerNum}번 {Main.name}, 자네가 졌구만!\n어서 {selectedBeads}개의 구슬을 나에게 주게.
                          """
                self.messageEdit.setText(display)
                # 결과 출력
                self.showInfo()
                self.gameRound += 1
                # self.round_Edit.setText(str(self.gameRound))
                self.messageEdit.append("\n다음 판을 할 준비가 됐나?\n됐다면 Game Start 버튼을 누르게.")

    # 현재 가지고 있는 구슬을 보여주는 함수
    def showInfo(self):
        self.remainBead1Edit.setText(self.player1.result())
        self.remainBead2Edit.setText(self.player2.result(self.name))

    def startBeadGame(self):
        self.choiceNumEdit.clear()
        self.round_Edit.setText(str(self.gameRound))
        self.messageEdit.setText(f"<<{self.gameRound}라운드>>")
        if self.gameRound % 2 == 1:  # 홀수 판: player2(사용자)-공격, player1(컴퓨터)-수비
            display = self.player1.messageOutput()  # player1이 수비자일 때 출력하는 메시지
        else:  # 짝수 판: player1(컴퓨터)-공격, player2(사용자)-공격
            display = self.player2.messageOutput()  # player2가 수비자일 때 출력하는 메시지
        self.messageEdit.append(display)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gm = SqGame()
    sys.exit(app.exec_())
