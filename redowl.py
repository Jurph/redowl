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

    def eval(self, word):
        # set self.score based on positional letters
        # 0 for a letter which does not appear
        # 1 for a letter which appears in a different position
        # 2 for a letter which is correctly placed 
        if self.score == [2, 2, 2, 2, 2]:
            self.isSolved = True
        return

    def printscore(self):
        # print an all-caps letter in gray for a score of 0
        # print an all-caps letter in yellow for a score of 1
        # print an all-caps letter in green for a score of 2
        return


def main():
    w = Wordle(5)
    w.fromFile('wordlist.txt')
    while not w.isSolved:
        guess = input()
        w.eval(guess)
        w.printscore()
    return


if __name__ == "__main__":
    main()
