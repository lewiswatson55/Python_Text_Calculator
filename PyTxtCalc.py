print("TheTechRobo Version: 0.2.6")
#SETUP
import os
#make a new command called Calculator()
def Calc():
    while True: 
#CALCULATION CHOICE
        calc = input("Calculation?  (type ? for help): ")
#HELP
        if calc == "?":
            print('''
            Currently supported: multiplication(*), division(/), addition(+), square (sq), subtraction (-), modulo (%), and area (ar). Type exit to exit. Commands are case-sensitive")
            ''')
#MULTIPLICATION
        elif calc == "*":
            print()
            number1 = int(input("Please select the first number: "))
            number2 = int(input("Please select the second number: "))
            print()
            print(number1 * number2)
            print()
#SQUARE
        elif calc == "sq":
            print()
            number1 = int(input("Please select the first number: "))
            print()
            print(number1 * number1)
            print()
#DIVISION
        elif calc == "/":
            print()
            number1 = int(input("Please select the first number: "))
            number2 = int(input("Please select the second number: "))
            print()
            print(number1 / number2)
            print()
#SUBTRACTION
        elif calc == "-":
            print()
            number1 = int(input("Please select the first number: "))
            number2 = int(input("Please select the second number: "))
            print()
            print(number1 - number2)
            print()
#ADDITION
        elif calc == "+":
            print()
            number1 = int(input("Please select the first number: "))
            number2 = int(input("Please select the second number: "))
            print()
            print(number1 + number2)
            print()
#MODULO
        elif calc == "%":
            print()
            try:
                number1 = int(input("Please select the first number(greater): "))
                number2 = int(input("Please select the second number(smaller): "))
            except (TypeError, ValueError):
                print("Error!")
                print("Invalid input (code 1)")
                print()
            if(abs(number1)<abs(number2)):
                print()
                print("The second number entered is greater than the bigger number")
                print()
                Calc()
                print(number1-number2*int(number1/number2))
                print()
        
        elif calc == "ar":
            win = input("Is your OS the following: Windows? (y/n, case-sensitive)")
            if win == "y":
                print()
                os.run(start Area.bat)
            else: 
                print()
                print("Then this command is useless to you")
                print()
        elif calc == "exit":
            exit()

        else:
            print('''
            print("Sorry, I don't understand your request. Currently supported calculations: *, /, -, +, % (modulo), sq (square) and ar (area). Sorry for the inconvenience")
            ''')

print()
Calc() #run the Calc() command above
