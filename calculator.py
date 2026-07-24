print("Hello!")
print("Welcome to the Calculator program.")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("What operation do you want to perform on the numbers? ")

if operation == "+" :
    total_addition = first_number + second_number
    print(f"{first_number} + {second_number} = {total_addition}")

if operation == "-" :
    total_subtraction = first_number - second_number
    print(f"{first_number} - {second_number} = {total_subtraction}")

if operation == "*" :
    total_multiplication = first_number * second_number
    print(f"{first_number} * {second_number} = {total_multiplication}")

if operation == "/" :
    total_division = first_number / second_number
    print(f"{first_number} / {second_number} = {total_division}")
