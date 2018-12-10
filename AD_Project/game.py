#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel, QMessageBox

import time
import threading

from guess import Guess
from endtoend import Endtoend


class EndtoendGame(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.guess = Guess()
        self.guess.test()
        self.endtoend = Endtoend()
        self.gameStart = False

        self.setGeometry(750, 300, 500, 400)
        self.setWindowTitle('End-TO-End')

        # label

        self.status = QLabel("")
        self.status.setFixedHeight(30)
        self.status.setAlignment(Qt.AlignCenter)
        font1 = self.status.font()
        font1.setPointSize(13)
        self.status.setFont(font1)

        self.inputword = QLabel('단어입력 : ', self)

        self.lastword = QLabel('이전 단어 : ', self)
        self.lastword.setFixedHeight(15)
        self.lastword.setAlignment(Qt.AlignCenter)
        font2 = self.lastword.font()
        font2.setPointSize(10)
        self.lastword.setFont(font2)

        self.showaipoint = QLabel('CPU 점수: ')
        font3 = self.showaipoint.font()
        font3.setPointSize(10)
        self.showaipoint.setFont(font3)

        self.showmypoint = QLabel('내 점수: ')
        font4 = self.showmypoint.font()
        font4.setPointSize(10)
        self.showmypoint.setFont(font2)

        # QLineEdit
        self.showword = QLineEdit()
        self.showword.setReadOnly(True)
        font5 = self.showword.font()
        font5.setPointSize(20)
        self.showword.setFont(font5)
        self.showword.setFixedHeight(50)
        self.showword.setFixedWidth(350)
        self.showword.setAlignment(Qt.AlignCenter)

        self.myrecord = QLineEdit()
        self.myrecord.setReadOnly(True)
        self.myrecord.setFixedHeight(30)
        self.myrecord.setAlignment(Qt.AlignCenter)

        self.airecord = QLineEdit()
        self.airecord.setReadOnly(True)
        self.airecord.setFixedHeight(30)
        self.airecord.setAlignment(Qt.AlignCenter)

        self.writeword = QLineEdit()
        self.writeword.setFixedHeight(40)
        self.writeword.setFixedWidth(200)
        self.writeword.setMaxLength(52)

        # QTextEdit
        self.character = QTextEdit()
        self.character.setReadOnly(True)
        self.character.setText(self.endtoend.text[0])

        # Button newGame
        self.newGame = QToolButton()
        self.newGame.setText('새 게임')
        self.newGame.clicked.connect(self.startGame)
        self.newGame.setFixedHeight(40)
        self.newGame.setFixedWidth(80)

        self.enter = QToolButton()
        self.enter.setText('Enter')
        self.enter.clicked.connect(self.pressedEnter)
        self.enter.setFixedHeight(40)

        # Message Box
        self.endmessage = QMessageBox()

        # QHbox1
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.showaipoint)
        hbox1.addWidget(self.airecord)
        hbox1.addStretch(1)
        hbox1.addWidget(self.showmypoint)
        hbox1.addWidget(self.myrecord)
        hbox1.addStretch(1)

        # QHbox2
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.showword)
        hbox2.addStretch(1)

        # QHbox3
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.inputword)
        hbox3.addWidget(self.writeword)
        hbox3.addWidget(self.enter)
        hbox3.addStretch(1)
        hbox3.addWidget(self.newGame)


        # QVbox
        vbox = QVBoxLayout()

        vbox.addWidget(self.status)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.lastword)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.character)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)
        self.startGame()

    def timeout(self):
        self.settime -= 1
        self.status.setText(str(self.settime))

        if self.settime == 0 and self.gameStart == False:
            self.settime = 15
            self.gameStart = True
            self.writeword.setDisabled(False)
        elif self.settime == 0 and self.gameStart == True:
            self.gameOver = True
            self.timer = None
            self.status.setText('Time Over')
            self.showword.setText(self.guess.botsword(self.firstword))
            self.enter.setDisabled(True)

            # 메세지박스 설정
            if self.yourscore > self.myscore:
                self.endmessage.setText('패배하셨습니다.')
            elif self.yourscore < self.myscore:
                self.endmessage.setText('승리하셨습니다!')
            elif self.yourscore == self.myscore:
                self.endmessage.setText('동점입니다!')
            self.endmessage.exec_()



    def startGame(self):
        # 타이머 초기화
        self.settime = 4
        self.maxtime = 15
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)
        self.timer.start(1000)
        self.gameStart = False
        self.enter.setDisabled(False)

        # 입력창 초기화
        self.writeword.setDisabled(True)
        self.character.setText(self.endtoend.text[0])
        self.myscore = 0
        self.yourscore = 0
        self.guess.usedword = []
        self.lastword.setText('이전 단어 : ')

        # 첫 단어 불러오기
        self.firstword = self.guess.game_start()

        # gameOver False 설정
        self.gameOver = False


        # 처음 시작할시 컴퓨터가 단어를 제시하도록 하는 부분
        self.showword.setText(self.firstword)
        self.guess.what_have_we_done(self.firstword)

        # if len(self.firstword) > 1:
        #     self.yourscore += len(self.firstword) * 4

        # 점수판 초기화된 점수 입력
        self.myrecord.setText(str(self.myscore))
        self.airecord.setText(str(self.yourscore))

        self.writeword.clear()
        self.status.setText('게임을 시작합니다.')



    def pressedEnter(self):
        self.usedword = self.guess.usedword
        self.settime = self.maxtime
        self.maxtime -= 1

        if self.settime == 0:
            self.gameOver = True
            self.status.setText('Time Over')

        enterword = self.writeword.text()
        self.writeword.clear()


        if len(enterword) > 1:
            print(1)
            # 예외처리

            if self.guess.isitin(enterword) == False:
                self.status.setText('불가능합니다.' + '2')
                print(3)

            elif self.guess.useingword(enterword) == False:
                self.status.setText('이미 사용한 단어입니다.')
                print(5)

            elif self.guess.botsword(enterword) == False:
                print(4)
                self.status.setText('존재하지 않는 단어입니다.')

            elif enterword in self.usedword:
                print(6)
                self.status.setText('이미 입력한 단어입니다.')

            elif self.showword.Text()[-1] != enterword[0]:
                self.status.setText("잘못된 입력입니다.")

            # 모든 오류 일어나지 않았을때 실행
            else:
                self.myscore += len(enterword) * 4
                self.myrecord.setText(str(self.myscore))
                last = self.guess.what_have_we_done(enterword)
                self.lastword.setText("이전 단어 : "+ ' - '.join(last))

                # 컴퓨터가 새로운 단어를 입력
                self.aiword = self.guess.botsword(enterword)
                self.showword.setText(self.aiword)

                self.yourscore += len(self.aiword) * 4

                self.guess.what_have_we_done(self.aiword)

                self.airecord.setText(str(self.yourscore))
                self.status.setText('당신의 차례입니다.')

                # 점수에 따라 character창의 점수가 바뀜
                if self.yourscore > self.myscore:
                    self.character.setText(self.endtoend.text[1])
                elif self.yourscore < self.myscore:
                    self.character.setText(self.endtoend.text[2])
                elif self.yourscore == self.myscore:
                    self.character.setText(self.endtoend.text[0])

        elif len(enterword) == 1:
            self.status.setText('2글자 이상 입력해주세요.')

        else:
            self.status.setText('공백은 입력할 수 없습니다.')


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = EndtoendGame()
    game.show()
    # timer = Timer()
    # timer.show()
    sys.exit(app.exec_())
