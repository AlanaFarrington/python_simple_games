# GAME RULES
# Ax9, Bx2, Cx2, Dx4, Ex12, Fx2, Gx3, Hx2, Ix9, Jx1, Kx1, Lx4, Mx2, Nx6, Ox8, Px2, Qx1, Rx6, Sx4, Tx6, Ux4, Vx2, Wx2, Xx1, Yx2, Zx1, blankx2
# word must be minimum of 2 letters long
# must run check that word guessed only uses letters that they have in their letter list
# check word against dictionary (dictionary module?)
# used letters must be removed from players letter list and then replaced with new tiles from remaining tiles list after each turn
# 50 point bonus for playing a word with all 7 of their letter tiles
# game ends when all the tiles have been drawn and one of the players has used all the tiles in their rack or both players have passed consecutively
# final scores are reduced by the amount of points on the players unplayer tiles
# player with most points wins the game

# EXTRA CHALLENGES
# make your letter_to_points dictionary able to handle lowercase inputs as well
# check if inputted words are real using a dictionary scraper
# plan out a board as a simple UI - board is 15 x 15 grid

import random

# make dictionary of letter points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letter_points = {key:value for key, value in zip(letters, points)}

# make list of remaining letter tiles
remaining_letter_tiles = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z", " ", " "]
print(letter_points)

#set players letter tiles and played words as empty lists
player_1_letters = []
player_2_letters = []
player_1_words = []
player_2_words = []

# fill player tiles rack with 7 random letter tiles from the 100 tiles which are then removed from the remaining tiles list
# TESTED
def fill_player_tiles(player_letters, remaining_letter_tiles):
  while len(player_letters) < 7:
    select_random_tile = random.randint(0,len(remaining_letter_tiles))
    print(select_random_tile)
    player_letters.append(remaining_letter_tiles[select_random_tile])
    # remove used letter from remaining_letter_tiles list
    del remaining_letter_tiles[select_random_tile]
    continue
  return player_letters

# print player letter list
# TESTED
def print_letter_list(player, player_letters):
   print(player + ", your letters are:\n")
   print(player_letters)

# get player input
# TESTED
def get_player_input():
    player_input = input("What is your word to play? ")
    return player_input.upper()

# validate player input - checked against their available letter tiles
def is_valid_word(player_letters, word):
   word_characters = [*word]
   print(len(word_characters))
   # check if word is correct length
   if len(word_characters) < 2 or len(word_characters) > 7:
      print("invalid word length. Word must be between 2 and 7 letters long.")
      return False
   #compare word characters with player letters
   check_letters = all(item in player_letters for item in word_characters)
   if check_letters == False:
    print("Invalid letter selection. Your played word contains one or more letters that you do not have.")
    return False
   # check against dictionary 
   return True

# add their played word to player word list
def update_player_word_list(word):
  if player == "player_1":
   player_1_words.append(word)
  if player == "player_2":
   player_2_words.append(word)

# validate real word (find dictionary module/scraper)
def validate_word(word):
  # check against dictionary
  return

#convert guessed word to score
# TESTED
def score_word(word):
  word_characters = [*word]
  point_total = 0
  for letter in word_characters:
    point_total += letter_points.get(letter, 0)
  if len(word_characters) == 7:
     point_total += 50
  return point_total

# print word outcome
def print_message(player_words, word_score):
    print("Your word was " + player_words[-1])
    print("You scored " + word_score + "for this word.\n")

# funcion to find scores for each player
player_words = {"player_1": player_1_words, "player_2": player_2_words}
player_to_points = {}
for player, words in player_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)

def is_game_complete(remaining_letter_tiles):
    if remaining_letter_tiles > 0:
        return False
    return True

# GAME LOOP
def run_game():
  scores = {"player 1": 0, "player 2": 0}
  player_words = {"player_1": player_1_words, "player_2": player_2_words}
  
  while is_game_complete(remaining_letter_tiles):
    fill_player_tiles(player_1_letters, remaining_letter_tiles)


