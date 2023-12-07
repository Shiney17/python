
def swapcase(input_string):
    return input_string.swapcase()

def title(input_string):
    return input_string.title()

def zfill(input_string):
    return input_string.zfill()

def isdecimal(input_string):
    return input_string.isdecimal()

def islower(input_string):
    return input_string.islower()

def split(input_string):
    return input_string.split()

def capitalize(input_string):
    return input_string.capitalize()

def count(input_string):
    return input_string.count()

def rjust(input_string):
    return input_string.rjust(len(input_string) + 4, '$')

def rstrip(input_string):
    return input_string.rstrip()

while True:
    print("String Functions")
    print("1. swapcase")
    print("2. title")
    print("3. zfill")
    print("4. isdecimal")
    print("5. islower")
    print("6. split")
    print("7. capitalize")
    print("8. count")
    print("9. rjust")
    print("10. rstrip")

    choice = int(input("Enter the function number (1-10): "))
    input_string = input("Enter the string: ")

    if choice == 1:
        print(swapcase(input_string))
    elif choice == 2:
        print(title(input_string))
    elif choice == 3:
        print(zfill(input_string))
    elif choice == 4:
        print(isdecimal(input_string))
    elif choice == 5:
        print(islower(input_string))
    elif choice == 6:
        print(split(input_string))
    elif choice == 7:
        print(capitalize(input_string))
    elif choice == 8:
        print(count(input_string))
    elif choice == 9:
        print(rjust(input_string))
    elif choice == 10:
        print(rstrip(input_string))
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")

    continue_program = input("Do you want to continue? (yes/no): ")
    if continue_program.lower() != 'yes':
        break