#TODO: Make data list for Higher Lower game using dictionary which has followers count and name of the object
import random

user_score = 0
game_data = [
    {
        'name': "Domestic Abuse",
        'follower_count': 33100
    },
    {
        'name': "Converse",
        'follower_count': 2700000
    },
    {
        'name': "Nike",
        'follower_count': 120000000
    },
    {
        'name': "Adidas",
        'follower_count': 26000000
    },
    {
        'name': "Puma",
        'follower_count': 11000000
    },
    {
        'name': "Reebok",
        'follower_count': 3000000
    },
    {
        'name': "Under Armour",
        'follower_count': 9000000
    },
    {
        'name': "New Balance",
        'follower_count': 2000000
    },
    {
        'name': "Vans",
        'follower_count': 15000000
    },
    {
        'name': "Asics",
        'follower_count': 1000000
    },
    {
        'name': "Fila",
        'follower_count': 5000000
    },
    {
        'name': "Skechers",
        'follower_count': 4000000
    },
    {
        'name': "Brooks",
        'follower_count': 800000
    },
    {
        'name': "Saucony",
        'follower_count': 600000
    },
    {
        'name': "Mizuno",
        'follower_count': 700000
    },
    {
        'name': "Hoka One One",
        'follower_count': 900000
    },
    {
        'name': "Salomon",
        'follower_count': 1000000
    },
    {
        'name': "Merrell",
        'follower_count': 800000
    },
    {
        'name': "Columbia",
        'follower_count': 1200000
    },
    {
        'name': "The North Face",
        'follower_count': 2000000
    }
]

def get_object_info(order, name, follower):
    if order == 0:
        print(f"Compare A: {name}, {follower} followers")
    else:
        print(f"Against B: {name}, {follower} followers")

def generate_object_b(object_a):
    while True:
        object_b = random.choice(game_data)
        if object_b != object_a:
            return object_b

while True:
    object_a = random.choice(game_data)
    get_object_info(0, object_a["name"], object_a["follower_count"])
    object_b = generate_object_b(object_a)
    get_object_info(1, object_b["name"], object_b["follower_count"])

    player_choose = input("Who has more followers? Type 'A' or 'B': ").lower()

    if player_choose == "a":
        if object_a["follower_count"] > object_b["follower_count"]:
            user_score += 1
            print(f"You're right! Current score: {user_score}")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
    elif player_choose == "b":
        if object_b["follower_count"] > object_a["follower_count"]:
            user_score += 1
            print(f"You're right! Current score: {user_score}")
            object_a = object_b
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
    else:
        print("Invalid input. Please type 'A' or 'B'.")

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again != 'yes':
        print(f"Thanks for playing! Your final score is: {user_score}")
        break
#TODO  If user correct: If B > A replace A by B. If A > B remove B. Add 1 point for user's score
#TODO: Random new object B and show its information
#TODO: If user was wrong: Display user's score and say game over
#TODO: Ask user if they want to play again or not.
