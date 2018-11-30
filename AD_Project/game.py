#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel

import time
import threading

from guess import Guess
#from endtoend import Endtoend


class EndtoendGame(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.guess = Guess()
        self.guess.test()
        #self.endtoend = Endtoend()

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('End-TO-End')

        # label

        self.status = QLabel("")
        self.status.setFixedHeight(30)
        self.status.setAlignment(Qt.AlignCenter)
        font1 = self.status.font()
        font1.setPointSize(13)
        self.status.setFont(font1)

        self.inputword = QLabel('단어입력 : ', self)


        # QLineEdit
        self.showword = QLineEdit()
        self.showword.setReadOnly(True)
        font1 = self.showword.font()
        font1.setPointSize(20)
        self.showword.setFont(font1)
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
        self.character.setText('')

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

        # QHbox1
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.airecord)
        hbox1.addStretch(1)
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
        vbox.addLayout(hbox1)
        vbox.addWidget(self.character)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)
        self.startGame()


    def startGame(self):
        firstword = self.guess.game_start()
        self.gameOver = False

        self.counter = 3
        self.myscore = 0
        self.yourscore = 0

        self.myrecord.setText(str(self.myscore))
        self.airecord.setText(str(self.yourscore))

        self.status.setText('게임을 시작합니다.')

        # 처음 시작할시 컴퓨터가 단어를 제시하도록 하는 부분
        self.showword.setText(firstword)

        if len(firstword) > 1:
            self.yourscore += len(firstword)*4

        self.airecord.setText(str(self.yourscore))
        self.writeword.clear()

    def pressedEnter(self):
        enterword = self.writeword.text()
        #returnword = ''
        self.writeword.clear()

        if len(enterword) > 1:
            self.myscore += len(enterword)*4

        self.myrecord.setText(str(self.myscore))

        # 예외처리
        if self.guess.starts(enterword[0]) == False:
            return self.status.setText('존재하지 않는 단어입니다.')

        if self.guess.isitin(enterword) == False:
            return self.status.setText('불가능합니다.')

        if self.guess.botsword(enterword) == False:
            return self.status.setText('존재하지 않는 단어입니다.')


        # 예외처리 끝난 후 메인 실행 코드

        # self.status.setText('상대방이 단어를 입력중입니다...')
        # time.sleep(1)
        # self.status.setText('상대방이 단어를 입력중입니다....')
        # time.sleep(2)
        # self.status.setText('상대방이 단어를 입력중입니다...')
        # time.sleep(1)
        if len(enterword) > 1:
            self.myscore += len(enterword)*4
        self.myrecord.setText(str(self.myscore))

        self.aiword = self.guess.botsword(enterword)
        self.showword.setText(self.aiword)

        if len(self.aiword) > 1:
            self.yourscore += len(self.aiword)*4

        self.airecord.setText(str(self.yourscore))
        self.status.setText('당신의 차례입니다.')


    # # 엔터 입력처리 메서드
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Space:
    #         print('Enter')
    #         self.pressedEnter()
    #     if event.key == Qt.Key_Escape:
    #         self.close()
    #
    # def count1(self):
    #     self.status.setText(str(self.counter))
    #     self.counter-=1
    #     threading.Timer(1,self.count1).start()


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = EndtoendGame()
    game.show()
    sys.exit(app.exec_())
