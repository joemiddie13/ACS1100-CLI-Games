# # flashcards.py

# import the json module from python3
import json
import random

# # open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

# initialize total as the length of the cards array
total = len(data["cards"])
# initialize score as 0
score = 0

# Original tutorial

# for i in data["cards"]:
#     guess = input(i["q"] + " > ")
#     print(guess)

#     if guess.lower() == i["a"].lower():
#         print("Correct!")
#     else:
#         print("Incorrect! The correct answer was", i["a"])

# Randomize the order of cards

random.shuffle(data["cards"])


# Keep Track of Score

for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess == i["a"]:
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")

# Game over message

if score == total:
    print("Amazing! You got all the questions correct! GOOD STUFF!")
    print("Do you want to review some more?")
elif score == 0:
    print("Sorry, you still have plenty of studying to do. You didn't get any correct. :/ ")
    print("Do you want to try again?")
else:
    print(f"GOOD STUFF! You got a score of {score}/{total}!")
    print("Do you want to keep practicing?")
