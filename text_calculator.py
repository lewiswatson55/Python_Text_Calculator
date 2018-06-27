from operations import *


def calculator():
    calc = input(
        f'\nWhat kind of calculation do you wish to do? '
        f'(type {OP_HELP} for help): '
    )

    # base commands
    if calc == OP_HELP:
        display_help()

    elif calc == OP_EXIT:
        exit()

    elif calc not in ALLOWED_OPERATIONS:
        print('Sorry, I dont understand your request. ')
        display_help()
        print('Sorry for the inconvenience!\n')

    else:
        # operations with one number
        res = get_input()
        if calc == OP_SQUARE:
            res *= res

        elif calc == OP_SQROOT:
            res **= .5

        # operations with two numbers
        else:
            number2 = get_input(index=2)
            if calc == OP_MULT:
                res *= number2

            elif calc == OP_DIV:
                res //= number2

            elif calc == OP_SUB:
                res -= number2

            elif calc == OP_ADD:
                res += number2

            elif calc == OP_MOD:
                if res < number2:
                    print('The second number entered is greater than the bigger number')
                res %= number2

        print(f'Answer: {res}\n')
    calculator()


def display_help():
    print(f"Currently supported: {', '.join(sorted(ALLOWED_OPERATIONS))}")


def get_input(index=1) -> int:
    msg = 'Please select the '
    msg += 'first' if index == 1 else 'second'
    msg += ' number: '

    nb = ''
    while not nb.isdigit():
        nb = input(msg)

    return int(nb)


if __name__ == '__main__':
    calculator()
