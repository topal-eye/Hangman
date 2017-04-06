# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    w = [] 
    for letters in lettersGuessed:
        if letters in secretWord:
            w.append(letters)
    if len(w) == len(secretWord):
        return True
    return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess=[]
    secret=[]
    secretLength= len(secretWord)
    secret= list(secretWord)
    x = 0
    while x < secretLength:
        guess+='_'
        x += 1    
        
    for letters in lettersGuessed:
        n = 0        
        while n < secretLength:
            if letters == secret[n]:
                guess[n] = secret[n]
            n+=1
    result= ''.join(guess)
    return(result)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
   
    list2=[]
    
    for i in string.ascii_lowercase:
        list2.append(i)
        
    def cleanDuplicate(list1, list2):
        ls= list1[:]
        for n in ls:
            if n in list2:
                list2.remove(n)
        return ''.join(str(n) for n in list2)

    return cleanDuplicate(lettersGuessed, list2)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    intro= len(secretWord)

    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is '+ str(intro) + ' letters long.') 
    gameOver = False
    guessesLeft = 8
    lettersGuessed = []
    while not gameOver:
        print("-" * 11)
        print("You have " + str(guessesLeft) + " guesses left." )
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters:"+ str(availableLetters))
        guess = input("Please guess a letter: ")
        guess = guess[0].lower()
        if guess in availableLetters:
            lettersGuessed.append(guess)
            if guess in secretWord:
                response = "Good guess:"
                if isWordGuessed(secretWord, lettersGuessed):
                    gameOver = True
            else:
                guessesLeft -= 1
                response = "Oops! That letter is not in my word:"
                if guessesLeft == 0:
                    gameOver = True
        else:
            response = "Oops! You've already guessed that letter:"
        print("{0:s} {1:s}".format(response, getGuessedWord(secretWord, lettersGuessed)))
    print("-" * 11)
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
         print("Sorry, you ran out of guesses. The word was"+ str(secretWord) + ".")




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
hangman('tact')
