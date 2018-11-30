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

        self.lastword = QLabel('이전 단어 : ', self)
        self.lastword.setFixedHeight(15)
        self.lastword.setAlignment(Qt.AlignCenter)
        font2 = self.lastword.font()
        font2.setPointSize(10)
        self.lastword.setFont(font2)


        # QLineEdit
        self.showword = QLineEdit()
        self.showword.setReadOnly(True)
        font3 = self.showword.font()
        font3.setPointSize(20)
        self.showword.setFont(font3)
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
        vbox.addWidget(self.lastword)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.character)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)
        self.startGame()


    def startGame(self):
        firstword = self.guess.game_start()
        self.gameOver = False
        #self.character.setText(self.)
        self.counter = 3
        self.myscore = 0
        self.yourscore = 0

        self.myrecord.setText(str(self.myscore))
        self.airecord.setText(str(self.yourscore))

        self.status.setText('게임을 시작합니다.')

        # 처음 시작할시 컴퓨터가 단어를 제시하도록 하는 부분
        self.showword.setText(firstword)
        self.guess.what_have_we_done(firstword)

        if len(firstword) > 1:
            self.yourscore += len(firstword)*4

        self.airecord.setText(str(self.yourscore))
        self.writeword.clear()

    def pressedEnter(self):
        enterword = self.writeword.text()
        #returnword = ''
        self.writeword.clear()
        #self.lastword.setText('이전 단어 : ', thirdword[0], thirdword[1], thirdword[2])

        # 예외처리
        if self.guess.starts(enterword[0]) == False:
            self.myscore -= len(enterword)*4
            return self.status.setText('존재하지 않는 단어입니다.')

        if self.guess.isitin(enterword) == False:
            self.myscore -= len(enterword) * 4
            return self.status.setText('불가능합니다.')

        if self.guess.botsword(enterword) == False:
            self.myscore -= len(enterword) * 4
            return self.status.setText('존재하지 않는 단어입니다.')

        if len(enterword) > 1:
            self.myscore += len(enterword)*4
        self.myrecord.setText(str(self.myscore))
        self.guess.what_have_we_done(enterword)

        # 컴퓨터가 새로운 단어를 입력
        self.aiword = self.guess.botsword(enterword)
        self.showword.setText(self.aiword)

        if len(self.aiword) > 1:
            self.yourscore += len(self.aiword)*4

        self.guess.what_have_we_done(self.aiword)

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
