#importing the random module
import random as r
#opening and reading the file
try:
    myFile = open("words.txt", "r")
    wordList = myFile.readlines()
    myFile.close()
except IOError:
    print("bugger, can't locate wordlist")

#determine word & test
word = r.choice(wordList)
#strips the /n off the end so the word length is correct
word = word.strip()
#test
print(word)

#creates guesses vairable for if loop
guesses = ''

#number of lives
lives = 12

#wrong guesses
wguess = ''



#loops while lives are greater than 0
while lives > 0:         
    print('hint: Animals')
    # blanks are for each character, this is used to tell if someone has one the game
    blanks = 0             

    # loops through for each character in the word
    for char in word:      
        if char in guesses:    
            print(char,)
        else:
            print("_",)    
            blanks += 1
    if blanks == 0:        
        print ("You won")
        #breaks the script as you dont want to continue to loop once you have won
        break              
    # input character
    guess = input("guess a character:")
    print('')
    # sets an extra variable
    guesses += guess
    print('Lives: '+lives* '0')
    # modifies the lives
    if guess not in word:  
        lives = lives -1
        wguess = wguess + guess
        print("Wrong guesses:", wguess)
    else:
        print("Wrong guesses:", wguess) 
        if lives == 0:
            print("You Loose") 