import random
from random import choice
import json

player_score = 0
computer_score = 0

def hangman(hangman):
    graphic = [
        """
            +-------+
            |
            |
            |
            |
            |
        =============
        """, 
        """
            +-------+
            |       |
            |       O
            |
            |
            |
        =============
        """,
        """
            +-------+
            |       |
            |       O
            |       |
            |
            |
        =============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|
            |
            |
        =============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |
            |
        =============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |      /
            |
        =============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |      / \\
            |
        =============
        """
    ]

    print(graphic[hangman])
    return

def start():
    print("Lets play hangman game !")
    while game():
        pass
    scores()

def game():
    jsonFile = open('ressources/dictionary.json')
    dictionary = json.load(jsonFile)
    word = choice(dictionary['en'])
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("You already tried letter", letter)
            else : 
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print("Sorry,", letter, "isnt't what we're looking for.")
                else:
                    print("Congratulation,", letter, "is correct !")
                    for i in range(word_length):
                        if letter == word[i] :
                            clue[i] = letter
        else:
            print("Do a another choice.")
        
        hangman(letters_wrong)
        print("".join(clue))
        print("\nTries : ", letters_tried)
        
        if letters_wrong == tries:
            print("Game over \nThe word was", word)
            computer_score += 1
            break
        if "".join(clue) == word:
            print("You win ! \nThe word was", word)
            player_score += 1
            break
    return play_again()

def guess_letter():
    print
    letter = input("Guess the mystery word :")
    letter.strip()
    letter.lower()
    print
    return letter

def play_again():
    answer= input("Try again ? y/n : ")
    if answer in ("y", "Y", "yes", "Yes"):
        return answer
    else :
        print("Thanks for playing. See you soon !")

def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("player: ", player_score)
    print("computer: ", computer_score)

if __name__ == '__main__':
        start()





