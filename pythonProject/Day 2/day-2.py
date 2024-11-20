print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = float(input("How many people to split the bill? "))
pay = (bill + tip) / number_of_people
print("Each person should pay: " + str(pay))
