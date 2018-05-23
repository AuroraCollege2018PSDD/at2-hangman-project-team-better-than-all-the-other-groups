import random as r
import time
#n stands for number of words in text document
n = 7
lives = 12
wordFile = open("words.txt", "r")
wordList = wordFile.readlines()
wordFile.close()
word = r.choice(wordList)
word = word.strip()

guessStr = '_ ' * len(word)
print(guessStr)
print(word)

for i in range(1,n-1):
    my_list.append(wordList.readline())

word = my_list[rNumber]
print(word)

for i in range(0,len(word)-1):
    print("_")
