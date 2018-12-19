import time

class Word():
    def __init__(self):
        self.dictword = {}

    def readingdb(self):
        #  Wordlist Encoding Type : UTF-8
        fh = open("Wordlist.txt", "r", encoding = 'UTF8')
        #word = fh.readlines()
        word = fh.read().splitlines()
        fh.close()

        # Making a dict
        for i in word:
            i = i.rstrip()
            self.dictword[i[0]] = []
        for i in word:
            self.dictword[i[0]] += [i]
        return self.dictword

        # Check for dict
#         fh = open("Temp.txt", "w")
#         fh.write(str(self.dictword))
#         fh.close()
#
#
# Test Place
# a = Word()
# a.readingdb()
