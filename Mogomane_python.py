def display_menu():
    print("Choose an arithmetic operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Nominal Division")
    print("4. Floor Division")
    print("5. Modulo")
    print("6. Exponential")
    print("7. Multiplication")

def get_numbers():
    while True:
        try:
            num1 = int(input("Enter the first integer number: "))
            num2 = int(input("Enter the second integer number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter integer numbers.")

def perform_operation(choice, num1, num2):
    match choice:
        case 1:
            return num1 + num2
        case 2:
            return num1 - num2
        case 3:
            return num1 / num2
        case 4:
            return num1 // num2
        case 5:
            return num1 % num2
        case 6:
            return num1 ** num2
        case 7:
            return num1 * num2
        case _:
            return None

def is_odd(number):
    return number % 2 != 0

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-7): "))
            if choice < 1 or choice > 7:
                print("Invalid choice. Please select a number between 1 and 7.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue
        
        num1, num2 = get_numbers()
        result = perform_operation(choice, num1, num2)
        
        if result is not None:
            match choice:
                case 1:
                    operation_name = "Addition"
                case 2:
                    operation_name = "Subtraction"
                case 3:
                    operation_name = "Nominal Division"
                case 4:
                    operation_name = "Floor Division"
                case 5:
                    operation_name = "Modulo"
                case 6:
                    operation_name = "Exponential"
                case 7:
                    operation_name = "Multiplication"

            print(f"The two numbers you entered are: {num1} and {num2}")
            print(f"The result of your {operation_name} operation is: {result}")
            if is_odd(result):
                print("The result of your arithmetic operation is odd.")
            else:
                print("The result of your arithmetic operation is even.")
        else:
            print("There was an error performing the operation.")
        
        another = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the arithmetic operation program. Goodbye!")
            break

if __name__ == "__main__":
    main()
