print("TheTechRobo Version: 0.3.1")
#SETUP
import os
#make a new command called Calc()
def Calc():
    while True: 
#CALCULATION CHOICE
        calc = input("Calculation?  (type ? for help): ")
#HELP
        if calc == "?":
            print('''
            Currently supported: multiplication (* or x), division (/ or div), addition (+), square (sq), subtraction (-), modulo (%), area (ar), volume (vol), and cube ([]). Type exit to exit. Commands are case-sensitive")
            ''')
#MULTIPLICATION
        elif calc == "*":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("Type the second number: "))
            print()
            print(number1 * number2)
            print()
            
        elif calc == "x":
            print()
            number1 = int(input("First number? "))
            number2 = int(input("Second number? "))
#SQUARE
        elif calc == "sq":
            print()
            squaredNumber = int(input("Type the number to be squared: "))
            print()
            print(squaredNumber * squaredNumber)
            print()
        elif calc == "[]":
            print()
            squaredNumber = int(input("Type the number to be squared: "))
            print()
            print(squaredNumber * squaredNumber)
            print()
#DIVISION
        elif calc == "/":
            print()
            number1 = int(input("type the first number: "))
            number2 = int(input("Type the second number: "))
            print()
            print(number1 / number2)
            print()
        elif calc == "div":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("Type the second number: "))
            print()
            print(number1 / number2)
            print()
#SUBTRACTION
        elif calc == "-":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("type the second number: "))
            print()
            print(number1 - number2)
            print()
        elif calc == "sub":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("type the second number: "))
            print()
            print(number1 - number2)
            print()
        elif calc == "min":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("type the second number: "))
            print()
            print(number1 - number2)
            print()
#ADDITION
        elif calc == "+":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("Type the second number: "))
            print()
            print(number1 + number2)
            print()
        elif calc == "add":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("Type the second number: "))
            print()
            print(number1 + number2)
            print()
#MODULO
        elif calc == "%":
            print()
            try:
                number1 = int(input("Type the first number(greater): "))
                number2 = int(input("Type the second number(smaller): "))
            except (TypeError, ValueError):
                print("Error!")
                print("Invalid input (code 1)")
                print()
            if(abs(number1)<abs(number2)):
                print()
                print("The second number entered is greater than the first number")
                print()
                Calc()
            else: 
                print(number1-number2*int(number1/number2))
                print()
        elif calc == "mod":
            print()
            try:
                number1 = int(input("Type the first number(greater): "))
                number2 = int(input("Type the second number(smaller): "))
            except (TypeError, ValueError):
                print("Error!")
                print("Invalid input (code 1)")
                print()
            if(abs(number1)<abs(number2)):
                print()
                print("The second number entered is greater than the first number")
                print()
                Calc()
            else: 
                print(number1-number2*int(number1/number2))
                print()
#AREA        
        elif calc == "ar":
            win = input("Is your OS the following: Windows? (Y/n, case-sensitive)")
            if win == "Y":
                print()
                os.system(start Area.bat)
            else: 
                print()
                print("Then this command is useless to you")
                print()
        elif calc == "#":
            win = input("Is your OS the following: Windows? (Y/n, case-sensitive)")
            if win == "Y":
                print()
                os.system(start Area.bat)
            else: 
                print()
                print("Then this command is useless to you")
                print()
#VOLUME
        elif calc == "vol":
            win = input("Is your OS the following: Windows? (Y/n, case-sensitive)")
            if win == "y":
                print()
                os.run(start Volume.bat)
            else: 
                print()
                print("Then this command is useless to you")
                print()
#CUBE
        elif calc == "{}":
            print()
            cubedNumber = int(input("Type the number to be cubed: "))
            print()
            print(cubedNumber * cubedNumber * cubedNumber)
            print()
        elif calc == "exit":
            exit()

        else:
            print('''
            print("Sorry, I don't understand your request. Currently supported calculations: * or x; / or div; -, min, or sub; + or add; % or mod (modulo); sq or [] (square); ar or # (area); vol (volume); and {} (cube). Sorry for the inconvenience")
            ''')

print()
Calc() #run the Calc() command above
