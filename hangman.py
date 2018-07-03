""" Basic pygame code that is a gui representation of the hangman game.
This code will have the letters display in box, text will go green when guess right or red when incorrect. Letters are clickable and no
lives are inplace for guesses as well as a shown hangman.
"""

__author__ = "Tynan, Pedro and Nicole"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "tynan.matthews@education.nsw.com.au"
__status__ = "Development"

#import code stuff
import pygame as P # pygame functions
import sys  # system functions
import time as T # Time functions
import random as r # random functions

#opening and reading the file
try:
    myFile = open("media/words.txt", "r")
    wordList = myFile.readlines()
    myFile.close()
except IOError:
    print("bugger, can't locate wordlist")

# Grabs a random word from the list
word = r.choice(wordList)
#strips the /n off the end so the word length is correct
word = word.strip()

#import pictures for loss
p1 = P.image.load('media/p1.png')
p2 = P.image.load('media/p2.png')
p3 = P.image.load('media/p3.png')
p4 = P.image.load('media/p4.png')
p5 = P.image.load('media/p5.png')
p6 = P.image.load('media/p6.png')
p7 = P.image.load('media/p7.png')
p8 = P.image.load('media/p8.png')
monster = P.image.load('media/monster.png')

monster = P.transform.scale(monster,(1000,375)) #scales the image

P.init()  # runs the game engine
clock = P.time.Clock()  ## creates clock to limit frames per second
loopRate = 60  # sets the fps
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1024, 768  # sets the screensize of the window displayed
screen = P.display.set_mode(SCREENSIZE)  # creates the game window

DEFAULT_TEXT_SIZE = 48 #text size variable we can refer to text rendering
icon = P.image.load('media/bailey.png')
#sets up the top window bar data 
P.display.set_icon(icon) 
P.display.set_caption('Spelling with Bailey')

# set variables for some colours RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (250, 0, 0)
yellow = (145, 131, 27)
green = (0, 255, 0)
blue = (250, 186, 255)
purple = (128, 0, 128)
lightBlue = (29, 145, 145)

#fills the screen with a blank colour
screen.fill(yellow)
#sets the number of lives
lives = 8 #wnumber of lives
looseSound = P.mixer.Sound('media/explosion.wav')
winSound = P.mixer.Sound('media/yay.wav')

#Small part of code that renders out the letters
class renderedLetter(object):
    """Renders the letters so that they can be displayed on the screen
    
    Before the text can be shown onto the screen each letter has to be
    individually renderd. Within here we can also control the text colour, size, etc.
    """
    def __init__(self, letter):
        self.text = letter
        self.size = DEFAULT_TEXT_SIZE
        self.color = yellow #text color
        self.backColor = yellow #the text background color
        self.x = 10 #x vaule where the ext will be shown on the sceen
        self.y = 100 #y vaule where the ext will be shown on the sceen
        self.font = P.font.SysFont("Lucida Console", self.size) #sets font, must be monospaced
        self.renderedText = self.font.render(self.text,1,self.color,self.backColor) #creates the rendered text
        self.rectangle = self.renderedText.get_rect().move(self.x,self.y) #Finds the rectangles of the text so that it can be clicked
        
    def update(self):
        '''  udates the rendered text on screen if there are any changes
        '''
        self.font = P.font.SysFont("Lucida Console", self.size) #monospace font
        self.renderedText = self.font.render(self.text,1,self.color,self.backColor) # creates the rendered text
        self.rectangle = self.renderedText.get_rect().move(self.x,self.y) #Finds the rectangles of the text so that it can be clicked
        
#other words to be rendered on the screen
alphabet = "abcdefghijklmnopqrstuvwxyz"
guessWord = word
looseWord = "You Loose"
hint = "Hint: animals "
winWord = 'tynan sucks'

#creates an array for the rendered letters
alphabetArray = [] #empty array for the alapabet letters to be rendered
for letter in alphabet:
    rLetter = renderedLetter(letter) #Refers back to the class rendered letter
    alphabetArray.append(rLetter) # joins each letter together
    
wordArray = [] #empty array for the letters to be rendered
for letter in guessWord:
    rLetter = renderedLetter(letter)
    wordArray.append(rLetter)

