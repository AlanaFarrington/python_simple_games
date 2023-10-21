
word_underscore_list = ["c", "a", "t"]
word_list = ["c", "a", "t"]

def is_game_complete(word_list, word_underscore_list):
    if word_list == word_underscore_list:
        return False
    return True

print(is_game_complete(word_list, word_underscore_list))

