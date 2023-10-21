letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
#print(letter_to_points)

player_1 = "player_1"
player_2 = "player_2"
player_1_words = []
player_2_words = []

def score_word(word):
  word_characters = [*word]
  point_total = 0
  for letter in word_characters:
    point_total += letter_to_points.get(letter, 0)
  return point_total

# play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
def play_word(player, word):
  if player == "player_1":
    player_1_words.append(word)
  if player == "player_2":
    player_2_words.append(word)

#brownie_points = score_word("BROWNIE")
#print(brownie_points)
#story_points = score_word("STORY")
#print(story_points)

player_words = {"player_1": player_1_words, "player_2": player_2_words}
player_to_points = {}
for player, words in player_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)

# If you want extended practice, try to implement some of these ideas with the Python you’ve learned
# update_point_totals() — turn your nested loops into a function that you can call any time a word is played
# make your letter_to_points dictionary able to handle lowercase inputs as well
# check if inputted words are real using a dictionary scraper
# plan out a board as a simple UI

