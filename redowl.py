#!/usr/bin/python3

class Wordle(object):
    def __init__(self, length=5):
        self.length = length
        self.score = [0, 0, 0, 0, 0]
        self.isSolved = False
        self.wordbank = []
        self.word = ""
        return

    def fromFile(self, filename):   
        # TODO: "filename" probably needs to be a Path or Pathlike object for robustness 
        with open(filename,'r') as fh:
            self.wordbank = fh.readlines()
        return

    def eval(self, guess):
        for i in range(self.length):
            if guess[i] == self.word[i]: # 2 for a letter which is correctly placed 
                self.score[i] = 2
            elif guess[i] in self.word:  # 1 for a letter which appears in a different position
                self.score[i] = 1
            else:                        # 0 for a letter which does not appear
                self.score[i] = 0
        if self.score == [2, 2, 2, 2, 2]:
            self.isSolved = True
        return

    def printscore(self):
        # TODO: look up those damn ANSI format incantations 
        # print an all-caps letter in gray for a score of 0
        # print an all-caps letter in yellow for a score of 1
        # print an all-caps letter in green for a score of 2
        return

def sanitize(self, string):
    newstring = string.strip(" ").lower()
    return newstring

def main():
    length = 5
    w = Wordle(length)
    w.fromFile('wordlist.txt')
    guess = ""
    tries = 0
    while not w.isSolved:
        guess = input().sanitize()
        # TODO: check length *after* sanitizing 
        if guess in w.wordbank:
            w.eval(guess)
            w.printscore()
            tries += 1
        elif len(guess) != length:
            print("No Guess (wrong length)")
        else:
            print("No Guess (not in our word bank)")
    return


if __name__ == "__main__":
    main()
