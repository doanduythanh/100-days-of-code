#TODO: Asking user want to play game or not
game_continue = True
while game_continue:
    is_new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if is_new_game == "y":
        print("Draw 2 random cards from deck for user and compute the value")
    else:
        print("Goodbye")
        game_continue = False
        break
    #TODO: Draw 2 random cards from deck for user and compute the value
    def draw_card():
        import random
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card
    computer_cards = []
    user_cards = []
    for _ in range(2):
        computer_cards.append(draw_card())
        user_cards.append(draw_card())
    print(f"Your cards: [{user_cards[0]}, {user_cards[1]}], current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    comp_value = sum(computer_cards)
    while sum(user_cards) < 21:
        want_draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if want_draw_card == "y":
            user_cards.append(draw_card())
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        else:
            break
    if 21 >= sum(user_cards) > comp_value:
        print("You win")
    elif sum(user_cards) > 21:
        print("You lose")
    elif sum(user_cards) == comp_value:
        print("Draw")
    else:
        print("You lose")
    print(f"Computer's cards: {computer_cards}, current score: {comp_value}")
    
#TODO: Draw 2 random cards from deck for computer and compute the value 
#TODO: Ask user want to draw another card or not
#TODO: If user draw another card, draw a random card from deck and compute the value
#TODO: If user value is greater than 21, user lose
#TODO: If user value is less than 21, and user want to draw one more card, computer draw a random card from deck and compute the value (can draw multiple cards until value is greater than 21)
#TODO: Ask user want to play again or not
#TODO: Compare user value and computer value, who is closer to 21 wins

