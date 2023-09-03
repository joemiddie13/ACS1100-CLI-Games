# # Import the random library
# from random import randint

# # Make an array / Define roles
# roles = ["Bear", "Ninja", "Cowboy"]
# print("GET READY TO PLAY: BEAR, NINJA, OR COWBOY!")

# # Generate a random number to pick a random element from the array
# # computer = roles[randint(0,2)]

# # Get player input
# # player = input("Bear, Ninja, or Cowboy? > ")

# # Compare computer and player role

# # Game loop
# player = False

# while player == False:
#     computer = roles[randint(0,2)]
#     while True:
#       player = input("Bear, Ninja, or Cowboy? > ").capitalize()
#       if player in roles:
#         break
#       else:
#         print("Please choose either Bear, Ninja, or Cowboy to play!")

# # print(f"{computer} - Computer choice!")
# # print(f"{player} - Player choice!")   
    
#     # Compare computer and player role
#     if computer == player:
#       print("DRAW!")
#     elif computer == "Cowboy":
#       if player == "Bear":
#         print(f"You lose! {computer} shoots {player}")
#       else: # computer is cowboy, player is ninja
#         print(f"You win! {player} defeats {computer}")
#     elif computer == "Bear":
#       if player == "Cowboy":
#         print(f"You win! {player} shoots {computer}")
#       else: # computer is bear, player is ninja
#         print(f"You lose! {computer} eats {player}")
#     elif computer == "Ninja":
#       if player == "Cowboy":
#         print(f"You lose! {computer} defeats {player}")
#       else: # computer is ninja, player is bear
#         print(f"You win! {player} eats {computer}")

# # Asking the user if they would like to play again.
#     play_again = input("Would you like to play again? (yes/no) > ")
#     if play_again == 'yes':
#       player = False
#       computer = roles[randint(0,2)]
#     else:
#       break

#################################################################################

# TURN THE ABOVE CODE INTO FUNCTION CODING BLOCKS

from random import randint

roles = ["Bear", "Ninja", "Cowboy"] # A variable of "roles" with an array of choices

# Create a function to get the computer's choice
def get_computer_choice(roles):
    return roles[randint(0,2)] # This randomly selects a role 

# Create a function to get the player's choice
def get_player_choice():
    while True:
        player = input("Bear, Ninja, or Cowboy? > ").capitalize()
        if player in roles: # Verifies if the player's choice was in "roles"
            return player
        else: # If choice is not valid, ask the user again.
            print("Please choose either Bear, Ninja, or Cowboy to play!")

# Create a function to determine the winner
def determine_winner(computer, player):
    if computer == player:
        return "DRAW!"
    elif computer == "Cowboy":
        if player == "Bear":
            return (f"You lose! {computer} shoots {player}")
        else:  # computer is cowboy, player is ninja
            return (f"You win! {player} defeats {computer}")
    elif computer == "Bear":
        if player == "Cowboy":
            return (f"You win! {player} shoots {computer}")
        else:  # computer is bear, player is ninja
            return (f"You lose! {computer} eats {player}")
    elif computer == "Ninja":
        if player == "Cowboy":
            return (f"You lose! {computer} defeats {player}")
        else:  # computer is ninja, player is bear
            return (f"You win! {player} eats {computer}")

# Create a function to see if the user wants to play again
def play_again_prompt():
    # Prompt the user and ask if they want to play again
    return input("Would you like to play again? (yes/no) > ") == 'yes'

# Game loop
roles = ["Bear", "Ninja", "Cowboy"]
print("GET READY TO PLAY: BEAR, NINJA, OR COWBOY!")

# Here we initialize the player variable to False to start the loop
player = False

# The loop will continue as long as the player variable is False
while player == False:
    # Retrieve the computer choice for round
    computer = get_computer_choice(roles)
    # Retrieve player's choice
    player = get_player_choice()
    
    # Determine the winner
    result = determine_winner(computer, player)
    print(result)
    
    # See if they player wants to play again
    if not play_again_prompt():
        break # breaks out of the loop if they don't want to play anymore
    player = False