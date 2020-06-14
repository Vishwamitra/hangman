import random
import re
from packages.words import word_list

def hideCharacters(word):
    hidden_word = word
    num = random.randint(0, len(word)-1)
    for i in range(0, len(word)-1):
            if i != num:
                hidden_word = hidden_word.replace(word[i], '_')
    return hidden_word

def startTheGame():
    print("Hello welcome to the new game... ")
    gamer = input("Enter your Name: ")
    print("Hello " + gamer + "! Welcome to hangman... Good luck!!")
    print("Let's begin...")
    print("************************")
    nextRound()

def nextRound():
    guesses = 6
    selected_word = random.choice(word_list)
    print("Total Chances : 6")
    print("Here you go with your word...")
    hidden_word = hideCharacters(selected_word)
    print(hidden_word)
    startGuessing(guesses,hidden_word,selected_word)

def startGuessing(guesses, hidden_word, selected_word):
    guessed_letters = []
    guessed = False
    while (not guessed and guesses >0):
            l = input("Your next guess : ")
            if (l in guessed_letters):
                print("Letter is already guessed !")
            elif (l in selected_word):
                occurances = [pos.start() for pos in re.finditer(l, selected_word)]
                for i in occurances:
                    hidden_word = hidden_word[:i] + l + hidden_word[i+1:]
                print(hidden_word)
            else :
                guesses = guesses - 1
                print("Wrong guess. Chances Left: " + str(guesses))
            guessed_letters.append(l)
            if  hidden_word == selected_word: guessed = True

    if  hidden_word != selected_word:
        print("The word was : " + selected_word)
        print("Sorry !! You lost this round !")
    else:
        print("Congratulations!! You won!!")

def main():
    startTheGame()
    while (input("Want to play again? (y/n)").upper() == "Y"):
        nextRound()
    print("Thank you!! See you next time...")

if __name__ == "__main__":
    main()