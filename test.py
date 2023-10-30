import random

# make dictionary of letter points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letter_points = {key:value for key, value in zip(letters, points)}

# make list of remaining letter tiles
remaining_letter_tiles = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z", " ", " "]
# print(letter_points)

#set players letter tiles and played words as empty lists
player_1_letters = ["S", "A"]
player_2_letters = ["B", "N", "P"]

# fill player tiles rack
def fill_player_tiles(player_letters, remaining_letter_tiles):
  while len(player_letters) < 7:
    select_random_tile = random.randint(0,len(remaining_letter_tiles))
    print(select_random_tile)
    player_letters.append(remaining_letter_tiles[select_random_tile])
    # remove used letter from remaining_letter_tiles list
    del remaining_letter_tiles[select_random_tile]
    continue
  return player_letters

fill_player_tiles(player_1_letters, remaining_letter_tiles)
print("Player 1, your letters are:")
print(player_1_letters)
#print("The remining unused letter tiles are:")
#print(remaining_letter_tiles)
print(len(remaining_letter_tiles))
fill_player_tiles(player_2_letters, remaining_letter_tiles)
print("Player 2's letter list is:")
print(player_2_letters)
#print("The remining unused letter tiles are:")
#print(remaining_letter_tiles)
print(len(remaining_letter_tiles))