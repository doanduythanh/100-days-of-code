def input_num1():
    """Prompt user to input the first number."""
    return float(input("What's the first number?: "))

def calc(num1):
    """Perform a calculation using num1 and a user-specified operation."""
    print("""
    +
    -
    *
    /
    """)
    op = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("Invalid operation.")
        return num1  # Return the original number if invalid
    print(f"{num1} {op} {num2} = {result}")
    return result

def continue_cal(num):
    """Continue calculations with the current result."""
    print("""
    +
    -
    *
    /
    """)
    op = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    if op == "+":
        result = num + num2
    elif op == "-":
        result = num - num2
    elif op == "*":
        result = num * num2
    elif op == "/":
        result = num / num2
    else:
        print("Invalid operation.")
        return num  # Return the original number if invalid
    print(f"{num} {op} {num2} = {result}")
    return result

game_over = False
while not game_over:
    num1 = input_num1()
    result = calc(num1)
    while True:
        will_continue = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'q' to quit: ").lower()
        if will_continue == 'y':
            result = continue_cal(result)
        elif will_continue == 'n':
            break
        elif will_continue == 'q':
            game_over = True
            break
        else:
            print("Invalid input. Please type 'y', 'n', or 'q'.")