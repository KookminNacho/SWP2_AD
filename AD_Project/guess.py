from Word import Word

import random


class Guess:
    def __init__(self):
        print("Word_data_Based_on : . https://github.com/KKuTu-Korea/KKuTu")
        print("-----------------------------------------------------------")
        self.word = Word()
        self.words = {}  # 단어 dict
        self.thirdword = ['', '', '']
        self.usedword = []

    def test(self):
        self.words = self.word.readingdb()

    def useingword(self, character):
        if character not in self.usedword:
            return True
        else:
            return False

    def isitin(self, m):  # 입력한 단어가 단어장에 있는지 확인 하는 메소드 return type : Boolean
        k = m  # 단어가 없으면 False 리턴
        if k in self.words[k[0]]:
            return m
        else:
            return False

    def botsword(self, charactors):  # 상대(컴퓨터)가 쓸 단어를 선택하는 메소드, 할 수 있는 단어가 없으면 False 리턴
        charactor = charactors[-1]
        if charactor in self.words:
            number = random.randint(1, len(self.words[charactor])-1)
            botword = (self.words[charactor])[number]
            return botword
        elif charactor not in self.words:
            return False

# 준혁아 guess 파일에 게임 처음 시작됬을때 컴퓨터가 제시가는 단어 뽑아주는 메서드 firstword 하나만 더 만들어주라!
    def game_start(self):
        while 1:
            numb = random.randint(ord('가'), ord('힣'))
            if chr(numb) in self.words:
                randnum = random.randint(0, len(self.words[chr(numb)])-1)
                if len(self.words[chr(numb)][randnum]) > 1:
                    wordx = self.words[chr(numb)][randnum]
                    return wordx
                else:
                    pass
            else:
                pass

    def what_have_we_done(self, wordnow):  # 사용자가 컴퓨터가 사용한 단어를 받아와 텍스트로 최대 3개까지 출력
        self.thirdword[2], self.thirdword[1] = self.thirdword[1], self.thirdword[0]
        self.thirdword[0] = wordnow
        self.usedword.append(wordnow)
        return self.thirdword

# --------------------------------Unit test----------------------------------


if __name__ == '__main__':
    B = Guess()
    B.test()
    wordlist = ['군견', '감성', '토끼', "끼룩끼룩", "안전", "암뤟"]

    print("--------------------isitin()Test----------------------")
    for i in wordlist:  # isitin 메소드 테스트
        testword = i
        seccscs = B.isitin(testword)

        if seccscs is False:
            print(i, "단어장에서 찾을 수 없음.")
        else:
            print("isitin 메소드:", seccscs)

    print("------------------game_start()Test------------------")
    for i in range(6):
        print("시작 단어:", B.game_start())

    print("-------------------botsword()Test-------------------")
    for i in wordlist:
        BOTTEST = B.botsword(i)
        if BOTTEST is False:
            print(i[-1], "으로 시작하는 단어가 없습니다")
        elif BOTTEST is not False:
            print(i[-1], '으로 시작하는 단어:', BOTTEST)
    print("------------------Usedword()Test--------------------")
    for i in range(3):
        B.usedword.append(wordlist[i])
    for i in wordlist:
        if i in B.usedword:
            print("이미 사용한 단어:", i)
        else:
            print("사용하지 않은 단어:", i)

    print("-----------------what_have_we_done()------------------")
    count = 0
    for i in wordlist:
        count += 1
        word = B.what_have_we_done(i)
        print(count, "번째 차례", word)
