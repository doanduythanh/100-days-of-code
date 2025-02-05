import random
#TODO: Number of attempts: easy 10, hard 5
EASY = 10
HARD = 5
WELCOME = "Welcome to the Number Guessing Game!"
def guess_number():
    print(WELCOME)
    #TODO: Generate a random number between 1 and 100
    answer_number = random.randint(1, 100)
    #TODO: Let user choose difficulty level: easy or hard
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = EASY
    else:
        attempts = HARD
    #TODO: Let user guess the number until he/she win or lose
    while attempts > 0:
        #TODO: Track the number of remaining attempts
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        #TODO: Check user's guess against actual answer
        if guess == answer_number:
            print("You got it!")
            break
        elif guess > answer_number:
            print("Too high.")
            attempts -= 1
        else:
            print("Too low.")
            attempts -= 1
        
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            break
while True:
    guess_number()
    play_again = input("Do you want to play again? Type 'yes' or 'no': ")
    if play_again == "no":
        break