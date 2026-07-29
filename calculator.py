import math

print("Hello!")
print("Welcome to the Calculator program.")

while True:

    while True:
        try:
            first_number = int(input("Enter the first number: "))
            break
        except ValueError:
            print("Please enter a number.")

    while True:
        operation = input("What operation do you want to perform on the numbers? ")

        if operation in ["%", "+", "-", "*", "**", "sqrt", "/"]:
            break
        else:
            print("You can use the following operations: %, +, -, *, **, sqrt, /")

    if operation == "sqrt":
        if first_number >= 0:
            square_root = math.sqrt(first_number)
            print(f"√{first_number} = {square_root}")
        else:
            print("You cannot calculate the square root of a negative number.")

    else:
        while True:
            try:
                second_number = int(input("Enter the second number: "))
                break
            except ValueError:
                print("Please enter a number.")

        if operation == "%":
            percentage = (first_number / 100) * second_number
            print(f"{first_number}% of {second_number} = {percentage}")

        elif operation == "+":
            addition = first_number + second_number
            print(f"{first_number} + {second_number} = {addition}")

        elif operation == "-":
            subtraction = first_number - second_number
            print(f"{first_number} - {second_number} = {subtraction}")

        elif operation == "*":
            multiplication = first_number * second_number
            print(f"{first_number} * {second_number} = {multiplication}")

        elif operation == "**":
            power = first_number ** second_number
            print(f"{first_number} ** {second_number} = {power}")

        elif operation == "/":
            if second_number != 0:
                division = first_number / second_number
                print(f"{first_number} / {second_number} = {division}")
            else:
                print("You cannot divide by zero.")