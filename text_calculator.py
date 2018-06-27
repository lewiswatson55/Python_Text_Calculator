from operations import *


def calculator():
    global number2, number1
    calc = input(
        f"\nWhat kind of calculation do you wish to do? "
        f"(type {OP_HELP} for help): "
    )

    if calc == OP_HELP:
        display_help()
        calculator()

    elif calc == OP_MULT:
        number1 = get_input()
        number2 = get_input()
        print("Answer: ", number1 * number2)

    elif calc == OP_SQUARE:
        number1 = get_input()
        print("Answer: ", number1 * number1)

    elif calc == OP_DIV:
        number1 = get_input()
        number2 = get_input()
        print("Answer: ", number1 / number2)

    elif calc == OP_SUB:
        number1 = get_input()
        number2 = get_input()
        print("Answer: ", number1 - number2)

    elif calc == OP_ADD:
        number1 = get_input()
        number2 = get_input()
        print("Answer: ", number1 + number2)

    elif calc == OP_MOD:
        number1 = get_input()
        number2 = get_input()

        if number1 < number2:
            print("The second number entered is greater than the bigger number")

        print("Answer: ", number1 - number2 * int(number1 / number2))

    elif calc == OP_EXIT:
        exit()

    else:
        print("Sorry, I dont understand your request. ")
        display_help()
        print("Sorry for the inconvenience!")

    print()
    calculator()


def display_help():
    print(f'Currently supported: {", ".join(sorted(ALLOWED_OPERATIONS))}')


def get_input() -> int:
    nb = 0
    invalid = True

    while invalid:
        invalid = False
        try:
            nb = int(input("Please select the first number(greater): "))
        except (TypeError, ValueError):
            print("Invalid input")

    return nb


if __name__ == '__main__':
    print("")
    calculator()
