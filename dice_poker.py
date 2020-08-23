import random
from itertools import groupby

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6 

names ={nine: "9", ten : "10", jack: "J", queen: "Q", king: "K", ace:"A"}

player_score = 0
computer_score = 0

def start(): 
    print("Let's play dice poker")
    while game():
        pass
    scores()

def game():
    print("The computer will help you to roll your five dices")
    throws()
    return play_again()

def throws():
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print("Dice", i + 1,":",names[dice[i]])

    result = hand(dice)
    print("You currently have", result)

    while True : 
        rerolls = input("How many dices would you reroll ? ")
        try : 
            rerolls = int(rerolls)
            if rerolls in (0,1,2,3,4,5):
                break
        except ValueError:
            pass 
        print("I didn't understand. Please enter 1, 2, 3, 4 or 5")

    if rerolls == 5 :
        dice = roll(rerolls)
        for i in range(len(dice)):
            print("Dice", i + 1,":",names[dice[i]])

    elif rerolls != 0:
        roll_number = rerolls
        dice_rerolls = roll(roll_number)
        dice_changes = []
        print("Enter the number of the dice you want to reroll :")
        iteration = 0
        while iteration < rerolls:
            iteration += 1
            while True: 
                selection = input("")
                try: 
                    selection = int(selection)
                    if selection in (1,2,3,4,5):
                        break
                except ValueError:
                    pass
                print("I didn't understand. Please enter 1, 2, 3, 4 or 5")
            dice_changes.append(selection-1)
            print("You have change dice", selection) 
        
        iterations = 0
        while iterations < rerolls:
            iterations += 1
            replacement = dice_rerolls[iterations-1]
            dice[dice_changes[iterations-1]] = replacement
                
        for i in range(len(dice)):
            print("Dice", i + 1,":", names[dice[i]])
        
    result = hand(dice)
    print("End with :", result)

def roll(roll_number):
    numbers = [1, 2, 3, 4, 5, 6]
    dice = []
    iterations = 0
    while iterations < roll_number:
        iterations += 1
        dice.append(random.choice(numbers))
    return dice

def hand(dice):
    # groupby : count the numbers that make up the dice variable
    dice_hand = [len(list(group)) for key, group in groupby(dice)]
    dice_hand.sort(reverse=True)
    straight1 = [1,2,3,4,5]
    straight2 = [2,3,4,5,6]

    if dice == straight1 or dice == straight2:
        return "Sequel !"
    elif dice_hand[0] == 5:
        return "Five identical quarters !"
    elif dice_hand[0] == 4:
        return "Poker !"
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return "Full !"
        else:
            return "Brelan"
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return "Two pairs"
        else:
            return "One pair"
    else:
        return "A high card"

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

