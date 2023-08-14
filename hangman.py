# hard code a word to be guessed
word_to_be_guessed = "einstein"

# separate the word into a list of characters 
def word_to_characters(word):
    return [*word]

# set up string with the correct number of underscores
def print_word_underscores(word_list, word_underscore_list):
    word_underscore_list.extend("_" * len(word_list))

# take user letter guess
def get_user_input():
    return input("Guess a letter. ")

# validate guess is a letter (not number/symbol)
def validate_user_input(user_input, user_guessed_list):
    if (len(user_input) > 1) or (len(user_input) == 0):
        return False
    if user_guessed_list.count(user_input) > 0:
        print("\nYou have already guessed that letter.")
        return False
    return (65 <= ord(user_input) <= 90) or (97 <= ord(user_input) <= 122)       

# check user input aginst list of characters
def check_input_against_word(user_input, word_list):
    num_of_occurences = word_list.count(user_input)
    if num_of_occurences > 0:
        indices = [i for i, letter in enumerate(word_list) if letter == user_input]
        return True, indices
    return False, []

# print outcome message
def print_outcome_message(outcome):
    if outcome == False:
        print("That letter is not in the word.\n")
        return
    print("Well done! That letter is in the word.\n")

# update underscores list
def update_underscores_list(outcome_bool, outcome_list, word_underscore_list, user_input):
    if outcome_bool == True:
        for index in outcome_list:
            word_underscore_list[index] = user_input

# set up a list containing the letters the user has guessed
def update_user_guesses(user_input, user_guessed_list):
    if user_guessed_list.count(user_input) > 0:
        return
    user_guessed_list.append(user_input)

# print user guessed list
def print_user_guesses(user_guessed_list):
    print("\nThe letters you have already guessed are: {} \n".format(user_guessed_list))

# check if game is complete
def is_game_complete(word_list, word_underscore_list):
    if word_list == word_underscore_list:
        return False
    return True

# game loop with is_game_valid logic
def run_game():
    round = 0
    user_guessed_letters = []
    word_underscore_list = []
    word_list = word_to_characters(word_to_be_guessed)
    print("Can you guess the secret password?")
    print_word_underscores(word_list, word_underscore_list)

    while is_game_complete(word_list, word_underscore_list):
        round += 1
        # get user input
        if round > 1:
            print_user_guesses(user_guessed_letters)

        user_input = get_user_input()

        # validate user input
        if not validate_user_input(user_input, user_guessed_letters):
            print("Invalid input. Try again.")
            continue

        # check user input against word
        is_in_word, letter_results = check_input_against_word(user_input, word_list)
        update_underscores_list(is_in_word, letter_results, word_underscore_list, user_input)
        print_outcome_message(is_in_word)
        print(word_underscore_list)
        
        # update user guessed letters list
        update_user_guesses(user_input, user_guessed_letters)

    print(f"GREAT JOB! You have guessed the secret word. The word was {word_to_be_guessed} \n \n YAY!   \( ﾟヮﾟ)/ \n ")
    print(f"It took you {round} guesses to find the word.\n")


# call game loop
run_game()