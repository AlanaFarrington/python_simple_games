# taking player input
def get_player_input():
    return input("make a choice: ")
    
def validate_player_input(input):
    return input.isnumeric()
    
def convert_input_to_int(input):
    return int(input)
    
    

# printing message to player
def printMessage(msg):
    print(msg)

# get computers choice
def getComputerChoice():
    print()

# get outcome
def getOutcome():
    print()

# update scores
def updateScores():
    print()

# adding stats
# run game loop
def run_game():
    player_input_valid = False

    while(player_input_valid != False):
        player_input_str = get_player_input()
        player_input_valid = validate_player_input(player_input_str)



    
# update rounds
# print final stats