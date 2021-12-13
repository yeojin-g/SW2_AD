import sys
from guess import Guess
from player1 import Player1  # player1: 컴퓨터
from player2 import Player2  # player2: 사용자
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pygame


def musicApply(music):
    music_file = music
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)


# 버튼 생성 & 콜백함수 연결하는 클래스
class Button(QPushButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setText(text)
        self.clicked.connect(callback)


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
        musicApply("트럼펫 협주곡.mp3")

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
        gameRule = QLabel("\t" * 8 + """각 참가자들은 선택한 개수만큼 구슬을 가지고 시작합니다.
        수비자는 자신의 구슬 중 자신이 원하는만큼 손에 쥡니다.
        공격자는 수비자의 손에 쥐어진 구슬의 개수가 홀수인지, 짝수인지 맞춥니다.
        공격자가 홀짝 여부를 맞췄을 경우, 공격자는 수비자의 손에 쥐어진 모든 구슬을 갖게되고,
        공격자가 틀렸을 경우, 수비자에게 수비자가 쥐고있던 구슬의 2배만큼 주어야 합니다.
        공수교대는 한 턴마다 이루어지고, 구슬을 먼저 모두 잃게 되는 자가 게임에서 패배하게 됩니다.
        모든 참가자들은 게임에서 살아남지 못할 경우, 그 대가를 치르게 됩니다.
        진행요원들이 여러분을 항시 감시하고 있으니 반칙은 삼가해주시기 바랍니다.
        그럼 행운을 빕니다.""")

        # 게임 룰 글씨 가운데 정렬
        gameRule.setAlignment(Qt.AlignCenter)
        gameRuleTitle.setAlignment(Qt.AlignCenter)

        # 입출력창
        self.nameEdit = QLineEdit()
        self.ptcNumberEdit = QLineEdit()
        self.pickBeadNumEdit = QLineEdit()
        self.pickBeadNumEdit.setPlaceholderText("10개 이상, 15개 이하")
        self.ErrorEdit = QLineEdit()  # 에러메시지 적는 칸
        self.ErrorEdit.setReadOnly(True)
        self.ErrorEdit.setStyleSheet("color: rgb(233, 075, 134);")  # '오징어게임' 타이틀과 색상이 같게

        # 버튼 생성, 함수 연결
        self.nextButton = Button('Next Page!', self.settingInfo)

        # 열(hbox)과 위젯 이름(widget)을 받아서 addWidget, addStretch 하는 함수
        def addWidgetAndStretch(hbox, widget):
            hbox.addWidget(widget)
            hbox.addStretch(1)

        # 가로 1열 - 타이틀
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        addWidgetAndStretch(hbox1, title)

        # 가로 2열 - 이름, 참가번호
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(name)
        addWidgetAndStretch(hbox2, self.nameEdit)
        hbox2.addWidget(ptcNumber)
        addWidgetAndStretch(hbox2, self.ptcNumberEdit)

        # 가로 3열 - 구슬 개수
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.pickBeadNumEdit)
        addWidgetAndStretch(hbox3, pickBeadNum)

        # 가로 4열 - 게임룰 타이틀
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        addWidgetAndStretch(hbox4, gameRuleTitle)

        # 가로 5열 - 게임 설명문
        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        addWidgetAndStretch(5, gameRule)

        # 세로
        vbox = QVBoxLayout()
        vbox.addWidget(titleImgLabel)
        vboxL = [hbox1, hbox2, hbox3, hbox4, hbox5, self.ErrorEdit, self.nextButton]
        for i in range(0, len(vboxL)):
            if i > 4:
                vbox.addWidget(vboxL[i])
            else:
                vbox.addLayout(vboxL[i])
            vbox.addStretch(1)

        # 윈도우 위치 및 타이틀, 메인 레이아웃 설정
        self.setLayout(vbox)
        self.move(570, 220)
        self.setFixedSize(800, 600)
        self.setWindowTitle('구슬 게임')
        self.show()

    def next_clicked(self):
        pygame.mixer.quit()
        self.hide()  # 메인 윈도우 숨김
        self.second = SecGame()
        self.second.exec()  # 두번째 창 닫을 때까지 기다림
        self.show()  # 두번째 창 닫으면 첫 번째 창 보여짐
        musicApply('트럼펫 협주곡.mp3')  # 메인 창으로 돌아갔을 때 노래 재생
        pygame.mixer.music.set_volume(0.6)  # 음악 소리 조절

    def settingInfo(self):
        # 예외 처리
        if len(self.nameEdit.text()) == 0:  # 이름을 입력하지 않은 경우
            self.ErrorEdit.setText("이름을 입력해주십시오.")
        elif len(self.ptcNumberEdit.text()) == 0:  # 참가번호를 입력하지 않은 경우
            self.ErrorEdit.setText("참가번호를 입력해주십시오.")
        elif not self.ptcNumberEdit.text().isdecimal():  # 참가번호를 숫자로 입력하지 않은 경우
            self.ErrorEdit.setText("참가번호에는 숫자만 입력해주십시오.")
        elif len(self.pickBeadNumEdit.text()) == 0:  # 총 구슬의 개수를 입력하지 않은 경우
            self.ErrorEdit.setText("총 구슬의 개수를 입력해주십시오.")
        elif not self.pickBeadNumEdit.text().isdecimal():  # 총 구슬의 개수를 숫자로 입력하지 않은 경우
            self.ErrorEdit.setText("총 구슬의 개수는 숫자만 입력해주십시오.")
        elif not (10 <= int(self.pickBeadNumEdit.text()) <= 15):  # 제한된 구슬의 개수(10~15개)로 입력하지 않은 경우
            self.ErrorEdit.setText("총 구슬의 개수는 10에서 15까지의 숫자만 입력해주십시오.")
        else:
            Main.name = self.nameEdit.text()
            Main.playerNum = self.ptcNumberEdit.text()
            Main.beadNum = int(self.pickBeadNumEdit.text())
            self.ErrorEdit.clear()  # 에러 메시지 삭제
            self.next_clicked()  # 다음 창으로 넘어가는 함수


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
        self.oddOrEven = None  # 사용자가 공격하는 경우, 즉 홀수판의 경우 사용자가 홀/짝 중 고른 것을 저장하는 변수
        musicApply('오징어게임 리코더.mp3')  # 음악 플레이
        pygame.mixer.music.set_volume(0.2)  # 음악 소리 조절
        self.disableSetting()  # 처음에 버튼을 비활성화, lineEdit read only로 만드는 함수

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
        app.setFont(QFont('나눔손글씨 할아버지의나눔', 13))

    def initUI(self):
        # 이미지
        titleImgLabel = QLabel(self)  # 오징어게임 타이틀 이미지 라벨
        titleImg = QPixmap('./title.png')  # 오징어게임 타이틀 이미지
        titleImg = titleImg.scaledToWidth(200)  # 이미지 사이즈 조정
        titleImgLabel.setPixmap(titleImg)  # 라벨과 연결
        titleImgLabel.setAlignment(Qt.AlignCenter)  # 가운데 정렬

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

        # 버튼 생성, 함수 연결
        self.backButton = Button('Back', self.BackButtonClicked)
        self.startButton = Button('Game Start', self.startButtonClicked)
        self.oddNumButton = Button('홀', self.oddOrEvenButtonClicked)
        self.evenNumButton = Button('짝', self.oddOrEvenButtonClicked)
        self.enterEventButton = Button('Enter', self.enterEventButtonClicked)
        self.restartButton = Button('Restart', self.restartButtonClicked)

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
        grid1_2.addWidget(self.startButton, 0, 0, 1, 1)
        grid1_2.addWidget(choiceNum, 1, 0, 1, 1)
        grid1_2.addWidget(self.choiceNumEdit, 2, 0, 1, 1)
        grid1_2.addLayout(hboxB, 3, 0, 1, 2)
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

        # 레이아웃, 사이즈, 윈도우 이름 설정
        self.setLayout(grid)
        self.move(600, 150)
        self.setFixedSize(700, 700)
        self.setWindowTitle('구슬 게임')
        self.show()

        # 게임 시작버튼을 누르라는 메시지 출력
        self.messageEdit.setText("게임을 시작할까?\n그렇다면 Game Start 버튼을 누르게.")

    def disableSetting(self):  # 홀수버튼, 짝수버튼, enter버튼 비활성화
        self.oddNumButton.setDisabled(True)
        self.evenNumButton.setDisabled(True)
        self.enterEventButton.setDisabled(True)
        self.choiceNumEdit.setReadOnly(True)

    def BackButtonClicked(self):  # Back 버튼 눌렀을 때 함수
        pygame.mixer.quit()
        self.close()  # 창 닫기
        self.close()  # 창 닫기

    def oddOrEvenButtonClicked(self):
        sender = self.sender()  # 클릭된 버튼을 sender에 저장
        if sender.text() == "홀":
            self.oddOrEven = "홀수"
        else:
            self.oddOrEven = "짝수"
        self.enterEventButton.setDisabled(False)  # enter 버튼 활성화

    def enterEventButtonClicked(self):  # gameRound의 홀/짝에 따라 다른 함수 실행하게 함
        if self.gameRound % 2 == 1:  # 홀수판이면
            self.guessWhenRoundOdd(self.oddOrEven)
        else:
            self.guessWhenRoundEven()

    def sleep(self, n):  # n초간 대기하는 함수
        loop = QEventLoop()
        QTimer.singleShot(n * 1000, loop.quit)
        loop.exec_()

    def printMessage(self, list):  # 메세지 리스트 프린트 함수
        self.showInfo()
        for i in list:
            self.messageEdit.setText(i)
            self.sleep(2)

    def beadNumControl(self, winner, loser, beadNum):  # 게임 결과에 맞게 구슬 개수 조절하는 함수
        changeBead = beadNum
        if changeBead > loser.getNumOfBeads():
            changeBead = loser.getNumOfBeads()
        winner.addBeads(changeBead)  # winner 구슬 개수 증가
        loser.subBeads(changeBead)  # loser 구슬 개수 감소

    def guessWhenRoundOdd(self, answer):  # 홀수판 / player1(컴퓨터): 수비자, player2(사용자): 공격자
        selectedBeads = self.player1.randomNumberOfBeads()  # player1(컴퓨터)-수비자.랜덤으로 구슬 고르기
        if self.guess_Ob.guess(selectedBeads, answer):  # True일 때 = 사용자가 이겼을 때
            self.beadNumControl(self.player2, self.player1, selectedBeads)  # 결과에 맞게 구슬 개수 조정
            # 메세지 출력 리스트
            display = [
                f"자, 나는 {selectedBeads}개를 쥐었었네.\n자네가 {answer}라고 했으니, 참가번호 {Main.playerNum}번 {Main.name},\n자네의 공격이 먹혔구만.\n여기 {selectedBeads}개의 구슬을 주겠네.",
                "이런, 내 구슬을 다 잃었구만..!\n괜찮네. 다 가져, 자네꺼야. 우린 깐부잖아.\n게임을 더 하고 싶으면 restart 버튼을 누르면 되네.", ]
            if self.guess_Ob.finished(self.player1.getNumOfBeads()):  # player1가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 승리)
                self.printMessage(display)
                self.startButton.setDisabled(True)  # 게임이 끝났으므로 start game 버튼 비활성화
            else:  # 계속 게임 진행
                self.printMessage(display[:1])
                self.gameRound += 1
                self.messageEdit.append("\n다음 판을 할 준비가 됐나?\n됐다면 Game Start 버튼을 누르게.")

        else:  # False = 사용자가 졌다면
            self.beadNumControl(self.player1, self.player2, selectedBeads * 2)  # 결과에 맞게 구슬 개수 조정
            # 메세지 출력 리스트
            display = [
                f"자, 나는 {selectedBeads}개를 쥐었었네.\n자네가 {answer}라고 했으니\n이런! 참가번호 {Main.playerNum}번 {Main.name},\n자네가 졌구만. 허허.\n어서 {selectedBeads * 2}개의 구슬을 나에게 주게.",
                "아니, 설마 자네 구슬을 다 잃은겐가?\n너무 그렇게 보지 말게나. 우린 깐부잖아~\n게임을 더 하고 싶으면 restart 버튼을 누르면 되네.", ]
            if self.guess_Ob.finished(self.player2.getNumOfBeads()):  # player2가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 패배)
                self.printMessage(display)
                self.startButton.setDisabled(True)  # 게임이 끝났으므로 start game 버튼 비활성화
            else:  # 계속 게임 진행
                self.printMessage(display[:1])
                self.gameRound += 1
                self.messageEdit.append("\n다음 라운드로 가보자고!\nGame Start 버튼을 누르게.")
        self.oddOrEven = None  # 홀짝 정보 초기화
        self.disableSetting()  # 홀/짝/enter 버튼, 구슬 line edit 비활성화

    def guessWhenRoundEven(self):  # 짝수판 / player1(컴퓨터): 공격자, player2(사용자): 수비자
        # 예외처리
        if not self.choiceNumEdit.text().isdecimal():  # 숫자를 입력하지 않았을 때
            self.messageEdit.setText("어허, 올바른 값을 입력하게나~")
            self.choiceNumEdit.clear()
            return
        if int(self.choiceNumEdit.text()) > self.player2.getNumOfBeads():  # 가지고 있는 구슬의 수보다 큰 수를 입력했을 때
            self.messageEdit.setText("자네가 구슬이 그렇게 많았었나~?")
            self.choiceNumEdit.clear()
            return
        if int(self.choiceNumEdit.text()) == 0:  # 구슬의 개수가 0 또는 음수일 때
            self.messageEdit.setText("0보다 큰 수를 골라야하지 않겠나!")
            self.choiceNumEdit.clear()
            return

        selectedBeads = int(self.choiceNumEdit.text())  # 사용자가 건 구슬 수
        chosenEvenOdd = self.player1.randomChooseOddEven()  # player1(컴퓨터)-수비자. 홀수, 짝수 둘 중 하나 랜덤으로 고르기
        display = "잠깐.. 고민할 시간을 좀 주게나.."
        self.messageEdit.setText(display)
        self.sleep(2)  # 문구를 볼 수 있도록 2초 대기

        if not self.guess_Ob.guess(selectedBeads, chosenEvenOdd):  # 사용자가 이겼을 때
            self.beadNumControl(self.player2, self.player1, selectedBeads * 2)  # 결과에 맞게 구슬 개수 조정
            # 프린트할 메세지 리스트
            display = [f"흠, 자네는 {selectedBeads}개를 쥐고있었구만.\n내가 방금 뭐라 그랬더라..?",
                       f"아, 나는 {chosenEvenOdd}라 했네!\n이런! 참가번호 {Main.playerNum}번 {Main.name}, 자네가 수비에 성공했구만. \n여기 {selectedBeads * 2}개의 구슬을 주지.",
                       "이런, 내 구슬을 다 잃었구만..!\n괜찮네. 다 가져, 자네꺼야. 우린 깐부잖아.\n게임을 더 하고 싶으면 restart 버튼을 누르면 되네.", ]

            # player1이 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 승리)
            if self.guess_Ob.finished(self.player1.getNumOfBeads()):
                self.printMessage(display)  # 메세지 프린트 함수
                self.startButton.setDisabled(True)  # 게임이 끝났으므로 start game 버튼 비활성화
            else:  # 계속 게임 진행
                self.printMessage(display[:2])  # 메세지 프린트 함수
                self.gameRound += 1
                self.messageEdit.append("\n다음 라운드로 가보자고!\nGame Start 버튼을 누르게.")

        else:  # False라면 = 사용자가 졌다면
            self.beadNumControl(self.player1, self.player2, selectedBeads)  # 결과에 맞게 구슬 개수 조정
            # 프린트할 메세지 리스트
            display = [f"흠, 자네는 {selectedBeads}개를 쥐고있었구만.\n내가 방금 뭐라 그랬더라..?",
                       f"아, 나는 {chosenEvenOdd}라 했네!\n허허! 참가번호 {Main.playerNum}번 {Main.name}, 자네가 졌구만!\n어서 {selectedBeads}개의 구슬을 나에게 주게.",
                       "아니, 설마 자네 구슬을 다 잃은겐가?\n너무 그렇게 보지 말게나. 우린 깐부잖아~\n게임을 더 하고 싶으면 restart 버튼을 누르면 되네.", ]
            if self.guess_Ob.finished(self.player2.getNumOfBeads()):  # player2가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 패배)
                self.printMessage(display)
                self.startButton.setDisabled(True)  # 게임이 끝났으므로 start game 버튼 비활성화
            else:  # 계속 게임 진행
                self.printMessage(display[:2])
                self.gameRound += 1
                self.messageEdit.append("\n다음 판을 할 준비가 됐나?\n됐다면 Game Start 버튼을 누르게.")
        self.disableSetting()  # 홀/짝/enter 버튼, 구슬 line edit 비활성화

    # 현재 가지고 있는 구슬을 보여주는 함수
    def showInfo(self):
        self.remainBead1Edit.setText(self.player1.result())
        self.remainBead2Edit.setText(self.player2.result(self.name))

    def startButtonClicked(self):
        self.choiceNumEdit.clear()
        self.round_Edit.setText(str(self.gameRound))
        self.messageEdit.setText(f"<<{self.gameRound}라운드>>")
        if self.gameRound % 2 == 1:  # 홀수 판: player2(사용자)-공격, player1(컴퓨터)-수비
            display = self.player1.messageOutput()  # player1이 수비자일 때 출력하는 메시지
            self.oddNumButton.setEnabled(True)  # 홀수 버튼 활성화
            self.evenNumButton.setEnabled(True)  # 짝수 버튼 활성화
        else:  # 짝수 판: player1(컴퓨터)-공격, player2(사용자)-공격
            display = self.player2.messageOutput()  # player2가 수비자일 때 출력하는 메시지
            self.choiceNumEdit.setReadOnly(False)  # 게임에 걸 구슬의 개수 write 가능
            self.enterEventButton.setDisabled(False)  # enter 버튼 활성화
        self.messageEdit.append(display)

    def restartButtonClicked(self):
        # 객체 및 변수 설정
        self.player1 = Player1(Main.beadNum)
        self.player2 = Player2(Main.beadNum, Main.name, Main.playerNum)
        self.guess_Ob = Guess()
        self.gameRound = 1
        self.showInfo()  # 구슬의 개수 정보를 보여줌
        self.startButton.setDisabled(False)  # 재시작했으므로 Game start버튼 활성화
        self.disableSetting()  # 처음에 버튼을 비활성화, lineEdit read only로 만드는 함수

        # 재시작을 알리는 문구 출력
        display = "다시 시작해보자고!"
        self.messageEdit.setText(display)
        self.sleep(2)  # 문구를 볼 수 있도록 2초 대기
        self.startButtonClicked()  # 재시작


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gm = SqGame()
    sys.exit(app.exec_())
