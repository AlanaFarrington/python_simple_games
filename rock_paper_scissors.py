#Rock = 1
#Paper = 2
#Scissors = 3

import random

rounds_played = 0
#make score list that is populated after each go with what user chose (won or lost). Could this be a dictionary?
player_choice_list = []
#sum the scores in each list to give player totals
computer_score = 0
player_score = 0
computer_choice = random.randint(1,3)

#use randint to generate play for computer
def computer_choice():
    return random.randint(1,3)

#use input to ask player for their play
def user_choice():
    user_choice = input("Make your choice. Rock, paper or scissors?")
    match user_choice:
        case "rock" | "Rock":
            print("You chose rock.")
            user_choice = int(1)
        case "paper" | "Paper":
            print("You chose paper.")
            user_choice = int(2)
        case "scissors" | "Scissors":
            print("You chose scissors.")
            user_choice = int(3)
        case _: 
            print("Invalid input error")
    return int(user_choice)

#compare player choice and computer choice using match case statement 
def run_game(user_choice, computer_choice):
    player_choice = user_choice()
    comp_choice = computer_choice()
    while player_choice != 1 and comp_choice != 1:
        if player_choice > comp_choice: 
            print("You won!")
        elif player_choice == comp_choice:
            print("You drew this round.")
    if player_choice == 1 and comp_choice == 3:
            print("You won!")
    elif player_choice == 3 and comp_choice == 1:
            print("You lost!")

#game loop runs 3 times and increments rounds played by 1
while rounds_played < 3:
    rounds_played += 1
    print(rounds_played)
    player_choice_list.append("won")
    player_score += 1
    comp_choice = computer_choice()
    player_choice = user_choice()
    run_game(comp_choice,player_choice)

print("Game over!")
print(score_list)
