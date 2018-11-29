#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel

import time

from AD_Project.guess import Guess

class EndtoendGame(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.guess = Guess()

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('End-TO-End')

        # label

        self.status = QLabel("초")
        self.status.setFixedHeight(30)
        self.status.setAlignment(Qt.AlignCenter)

        self.inputword = QLabel('단어입력 : ', self)


        # QLineEdit
        self.showword = QLineEdit()
        self.showword.setReadOnly(True)
        self.showword.setFixedHeight(50)
        self.showword.setFixedWidth(350)

        self.myrecord = QLineEdit()
        self.myrecord.setReadOnly(True)
        self.myrecord.setFixedHeight(30)

        self.airecord = QLineEdit()
        self.airecord.setReadOnly(True)
        self.airecord.setFixedHeight(30)

        self.writeword = QLineEdit()
        self.writeword.setFixedHeight(40)
        self.writeword.setFixedWidth(200)

        # QTextEdit
        self.character = QTextEdit()
        self.character.setReadOnly(True)

        # Button newGame
        self.newGame = QToolButton()
        self.newGame.setText('새 게임')
        self.newGame.clicked.connect(self.startGame)
        self.newGame.setFixedHeight(40)
        self.newGame.setFixedWidth(80)

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

        self.status.setText('게임을 시작합니다.')
        self.myrecord = 0
        self.airecord = 0
        self.character.setText('')
        time.sleep(1)
        self.status.setText('3')
        time.sleep(1)
        self.status.setText('2')
        time.sleep(1)
        self.status.setText('1')
        time.sleep(1)
        # 처음 시작할시 컴퓨터가 단어를 제시하도록 하는 부분
        self.showword.setText(firstword)
        self.character.setText('')
        self.writeword.clear()

    def pressedEnter(self):
        enterword = self.writeword.text()
        returnword = ''
        self.writeword.clear()

        # 예외처리
        if self.guess.isitin(enterword) == False:
            return self.status.setText('존재하지 않는 단어입니다.')


        # 예외처리 끝난 후 메인 실행 코드
        self.status.setText('상대방이 단어를 입력중입니다...')
        time.sleep(1)
        self.status.setText('상대방이 단어를 입력중입니다....')
        time.sleep(2)
        self.status.setText('상대방이 단어를 입력중입니다...')
        time.sleep(1)
        self.showword.setText(self.guess.botsword(enterword))
        self.status.setText('당신의 차례입니다.')
        time.sleep(1)


    # 엔터 입력처리 메서드
    def keyPressEvent(self, enter):
        if enter.key() == Qt.Key_Enter:
            self.pressEnter()


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = EndtoendGame()
    game.show()
    sys.exit(app.exec_())