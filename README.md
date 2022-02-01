# redowl
Perhaps you've played Wordle (https://www.powerlanguage.co.uk/wordle/) - well, `redowl` is a Wordle clone for python. 

# design / TODO 

- Let user set up parameters of the game 
  - [d]ebug mode should print the answer before playing 
  - [r]andom mode should not standardize the seed 
  - [s]eed should let users specify a seed 
  - [f]ile should let you use any input file 
  - [l]ength should allow users to choose a new word length 
- Get a list of valid words 
  - Import wordlist.txt [X]
  - Import arbitrary file
  - Strip out words of length != "L"
  - Tell user how many words are left (for large L or pre-trimmed lists, could be unwinnable/unfun)
- Choose a good word 
  - Choose randomly based on today's seed 
  - Later: Investigate whether removing simple plurals from the dictionary helps to devalue `S` and make the game more fun 
  - Later: use a repeatable seed e.g. UTC rounded to the hour (?), modulo number of entries in wordlist.txt
  - Later: display the repeatable seed so others can play the same game
  - Later: choose words with statistically unusual properties 
- Accept user input 
  - Only letters, no numeric / specials  
  - Check whether user input is 5 letters long [X]
  - Check whether user input is in dictionary [X]
- Evaluate & respond to user input
  - For each letter n in user input:
   - If userguess[n] is chosenword[n] color that letter green [X]
   - If userguess[n] appears in chosenword, color that letter yellow [X]
   - Otherwise color that letter dark grey [X]
  - Later: display a QWERTY layout showing which letters are in / out 
  - Later: display a “grade” for the guess, showing how many words the guess eliminated 
- Show output [X]

