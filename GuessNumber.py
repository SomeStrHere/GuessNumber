#GuessNumber
#
#This program will randomly generate a number, and ask the user to attempt to guess that number. The
#program will inform the user if their guess is low or high.
#
#Version 0.0.1
#


import sys
from random import randint


def gameMenu() : 
    """Display welcome message and initial menu to user."""
    
    print('\nHello, welcome to Guess Number!\n')
    print('Ready to play...?')
    menuChoice = input('Press Y to start game, or X to quit.\n').upper()

    if menuChoice == "Y" :
        clearConsole(0)
        playGame()

    elif menuChoice == "X" :
        clearConsole(0)
        sys.exit()

def playGame() :
    """Obtain input from user, check against random number and display output"""

    intLower = 0
    intHigher = 0

    randomNumber(intLower, intHigher)


def randomNumber(a, b) :
    """Generates a random int from range a, b"""

    return(randint(a,b))


def clearConsole(wait) : #function to clear console on Linux or Windows
    """Clears console, with optional time delay.

    Will attempt to clear the console for Windows, should that fail it will attempt to clear the
    console for Linux.
    """

    import time
    time.sleep(wait) 
    # produces a delay based on the argument given to clearConsole()
    
    import os

    try :
       os.system('cls') #clears console on Windows

    except :
       os.system('clear') #clears console on Linux


def main() : 
    pass #TODO

if __name__ == "__main__" :
    main()
