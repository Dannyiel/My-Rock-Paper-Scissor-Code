import random

print("This is the Rock, Paper, scissor game")
print("Note: P = Paper, S = Scissor, R = Rock")
user_selection = ["P", "R", "S"]
computer_action = random.choice(user_selection)

user = str(input("enter P or R or S, to play the rock, scissors game: "))

for element in user_selection:
    if user == element:
        print("worked")
        break
    else:
        print("not available")
        break
if user == computer_action:
        print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
elif user == "paper":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
elif user == "scissors":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


# if user == computer_action:
#     print(f"Both players selected {user}. It's a tie!")
# elif user == "rock":
#     if computer_action == "S":
#         print("Rock smashes scissors! You win!")
#     else:
#         print("Paper covers rock! You lose.")
# elif user== "paper":
#     if computer_action == "R":
#         print("Paper covers rock! You win!")
#     else:
#         print("Scissors cuts paper! You lose.")
# elif user == "scissors":
#     if computer_action == "P":
#         print("Scissors cuts paper! You win!")
#     else:
#         print("Rock smashes scissors! You lose.")
