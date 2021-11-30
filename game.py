from guess import Guess
from player1 import Player1  # 컴퓨터
from player2 import Player2  # 사용자
import time


class gameMain():
    name = input("이름을 입력하세요: ")  # 이름
    number = input("참가번호를 입력하세요: ")  # 참가번호
    totalNumberOfBeads = int(input("플레이할 구슬의 수를 입력하세요: "))  # 총 구슬의 개수

    gameRound = 1  # 게임 판 수
    player1 = Player1(totalNumberOfBeads)  # 총 구슬의 개수 저장
    player2 = Player2(totalNumberOfBeads, name, number)
    guess = Guess()

    while 1:
        if gameRound % 2 == 1:  # 홀수 판이면 사용자가 공격
            selectedBeads = player1.randomNumberOfBeads()  # 플레이어1(수비자).랜덤으로 구슬 고르기
            print(f"<<{gameRound}라운드>> 공격자입니다.")
            display = player1.messageOutput()
            print(display)
            chosenEvenOdd = input()  # 사용자가 고른 홀/짝 String: "홀수" or "짝수"
            if guess.guess(selectedBeads, chosenEvenOdd):  # True면 = 사용자가 이겼으면
                player1.subBeads(selectedBeads)  # player1 구슬 개수 감소
                player2.addBeads(selectedBeads)  # player2 구슬 개수 증가
                display = f"""
                          player1은 {selectedBeads}개의 구슬을 선택했습니다.
                          {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 공격 성공입니다.
                          이번 판에서 {selectedBeads}개의 구슬을 얻었습니다.
                          """
                print(display)
                print("결과: ")
                p1Res = player1.currentBeadsDrawing()
                p2Res = player2.currentBeadsDrawing()
                print("player1 남은 공: " + p1Res)
                print(f"{name} 남은 공: " + p2Res)

                if guess.finished(player1.getNumOfBeads()):
                    print("승리입니다")
                    break
                else:
                    gameRound += 1
                    continue

            else:  # False라면 = 사용자가 졌다면
                player1.addBeads(selectedBeads * 2)  # player1 구슬 개수 감소
                player2.subBeads(selectedBeads * 2)  # player2 구슬 개수 증가
                display = f"""
                          player1은 {selectedBeads}개의 구슬을 선택했습니다.
                          {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 공격 실패입니다.
                          이번 판에서 {selectedBeads * 2}개의 구슬을 잃었습니다.
                          """
                print(display)
                print("결과: ")
                p1Res = player1.currentBeadsDrawing()
                p2Res = player2.currentBeadsDrawing()
                print("player1 남은 공: " + p1Res)
                print(f"{name} 남은 공: " + p2Res)

                if guess.finished(player2.getNumOfBeads()):
                    print("패배입니다")
                    break
                else:
                    gameRound += 1
                    continue


        else:  # 짝수 판이면 사용자가 수비자
            print(f"<<{gameRound}라운드>> 수비자입니다.")
            display = player2.messageOutput(name, number)
            print(display)
            selectedBeads = int(input())  # 사용자가 건 구슬 수
            chosenEvenOdd = player1.randomChooseOddEven()
            print("\t\tplayer1이 짝수/홀수를 고르는 중입니다. 잠시만 기다려주세요.")
            time.sleep(2)  # 2초 기다림

            if not guess.guess(selectedBeads, chosenEvenOdd):  # True면 = 사용자가 이겼으면
                player1.subBeads(selectedBeads * 2)  # player1 구슬 개수 감소
                player2.addBeads(selectedBeads * 2)  # player2 구슬 개수 증가
                display = f"""
                          당신은 {selectedBeads}개의 구슬을 선택했습니다.
                          player1은 {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 수비 성공입니다.
                          이번 판에서 {selectedBeads * 2}개의 구슬을 얻었습니다.
                          """
                print(display)
                print("결과: ")
                p1Res = player1.currentBeadsDrawing()
                p2Res = player2.currentBeadsDrawing()
                print("player1 남은 공: " + p1Res)
                print(f"{name} 남은 공: " + p2Res)

                if guess.finished(player1.getNumOfBeads()):
                    print("승리입니다")
                    break
                else:
                    gameRound += 1
                    continue

            else:  # False라면 = 사용자가 졌다면
                player1.addBeads(selectedBeads)  # player1 구슬 개수 감소
                player2.subBeads(selectedBeads)  # player2 구슬 개수 증가
                display = f"""
                          당신은 {selectedBeads}개의 구슬을 선택했습니다.
                          player1은 {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 수비 실패입니다.
                          이번 판에서 {selectedBeads}개의 구슬을 잃었습니다.
                          """
                print(display)
                print("결과: ")
                p1Res = player1.currentBeadsDrawing()
                p2Res = player2.currentBeadsDrawing()
                print("player1 남은 공: " + p1Res)
                print(f"{name} 남은 공: " + p2Res)

                if guess.finished(player2.getNumOfBeads()):
                    print("패배입니다")
                    break
                else:
                    gameRound += 1
                    continue


if __name__ == '__main__':
    gameMain()
