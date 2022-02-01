#!/usr/bin/python3
import random
import datetime

class Wordle(object):
    def __init__(self, length=5, seed = 420):
        self.length = length
        self.seed = seed
        self.score = [0, 0, 0, 0, 0]
        self.isSolved = False
        self.wordbank = []
        self.word = ""
        return

    def fromFile(self, filename):   
        # TODO: "filename" probably needs to be a Path or Pathlike object for robustness 
        with open(filename,'r') as fh:
            self.wordbank = fh.readlines()

        random.seed(self.seed)
        self.word = random.choice(self.wordbank)
        return

    def eval(self, guess):
        scorestring = ""
        yellow = '\x1b[1;33;40m'
        green = '\x1b[1;32;40m'
        dim = '\x1b[1;30;40m'
        end = '\x1b[0m'
        for i in range(self.length):
            if guess[i] == self.word[i]: # 2 for a letter which is correctly placed 
                self.score[i] = 2
                scorestring += green + guess[i].upper() + end
            elif guess[i] in self.word:  # 1 for a letter which appears in a different position
                self.score[i] = 1
                scorestring += yellow + guess[i].upper() + end
            else:                        # 0 for a letter which does not appear
                self.score[i] = 0
                scorestring += dim + guess[i].upper() + end
        print(scorestring)
        if self.score == [2, 2, 2, 2, 2]:
            self.isSolved = True

        return

def sanitize(self, string):
    newstring = string.strip(" ").lower()
    return newstring

def main():
    # TODO: accept command line args for initialization
    # -d    : debug, prints answer up front
    # -f    : fast, seeds random with (day,hour,minute,second) precision 

    # Initialize the game 
    now = datetime.datetime.now()
    seed = now.day
    length = 5
    w = Wordle(length, seed)
    w.fromFile('wordlist.txt')
    guess = ""
    tries = 0

    # Play the game 
    while not w.isSolved:
        guess = input().sanitize()
        # TODO: check length *after* sanitizing 
        if guess in w.wordbank:
            w.eval(guess)
            tries += 1
        elif len(guess) != length:
            print("No Guess (wrong length)")
        else:
            print("No Guess (not in our word bank)")
    return


if __name__ == "__main__":
    main()
