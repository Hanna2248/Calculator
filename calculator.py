print("Hello!")
print("Welcome to the Calculator program.")

while True:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    operation = input("What operation do you want to perform on the numbers? ")

    if operation == "+" :
        addition = first_number + second_number
        print(f"{first_number} + {second_number} = {addition}")

    elif operation == "-":
        subtraction = first_number - second_number
        print(f"{first_number} - {second_number} = {subtraction}")

    elif operation == "*":
        multiplication = first_number * second_number
        print(f"{first_number} * {second_number} = {multiplication}")

    elif operation == "/":
        if second_number != 0:
            division = first_number / second_number
            print(f"{first_number} / {second_number} = {division}")
        else:
            print("You cannot divide by zero.")
    else :
        print("Invalid operation.")

    