print("Welcome to secret auction program")

bid_info = {}
game_over = False
bid_count = 0
def input_bid():
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: "))
    bid_info.update({name:bid})  

while not game_over:
    input_bid()
    will_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if will_continue == 'no':
        game_over = True
value_list = list(bid_info.values())
key_list = list(bid_info.keys())
max_bid_value = max(value_list)
max_bid_value_index = value_list.index(max_bid_value)
print(f"The winner is {key_list[max_bid_value_index]}")
