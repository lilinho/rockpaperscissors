"""
main.py

File contains actual game code
"""

from figures import *
import os
from random import randint


name = input("What\'s your name?: ")
ai = Player()
user = Player(n=name)

figures = [Scissors(), Rock(), Paper(), Spock(), Lizard()]
ai_choice = 0
key = ''
os.system('cls')
while True:
    print("0 - Scissors")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Spock")
    print("4 - Lizard")
    print("q - Quit")
    choice = input("What is your choice? ")
    ai_choice = randint(0, 4)

    if choice.isdigit():
        if int(choice) > 4:
            print("You've pressed wrong key. Try again!")
            continue
    elif not choice == "q":
        print("You've pressed wrong key. Try again!")
        continue
    if choice == "q":
        break
    # cheking if id of chosen figure is the key in defeat dict in opponents figure
    elif figures[ai_choice].id in figures[int(choice)].defeats:
        print(figures[int(choice)].defeats[ai_choice] + " - You won!")
        user.wins += 1
    elif figures[int(choice)].id in figures[ai_choice].defeats:
        print(figures[ai_choice].defeats[int(choice)] + " - Computer won!")
        ai.wins += 1
    else:
        print('It\'s a draw!')

if user.wins > ai.wins:
    print('You won!')
elif user.wins < ai.wins:
    print('Good game, but computer won')
else:
    print('It\'s a draw!')