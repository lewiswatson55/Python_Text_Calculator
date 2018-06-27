def calculator():
    calc = input("What kind of calculation do you wish to do? (type ? for help): ")

    if calc == "?":
        print("Currently supported: multiplication(*), division(/), addition(+),square (sq) and subtraction (-)")
        print("")
        calculator()

    elif calc == "*":
        print("")
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))
        print("Answer: ", number1 * number2)
        print("")
        calculator()

    elif calc == "sq":
        print("")
        number1 = int(input("Please select the first number: "))
        print("Answer: ", number1 * number1)
        print("")
        calculator()

    elif calc == "/":
        print("")
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 / number2)
        print("")
        calculator()

    elif calc == "-":
        print("")
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 - number2)
        print("")
        calculator()

    elif calc == "+":
        print("")
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 + number2)
        print("")
        calculator()

    elif calc == "%":
        print("")
        try:
            number1 = int(input("Please select the first number(greater): "))
            number2 = int(input("Please select the second number(smaller): "))
        except (TypeError, ValueError):
            print("Invalid input")
            print("")
            calculator()

        if abs(number1) < abs(number2):
            print("")
            print("The second number entered is greater than the bigger number")
            print("")
            calculator()

        print("Answer: ", number1 - number2 * int(number1 / number2))
        print("")
        calculator()

    elif calc == "exit":
        exit()

    else:
        print("")
        print(
            "Sorry, I dont understand your request. Currently "
            "supported calculations: *, /, -, + and % (MODULO). "
            "Sorry for the inconvenience!"
        )
        print("")
        calculator()


if __name__ == '__main__':
    print("")
calculator()
