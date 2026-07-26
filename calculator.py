print("Hello!")
print("Welcome to the Calculator program.")

while True:
    first_number = int(input("Enter the first number: "))

    while True:
        operation = input("What operation do you want to perform on the numbers? ")
        
        if operation == "+" or operation == "-" or operation == "*" or operation == "/" :
            break
        else :
            print("You can use the following operations: +, -, *, /")

    second_number = int(input("Enter the second number: "))

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
    