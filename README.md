# redowl
Perhaps you've played Wordle (https://www.powerlanguage.co.uk/wordle/) - well, `redowl` is a Wordle clone for python. 

# design / TODO 

- Get a list of valid words 
  - Import wordlist.txt 
  - Strip out words of length != 5
  - Save the resulting list as `5letters.txt`
  - Easy on-the-way target: split the dictionary up by length and save `Nletters` for N = 3 to 8
- Choose a good word 
  - Choose randomly
  - Later: Investigate whether removing simple plurals from the dictionary helps to devalue `S` and make the game more fun 
  - Later: use a repeatable seed e.g. UTC rounded to the hour (?), modulo number of entries in wordlist.txt 
  - Later: display the repeatable seed so others can play the same game
  - Later: choose words with statistically unusual properties 
- Accept user input 
  - Only letters, no numeric / specials  
  - Check whether user input is 5 letters long 
  - Check whether user input is in dictionary 
- Evaluate & respond to user input
  - For each letter n in user input:
   - If userguess[n] is chosenword[n] color that letter green 
   - If userguess[n] appears in chosenword, color that letter yellow 
   - Otherwise color that letter dark grey 
  - Later: display a QWERTY layout showing which letters are in / out 
  - Later: display a “grade” for the guess, showing how many words the guess eliminated 
- Show output 

