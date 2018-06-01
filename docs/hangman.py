""" Hangman game to be played in dentist wating room.
This code is designed to be played as a text based hangman game, prototype to the GUI game which will be created later. The hangman
is to be replaced with lives.
"""

__author__ = "Tynan, Pedro and Nicole"
__copyright__ = "Copyright 2018, NSW Dept. Ed."
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Tynan, Pedro and Nicole"
__email__ = "tynan.matthews@education.nsw.com.au"
__status__ = "Prototype" 


import random as r
import time
#variables
lives = 4
wrongGuess = ''
correct = 0
displayWord = []
#n stands for number of words in text document
try:
    myFile = open("words.txt", "r")
    wordList = myFile.readlines()
    myFile.close()
except IOError:
    print("bugger, can't locate wordlist")

#determine word & test
word = r.choice(wordList)
word = word.strip()
#strips the /n off the end so the word length is correct
print(word)

#determine word length & test
wordLength = len(word)
print(wordLength)

print('hint: Animals')
#print blank space
blankSpace = "_ " * wordLength


"""
wrongGuess.append(guess)
guess = input("Guess a letter  ")
wrongGuess.append(guess)
print("Previous Guesses ", wrongGuess)
"""
#def mainGame():
while lives > 0 and correct < wordLength:
      #print lives
    print(blankSpace)
    displayLives = 'lives: '+("O" * lives)
    #print(displayLives)
    guess = input("Guess a letter  ")
    for char in word:
          if guess == char:
              print(char)
          else:
              print("_ ")
    print(displayWord)
    if guess in word:
      print("yes")
      print(guess)
      correct = correct + 1
    else:
      print("no")
      lives = lives-1
      #shows all wrong guesses
      wrongGuess = wrongGuess+' '+ guess
      print('wrong guesses: '+wrongGuess)

#mainGame()

def win():
    print("Congratulations! You win!!")    

def lose():
    print("Unlucky, you lose. Better luck next time. The correct word was " + word + ".")
    
if correct == wordLength:
    win()
else:
    lose()
"""    
playAgain = input("Would you like to play again? y/n ")
playAgain = playAgain.lower()

if playAgain == "y":
    mainGame()
elif playAgain == "n":
    print("Thanks for playing!")
else:
    print("I didn't quite get that. ")
    playAgain = input("Would you like to play again? y/n ")
"""