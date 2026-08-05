import math

print("Hello!")
print("Welcome to the Calculator program.")

print()

operations = ["%", "+", "-", "*", "**", "sqrt", "/"]
print("You can use the following operations: ")
print(operations)
    
print()



while True:

    first_number = get_number("Enter the first number: ")

    while True:
        operation = input("What operation do you want to perform on the numbers? ")

        if operation in operations:
            break
        else:
            print("Invalid operation. Please try again.")

    if operation == "sqrt":
        if first_number >= 0:
            square_root = round(math.sqrt(first_number), 2)
            print(f"√{first_number} = {square_root}")
        else:
            print("You cannot calculate the square root of a negative number.")

    else:
        second_number = get_number("Enter the second number: ")

        if operation == "%":
            percentage = round((first_number / 100) * second_number, 2)
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
                division = round(first_number / second_number, 2)
                print(f"{first_number} / {second_number} = {division}")
            else:
                print("You cannot divide by zero.")