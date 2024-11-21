import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock,paper,scissors]
print(rps)
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)
else:
    print("Not valid. Try again")
com_choice = random.choice(rps)
if user_choice == com_choice:
    print("Draw")
else:
    if user_choice == "0":
        if com_choice == rock:
            print("You Lose")
        else:
            print("You win")
    elif user_choice == "1":
        if com_choice == rock:
            print("You win")
        else:
            print("You lose")
    else:
        if com_choice == "1":
            print("You win")
        else:
            print("You lose")
