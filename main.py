#!/usr/bin/python3
import itertools
import random

def main():

    #define the work to be guessed
    lines = open('wordlist.txt').read().splitlines()
    secretWord = random.choice(lines).upper()

    #secretWord = "cheese"
    secretList = list(secretWord)
    blanks = list(itertools.repeat("_", len(secretWord)))
    guesses = 6
    won = False
    guessList = []
    #prompt user for guess and display rules. Use a function to validate that the user entered only one alpha character. 
    #Function should also check to see if the inputted letter is in the hidden word.
    #If in word, let the user know how many times.
    print("Welcome to Hangman. You get six guesses")
    while guesses > 0:
        if "_" in blanks:      
            try:
                print("\nYou have {0} guesses remaining!".format(guesses))
                print(" ".join(blanks) + "\n{0} letter word".format(len(blanks)) + "\n")
                guessLetter = input("Enter only one letter: ").upper()
                blanks, guesses = computeWord(secretList, guessLetter, blanks, guesses)
                guessList.append(guessLetter)
                guessList.sort()
                print("Your guesses: " + " ".join(guessList) + "\n")
            except:
                print("Try again")
        else:
            print("\nYou win!\nThe secret word was {0}\n".format(secretWord))
            won = True
            break

    if won != True:
        print("\nNice Try! Better luck next time\nThe secret word was {0}\n".format(secretWord))
    

#Function to print letters and number of guesses remaining
def computeWord(secret, letter, reveal, guesses):
    if len(letter) == 1 and letter.isalpha():
        print("'{0}' appears {1} time/s in the word!".format(letter, secret.count(letter)))
        for char in range(len(secret)):
            if secret[char] == letter:
                reveal[char] = letter
    else:
        print("You entered an incorrect character")
    if letter not in secret:
        guesses -= 1
    return reveal, guesses

if __name__== "__main__":
  main()