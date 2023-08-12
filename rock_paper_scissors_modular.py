import random

rounds_played = 0
game_choices = {1: "rock", 2: "paper", 3: "scissors"}

# taking player input
def get_player_input():
    return input("Make your choice. rock = 1, paper = 2 or scissors = 3? ")

def validate_player_input(input): 
    return input.isnumeric() and (input > '0' and input < '4')
    
def convert_input_to_int(input):
    return int(input)

def get_computer_choice():
    return random.randint(1,3)

def get_outcome(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 1
    elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
        return 2
    return 3

def update_scores(scores, outcome):
    if outcome == 2:
        scores["player_score"] +=1
    elif outcome == 3:
        scores["computer_score"] +=1

# printing message to player
def print_message():
    if 
    print(print("You chose " + game_choices[player_choice_int]))
    
    print("You drew this round.\n")
    print("You won!\n")
    print("You lost this round.\n")

# adding stats
def update_stats(outcome):
    player_stats = []
    computer_stats = []
    if outcome == 1:
        player_stats.append("drew")
        computer_stats.append("drew")
    elif outcome == 2:
        player_stats.append("won")
        computer_stats.append("lost")
    else:
        player_stats.append("lost")
        computer_stats.append("won")

# run game loop
def run_game():
    scores = {"computer_score": 0, "player_score": 0}
    player_input_valid = False
    while(player_input_valid != False):
        player_input_str = get_player_input()
        player_input_valid = validate_player_input(player_input_str)

# update rounds
def round_counter():
    rounds_played = 0
    rounds_played += 1
    return rounds_played

# print final stats
def print_stats():
    print("GAME OVER!\n")
    print("This game lasted " + str(rounds_played) + " rounds.\n")
    print("You scored " + str(player_score) + " and the computer scored " + str(computer_score) + ".\n")
    print("Your stats were:")
    print(player_stats)
    print("The computer's stats were:")
    print(computer_stats)