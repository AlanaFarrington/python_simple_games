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

# validate player input - checked against their available letter tiles
def is_valid_word(player, word):
   word_characters = [*word]
   copy_player_letters = player_letters[player]
   # check if word is correct length - TESTED
   if len(word_characters) < 2 or len(word_characters) > 7:
      print("Invalid word length. Word must be between 2 and 7 letters long.")
      return False
   #compare word characters with player letters
   # MUST FIX!!!!!!
   # need to account for player using a letter twice that they only have 1 of
   check_letters = all(item in player_letters[player] for item in word_characters)
   if check_letters == False:
    print("Invalid letter selection. Your played word contains one or more letters that you do not have.")
    return False
   for letter in [*word]:
         copy_player_letters.remove(letter)
         print(copy_player_letters)
   # validate real word (find dictionary module/scraper) - need to be a separate function??
   return True

# test calls of functions
fill_player_tiles(player_1)
print_letter_list(player_1)
player_1_word = get_player_input()
is_valid = is_valid_word(player_1, player_1_word)
