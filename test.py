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
            print("You drew this round.")
            player_score += 1
            computer_score += 1
            player_stats.append("drew")
            computer_stats.append("drew")
    elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
        print("You won!")
        player_score += 1
        player_stats.append("won")
        computer_stats.append("lost")
    else:
        print("You lost!")
        computer_score += 1
        player_stats.append("lost")
        computer_stats.append("won")

# Make game loop run 3 times
def game_loop():
    while (player_score < 3) or (computer_score < 3):
        rounds_played += 1
        print("Round " + str(rounds_played))
        compare_choices()

#print final score list
print("Game over!")
print("This game lasted " + str(rounds_played) + " rounds.")
print("You scored " + str(player_score) + " and the computer scored " + str(computer_score))
print("Your stats were:")
print(player_stats)
print("The computer's stats were:")
print(computer_stats)

