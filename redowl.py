#!/usr/bin/python3
import click
import random
import datetime

class Wordle(object):
    def __init__(self, seed, length=5):
        self.length = length
        self.seed = seed
        self.score = [0, 0, 0, 0, 0]
        self.isSolved = False
        self.wordbank = []      # "Wordbank" is words that can be the answer 
        self.dictionary = []    # "Dictionary" is words that are legal to guess 
        self.word = ""
        return

    def fromFiles(self, bankfile="valid.txt", dictfile="canon.txt"):   
        self.wordbank = [line.rstrip() for line in open(bankfile)]
        self.dictionary = [line.rstrip() for line in open(dictfile)]
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

@click.command()
# TODO: run in "Canonical" mode where it chooses the same word as the official web app 
#@click.option('-c', '--canon', is_flag=True, default=False)
@click.option('-d', '--debug', is_flag=True, default=False)
@click.option('-f', '--file', default='valid.txt')
@click.option('-l', '--length', default=5, type=int)
@click.option('-r', '--random', is_flag=True, default=False)
@click.option('-s', '--seed', type=int)
def main(debug, file, length, random, seed):

    # Initialize the game 
    if not seed:
        now = datetime.datetime.now()
        if not random:
            seed = int((((now.year - 2000)*365) + now.month*12 + now.day) % 65535) # One unique seed each day
            print("Today's seed: #{}".format(seed))
        else:
            seed = int((now.year * now.second + now.minute * now.hour + now.second * 16381) % 65535)
            print("Random seed selected: #{}".format(seed))
    w = Wordle(seed, length)
    w.fromFiles('valid.txt', 'canon.txt')
    guess = ""
    tries = 0

    # Play the game 
    if debug:
        click.echo("DEBUG: the word for Seed #{} is {}".format(w.seed, w.word.upper()))
    while not w.isSolved:
        guess = input().strip("").lower()
        # TODO: check length *after* sanitizing 
        if guess in w.dictionary:
            w.eval(guess)
            tries += 1
        elif len(guess) != length:
            click.echo("No Guess (wrong length)")
        else:
            click.echo("No Guess (not in our dictionary)")
    click.echo("You Win! The word was \x1b[1;32;40m{}\x1b[0m! It only took you {} tries.".format(w.word.upper(), tries))
    click.echo("This was seed #{} -- you can replay this level using the '-s' command line flag.".format(seed))
    return


if __name__ == "__main__":
    main()
