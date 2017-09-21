def Calculator():

    calc = input("What kind of calculation do you wish to do? (type ? for help): ")

    if calc == "?":
        print("Currently supported: *, /, + and - ")
        print("")
        Calculator();

    elif calc == "*":
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))
        print("Answer: ", number1 * number2)
        print("")
        Calculator();

    elif calc == "/":
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 / number2)
        print("")
        Calculator();

    elif calc == "-":
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 - number2)
        print("")
        Calculator();

    elif calc == "+":
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 + number2)
        print("")
        Calculator();
	
    elif calc == "exit":
        exit();
	
    else:
        print("")
        print("Sorry, I dont understand your request. Currently supported calculations: *, /, - and +. Sorry for the inconvenience!")
        print("")
        Calculator();

print("")
Calculator();
