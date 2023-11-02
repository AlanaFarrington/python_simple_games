import random

# make dictionary of letter points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letter_points = {key:value for key, value in zip(letters, points)}

# make list of remaining letter tiles
remaining_letter_tiles = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z", " ", " "]

player_1 = "Alana"
player_2 = "Will"
player_letters = {player_1: ["S", "A", "E"], player_2: ["B", "N", "P", "E", "R", "S", "E"]}
player_words = {player_1: ["SEA"], player_2: ["BROWNIE"]}
current_player = player_1
turns_played = {player_1: 0, player_2: 0}

# change current player
def update_current_player():
   if turns_played[player_1] > turns_played[player_2]:
       current_player = player_2
       print("Current player is now player 2")
       return current_player
   if turns_played[player_1] == turns_played[player_2]:
       current_player = player_1
       print("Current player is now player 1")
       return current_player

# test calls of functions
# fill_player_tiles(player_1)
# print_letter_list(player_1)
# player_1_word = get_player_input()
# is_valid = validate_word(player_1, player_1_word)
# update_player_letter_list(is_valid, player_1, player_1_word)

print(current_player)
turns_played[current_player] += 1
print(turns_played)
current_player = update_current_player()
print(current_player)

turns_played[current_player] += 1
print(turns_played)
current_player = update_current_player()
print(current_player)

turns_played[current_player] += 1
print(turns_played)
current_player = update_current_player()
print(current_player)

turns_played[current_player] += 1
print(turns_played)
current_player = update_current_player()
print(current_player)