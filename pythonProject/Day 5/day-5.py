#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ""
for _ in range(0,nr_letters):
    easy_password += random.choice(letters)
for _ in range(0,nr_symbols):
    easy_password += random.choice(symbols)
for _ in range(0,nr_numbers):
    easy_password += random.choice(numbers)
print(easy_password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
result_characters = []
password_hard = ""
letter_order_list = []
for _ in range(0,nr_letters):
    result_characters.append(random.choice(letters))
for _ in range(0,nr_symbols):
    result_characters.append(random.choice(symbols))
for _ in range(0,nr_numbers):
    result_characters.append(random.choice(numbers))
while len(password_hard) != len(result_characters):
    _ = random.randrange(0, len(result_characters))
    if _ not in letter_order_list:
        password_hard += result_characters[_]
        letter_order_list.append(_)
print(password_hard)