def convert_length():
    print("\n--- Length Converter ---\n")
    print("1. Meter to kilometers\n")
    print("2. Kilometer to meter\n")
    print("3. Miles to kilometers\n")
    print("4. Kilometers to miles\n")

    choice = int(input("Select a conversion 1-4: "))
    if choice not in [1,2,3,4]:
        print("Invalid choice bro!")
    val = float(input("Enter the value to convert: "))
    try:
        if choice == 1:
            print(f"{val} meters = {val/1000:.2f} kilometers.")
        if choice == 2:
            print(f"{val} kilometers = {val*1000:.2f} meters")
        if choice == 3:
            print(f"{val} miles = {val * 1.60934:.2f} kilometers.")
        if choice == 4:
            print(f"{val} kilometers = {val/1.60934:.2f} miles.")
    except ValueError:
        print("Error: Please enter a valid numerical value.")


def convert_weight():
    print("\n--- Weight Converter ---\n")
    print("1. Kilogram to pounds\n")
    print("2. Pounds to Kilograms\n")

    choice = int(input("Select a conversion 1-2: "))
    try:
        if choice not in [1,2]:
            print("Invalid choice bro!")
        val = float(input("Enter the value to convert: "))
        if choice == 1:
            print(f"{val} kilograms = {val * 2.205:.2f} pounds")
        if choice == 2:
            print(f"{val} pounds = {val/2.205:2f} kilograms")
    except ValueError:
        print("Error: Please enter a numerical value.")


def convert_temperature():
    print("\n--- Temperature Converter ---\n")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input('Select a conversion 1-2: '))
    try:
        if choice not in [1,2]:
            print('Invalid choice bro!')
        val = float(input('Enter the value to convert: '))
        if choice == 1:
            print(f"{val} degree Celsius = {val*(9/5)+32} degree Fahrenheit.")
        if choice == 2:
            print(f"{val} degree Fahrenheit = {(val-32)*(5/9)} degree Celsius.")
    except ValueError:
        print("Error: Please enter a numerical value.")

def main_menu():
    print("---------------------------")
    print("Python Unit Converter Tool |")
    print("---------------------------")
    print("1. Length\n")
    print("2. Weight\n")
    print("3. Temperature\n")
    print("4. Exit\n")

    main_choice = input("Please choose a category 1-4: ")
    if main_choice == '1':
        convert_length()
    elif main_choice == '2':
        convert_weight()
    elif main_choice == '3':
        convert_temperature()
    elif main_choice == '4':
        print("Thanks for using unit converter. Bye!")
        exit()
    else:
        print("Invalid category bro!")

if __name__ == "__main__":
    main_menu()