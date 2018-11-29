from AD_Project.word import Word

import random


class Guess:
    def __init__(self):
        print("Word_data_Based_on : . https://github.com/KKuTu-Korea/KKuTu")
        print("-----------------------------------------------------------")
        self.word = Word()
        self.words = {}  # 단어 dict

    def test(self):
        self.words = self.word.readingdb()

    def starts(self, charactor):  # dict 안에 해당되는 key 값(charactor)이 있는지 확인하는 메소드 return type 단어장에 있는
        # 단어를 파악하는 것이 아닌 해당 단어로 시작하는 단어를 가져온다
        wordex = []
        if len(charactor) < 1:
            pass
        else:
            if charactor[0] in self.words:
                for i in range(10):
                    wordex += [(self.words[charactor][i])]
                return wordex
            else:
                return False

    def isitin(self, m):  # 입력한 단어가 단어장에 있는지 확인 하는 메소드 return type : Boolean
        k = m  # 단어가 없으면 False 리턴
        if k in self.words[k[0]]:
            return m
        else:
            return False

    def botsword(self, charactors):  #상대(컴퓨터)가 쓸 단어를 선택하는 메소드, 할 수 있는 단어가 없으면 False 리턴
        charactor = charactors[-1]
        if charactor in self.words:
            number = random.randint(1, len(self.words[charactor]))
            botword = (self.words[charactor])[number]
            return botword
        elif charactor not in self.words:
            return False


# --------------------------------작동 확인 영역----------------------------------

B = Guess()

B.test()

testword = "가가린"
success = B.starts('가')
seccscs = B.isitin(testword)

starttest = B.starts("가")
if not starttest:
    print("단어가 없습니다.")
else:
    print(starttest)
if seccscs is False:
    print("seccscs: 불가능 ㅠ")

else:
    print(testword)

if not success:
    print("success: 불가능 ㅠ")
else:
    print("success: 가능")

BOTTEST = B.botsword('군귋')
if BOTTEST is False:
    print("단어가 없습니다")
elif BOTTEST is not False:
    print(BOTTEST)
