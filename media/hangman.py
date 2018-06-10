
""" Hangman game to be played in dentist wating room.
This code is designed to be played as a text based hangman.
"""

__author__ = "Tynan, Pedro and Nicole"
__copyright__ = "Copyright 2018, NSW Dept. Ed."
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Tynan, Pedro and Nicole"
__email__ = "tynan.matthews@education.nsw.com.au"
__status__ = "Prototype" 

#draft taken from the coffee rush game.

# dependencies
import pygame as P

#initialise pygame
P.init()


def main():
    # parameters
    screen_size = width, height = 800, 600

    # Define the colors we will use in RGB format
    black = [ 0, 0, 0]
    white = [255 ,255 ,255]
    blue = [ 0, 0 ,255]
    light_blue = [125,125,255]
    green = [ 0 ,255 , 0]
    red = [255 , 0, 0]

    clock = P.time.Clock() # Create a timer used to control how often the screen updates
    loop_rate = 30 #number of times per second does loop
    play = True
    over = False

    P.display.set_caption('Hangman Game')
    #icon = 
##    P.display.set_icon(icon)
    screen = P.display.set_mode(screen_size)
    #font = P.font.Font(None,30)
    
    while play:
        clock.tick(loop_rate) #fps
        now = P.time.get_ticks() #get the time since program started in millisecs

        event = P.event.poll() #did the player do something?

        if event.type == P.QUIT: #player clicked close so quit
            play = False
            over = True
        screen.fill(white) #clear the screen
    while not over:
        event = P.event.poll() #did the player do something?
        if event.type == P.QUIT: #player clicked close so quit
            over = True

    P.quit()


if __name__ == '__main__':
    main()