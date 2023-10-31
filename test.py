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

# fill player tiles rack with 7 random letter tiles from the 100 tiles which are then removed from the remaining tiles list - TESTED
def fill_player_tiles(player):
  while len(player_letters[player]) < 7:
    select_random_tile = random.randint(0,(len(remaining_letter_tiles) - 1))
    player_letters[player].append(remaining_letter_tiles[select_random_tile])
    # remove used letter from remaining_letter_tiles list
    del remaining_letter_tiles[select_random_tile]
    continue

# print player letter list - TESTED
def print_letter_list(player):
   print(player + ", your letters are:")
   print(player_letters[player])

# get player input - TESTED
def get_player_input():
    player_input = input("What is your word to play? ")
    print("Your word was " + (player_input.upper()) + ".")
    return player_input.upper()

# update players letter tile list after word has been played - TESTED
def update_player_letter_list(valid_word, player, word):
   if valid_word == True:
      for letter in [*word]:
         player_letters[player].remove(letter)
   # replace used letter with new letters
   fill_player_tiles(player)

# test calls of functions
fill_player_tiles(player_1)
print_letter_list(player_1)
player_1_word = get_player_input()
#print(player_1_word)
is_valid = True
update_player_letter_list(is_valid, player_1, player_1_word)
