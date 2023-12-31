import random

rounds_played = 0
game_choices = {1: "rock", 2: "paper", 3: "scissors"}
player_stats = []
computer_stats = []
computer_score = 0
player_score = 0

def compare_choices():
    global computer_score
    global player_score
    player_choice = int(input("Make your choice. rock = 1, paper = 2 or scissors = 3? "))
    print("You chose " + game_choices[player_choice])
    computer_choice = random.randint(1,3)
    print("The computer chose " + game_choices[computer_choice])
    if player_choice == computer_choice:
            print("You drew this round.\n")
            # player_score += 1
            # computer_score += 1
            player_stats.append("drew")
            computer_stats.append("drew")
    elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
        print("You won!\n")
        player_score += 1
        player_stats.append("won")
        computer_stats.append("lost")
    else:
        print("You lost this round.\n")
        computer_score += 1
        player_stats.append("lost")
        computer_stats.append("won")

# Make game loop run 3 times
def game_loop(winning_total):
    global rounds_played
    while (player_score < winning_total) and (computer_score < winning_total):
        rounds_played += 1
        print("Round " + str(rounds_played))
        compare_choices()

game_loop(3)

# print final score list
print("GAME OVER!\n")
print("This game lasted " + str(rounds_played) + " rounds.\n")
print("You scored " + str(player_score) + " and the computer scored " + str(computer_score) + ".\n")
print("Your stats were:")
print(player_stats)
print("The computer's stats were:")
print(computer_stats)