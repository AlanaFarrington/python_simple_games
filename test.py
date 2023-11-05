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

def fill_player_tiles(player):
  while len(player_letters[player]) < 7:
    select_random_tile = random.randint(0,(len(remaining_letter_tiles) - 1))
    player_letters[player].append(remaining_letter_tiles[select_random_tile])
    # remove used letter from remaining_letter_tiles list
    del remaining_letter_tiles[select_random_tile]
    continue
  
def print_letter_list(player):
   print(player + ", your letters are:")
   print(player_letters[player])

# get player input - TESTED
def get_player_input():
    player_input = input("What is your word to play? ")
    print("Your word was " + (player_input.upper()) + ".")
    return player_input.upper()

def update_player_letter_list(valid_word, player, word):
   if valid_word == True:
      for letter in [*word]:
         player_letters[player].remove(letter)
   # replace used letter with new letters
   fill_player_tiles(player)

def swap_tiles(upper_want_to_swap, player):
   letters_to_swap = [*upper_want_to_swap]
   for letter in letters_to_swap:
      player_letters[player].remove(letter)
   fill_player_tiles(player)

def validate_word(player, word):
   word_characters = [*word]
   # check if word is correct length - TESTED
   if len(word_characters) < 2 or len(word_characters) > 7:
      print("Invalid word length. Word must be between 2 and 7 letters long.")
      return False
   #compare word characters with player letters
   check_letters = all(item in player_letters[player] for item in word_characters)
   if check_letters == False and word == "SWAP":
    want_to_swap = input("Type all of the letters that you wish to swap. ")
    upper_want_to_swap = want_to_swap.upper()
    swap_tiles(upper_want_to_swap, player)
    return False
   if check_letters == False:
    print("Invalid letter selection. Your played word contains one or more letters that you do not have.")
    return False
   # need to account for player using more copies of a letter than they have
   for letter in word_characters:
      if word_characters.count(letter) > player_letters[player].count(letter):
        print("Invalid letter selection. Your played word contains more " + letter + "s than you have.")
        return False
   # validate real word (find dictionary module/scraper) - need to be a separate function??
   return True

# test calls of functions
fill_player_tiles(player_1)
print_letter_list(player_1)
player_1_word = get_player_input()
is_valid = validate_word(player_1, player_1_word)
update_player_letter_list(is_valid, player_1, player_1_word)