#displays alphabet letters on the screen
xPosition = 10 # x axis for alphabet
yPosition = 400 #y axis for alphabet
for l in alphabetArray:
    l.x = xPosition #set the x position for an individual rendered letter
    l.y = yPosition #set the y position for an individual rendered letter
    l.color = white #start with letters white
    l.backColor = yellow #so the letters blend in
    l.update() #refers back to the (update) part of the code
    screen.blit(l.renderedText,l.rectangle) #flips the screen and tells where the next letter will be
    xPosition += (l.rectangle.width + 10) #sets the postition for the next rendered letter

xPosition = 15 # x axis for word
yPosition = 200 # y axis for word
for l in wordArray: #follows the same steps as the last
    l.x = xPosition
    l.y = yPosition
    l.color = lightBlue
    l.backColor = lightBlue
    l.size = 2 * DEFAULT_TEXT_SIZE #make the vowels twice as big as the alphabet
    l.update()
    screen.blit(l.renderedText,l.rectangle)
    xPosition += (l.rectangle.width + 20)
    
hintArray = [] #empty array for the letters to be rendered
for letter in hint:
    rLetter = renderedLetter(letter)
    hintArray.append(rLetter)

    
xPosition = 25 # x axis for word
yPosition = 25 # y axis for word
    
for l in hintArray: #follows the same steps as the last
    l.x = xPosition #set the x position for an individual rendered letter
    l.y = yPosition #set the y position for an individual rendered letter
    l.color = black
    l.backColor = yellow #so the letters blend in
    l.size = 20 #sets the words size
    l.update() #refers back to the (update) part of the code
    screen.blit(l.renderedText,l.rectangle) #flips the screen and tells where the next letter will be
    xPosition += (l.rectangle.width + 10) #sets the postition for the next rendered letter

    
def looseText():
    looseArray = [] #empty array for the letters to be rendered
    looseSound.play()# plays the loosing explosion sound
    for letter in looseWord: 
        rLetter = renderedLetter(letter)
        looseArray.append(rLetter)

    
    xPosition = 200 # x axis for word
    yPosition = 100 # y axis for word
    screen.blit(monster, (10,225))
    for l in looseArray: #follows the same steps as the last
        l.x = xPosition #set the x position for an individual rendered letter
        l.y = yPosition #set the y position for an individual rendered letter
        l.color = black
        l.backColor = red #so the letters blend in
        l.size = DEFAULT_TEXT_SIZE * 2 #sets the words size
        l.update() #refers back to the (update) part of the code
        screen.blit(l.renderedText,l.rectangle) #flips the screen and tells where the next letter will be
        xPosition += (l.rectangle.width + 10) #sets the postition for the next rendered letter

def lifeImages():
    variableName = 'p' + str(lives)
    image = eval(variableName)
    image = P.transform.scale(image,(525,375)) #scales the image
    screen.blit(image, (450,25))

play = True# controls the whole loop

# this game loop should not loop any longer than the set looprate
while play:
    lifeImages()
    for event in P.event.get():  # gets any interactions the user has made
            if event.type == P.QUIT:  # if the X in the top corner has been clicked, the game will exit
                play = False  # exit game loop
            elif event.type != P.QUIT:
                if lives <= 0: # breaks the loop if there are no lives
                    screen.fill(red) # fills the screen red
                    looseText()#refers back to anohter part of the code to render out the text
                    P.display.flip()
                    T.sleep(10)
                    
                    play = False
                    

                elif lives > 0: # starts the main games loop for when there are lives
                    if event.type == P.MOUSEBUTTONDOWN:
                        mousePosition = P.mouse.get_pos() #finds where they clicked
            
            #Checks which letter was clicked
                        for a in alphabetArray:
                            if a.rectangle.collidepoint(mousePosition): #is the mouse click inside the letters rectangle
                                a.color = red
                                lives = lives - 1
                                 # a life is taken away when a letter is clicked, one is added to equal out if its the same as the word.
                                
                                for v in wordArray: #check whether that letter is a vowel
                                    if a.text == v.text: #if the letter clicked is in the word
                                        a.color = green
                                        v.backColor = yellow
                                        lives = lives + 1
                                        v.update() #we need to update any changes
                                        screen.blit(v.renderedText, v.rectangle) #re-blit
        
                                a.update() #made changes so we need to update
                                screen.blit(a.renderedText, a.rectangle) #re-blit
                


            P.display.flip()  # makes all the changes visable on the screen
            clock.tick(loopRate)  # limits the loops fps

P.quit()   # quits pygame 
sys.exit()  # quits the operating system window

