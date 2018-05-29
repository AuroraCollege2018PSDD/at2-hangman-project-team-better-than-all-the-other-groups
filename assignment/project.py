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
#n stands for number of words in text document
n = 7
lives = 12
#creating an array of words from the document to be selected.
try:
    wordFile = open("words.txt", "r")
    wordList = wordFile.readlines()
    wordFile.close()
    word = r.choice(wordList)
    word = word.strip()

except IO error:
    print('error cannot find .txt document")
        
    
    #gives user a hint
print("Topic: Animals")

livesDisplay = "0 " * n
print("Number of lives: " + livesDisplay)
          

guessStr = '_ ' * len(word)
print(guessStr)
#bug checking
print(word)



While n > 0:
    #we need to wack in a loop that 
    #1. asks for an input 
    #2. updates the underscores to characters (i pedro struggle with arrays lol) 
    #3. n-1 
    #4. displays lives after incorrect answer
    #5. Do we want to do this so that we dont get multiple prints, or so that the last print is erased?? i cant word right.





#extra stuff which was needed before but then fixed.
for i in range(1,n-1):
    my_list.append(wordList.readline())

word = my_list[rNumber]
print(word)

for i in range(0,len(word)-1):
    print("_")
