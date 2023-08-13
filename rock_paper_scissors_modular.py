import random
game_choices = {1: "rock", 2: "paper", 3: "scissors"}

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

def update_scores(outcome, scores):
    if outcome == 2:
        scores["player"] +=1
    elif outcome == 3:
        scores["computer"] +=1

def is_game_complete(scores, winning_total):
    if scores["player"] == winning_total:
        return False
    if scores["computer"] == winning_total:
        return False
    return True

def print_choice_message(player, computer):
    print("You chose " + game_choices[player])
    print("The computer chose " + game_choices[computer])

# print round outcome
def print_outcome(outcome):    
    match outcome:
        case 1:
            print("You drew this round.\n")
        case 2:
            print("You won!\n")
        case 3:
            print("You lost this round.\n")
        case _:
            print("invalid outcome error\n") 

# adding stats
def update_stats(outcome, stats):
    if outcome == 1:
        stats["player"] += ["drew"]
        stats["computer"] += ["drew"]
    elif outcome == 2:
        stats["player"] += ["won"]
        stats["computer"] += ["lost"]
    else:
        stats["player"] += ["lost"]
        stats["computer"] += ["won"]

# update rounds
def round_counter(stats):
    stats["rounds"] += 1

# print final stats
def print_stats(scores, stats):
    print("GAME OVER!\n")
    print("You scored " + str(scores["player"]) + " and the computer scored " + str(scores["computer"]) + ".\n")
    print("This game lasted " + str(stats["rounds"]) + " rounds.\n")
    print("Your stats were: \n" + str(stats["player"]))
    print("The computer's stats were: \n" + str(stats["computer"]))

# run game loop
def run_game(winning_total):
    scores = {"player": 0, "computer": 0}
    stats = {"player": [], "computer": [], "rounds": 0}

    while is_game_complete(scores, winning_total):
        # take and validate player input
        player_input_str = get_player_input()
        if not validate_player_input(player_input_str):
            print("invalid response")
            continue
        
        # begin round incrementing
        round_counter(stats)
        
        # take int player and computer choice
        player_choice = convert_input_to_int(player_input_str)
        computer_choice = get_computer_choice()

        # check outcome of round
        outcome = get_outcome(player_choice, computer_choice)

        # update scores and stats for this round
        update_scores(outcome, scores)
        update_stats(outcome, stats)

        # prints messages for player
        print("Round " + str(stats["rounds"]))
        print_choice_message(player_choice, computer_choice)
        print_outcome(outcome)

    print_stats(scores, stats)

run_game(3)