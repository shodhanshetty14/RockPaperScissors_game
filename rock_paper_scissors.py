import random   

user_wins = 0
comp_wins = 0

elements = ['rock', 'paper', 'scissors']

while True:
    # the computer selects one of the items from the element list
    comp_choice = random.choice(elements)
    user_choice = input("Enter your choice:Rock, Paper, Scissors\nOr to Quit press 'q'").lower()
    if user_choice == 'q':
        # print the results and close the program
        print(f'you have won {user_wins} times.')
        print(f'Computer has won {comp_wins} times.')
        break
    if user_choice not in elements:
        print("Enter a valid choice(rock, Paper, Scissors)\n")
        continue
    if user_choice == 'rock' and comp_choice == 'scissors':
        print("You have won.")
        user_wins += 1
    elif user_choice == 'paper' and comp_choice == 'rock':
        print("You have won.")
        user_wins += 1
    elif user_choice == 'scissors' and comp_choice == 'paper':
        print("You have won.")
        user_wins += 1
    else:
        print("You have lost.")
        comp_wins += 1
