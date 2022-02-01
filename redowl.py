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
        self.wordbank = [line.rstrip() for line in open(filename)]
        print("Initializing word bank... there are {} valid words.".format(len(self.wordbank)))
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
    # -f    : file, accepts an input dictionary other than the standard one 
    # -r    : random, forces the game not to use today's seed 
    # -s    : seed, forces a specific puzzle number (???)
    # -l    : length, lets you use a different word length 

    # Initialize the game 
    now = datetime.datetime.now()
    seed = now.day
    length = 5
    w = Wordle(length, seed)
    w.fromFile('5letters.txt')
    guess = ""
    tries = 0

    # Play the game 
    while not w.isSolved:
        guess = input().strip("").lower()
        # TODO: check length *after* sanitizing 
        if guess in w.wordbank:
            w.eval(guess)
            tries += 1
        elif len(guess) != length:
            print("No Guess (wrong length)")
        else:
            print("No Guess (not in our word bank)")
    print("You Win! The word was \x1b[1;32;40m{}\x1b[0m! It only took you {} tries.".format(w.word.upper(), tries))
    return


if __name__ == "__main__":
    main()
