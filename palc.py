#SETUP
import os
from ex import *
from root import *
print("Please wait")
print()
macwin = input("Is your os the following: Windows? (Y/n)")
if macwin == "Y":
    print("Ok, OS set to: Windows")
    os.system('cls')
elif macwin == "y":
    print("Set os to: Windows")
    os.system('cls')
elif macwin == "N":
    print("Set os to: linux")
    os.system('clear')
elif macwin == "n":
    print("Set os to: Linux")
    os.system('clear')
else:
    print("Please, Type in the answer to the question (y/n)")
#make a new command called palc()
def e():
	exit()
def palc():
    while True:
       for i in range (1, 13):
		   print()
#CALCULATION CHOICE
        calc = input("Calculation?  (type ? for help): ")
#HELP
        if calc == "?":
            print('''
            Currently supported: multiplication (*), division (/), addition (+), square (sq), subtraction (-), modulo (%), area (#), volume (vol), cube ({}), cube twice ({2}), exponents (ex), and root (root). Type exit to exit. Commands are case-sensitive
            To access support: go to https://github.com/thetechrobo/support/
            To modify Palc: go to https://github.com/thetechrobo/python-text-calculator/
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
            print()
            print(number1 * number2)
            print()
#SQUARE
        elif calc == "sq":
            print("Please note this is the same as running [] or ex")
            ex2()
        elif calc == "[]":
            print("Please note it's the same as running sq or ex")
            ex2()
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
                bigger = int(input("Type the first number(greater): "))
                smaller = int(input("Type the second number(smaller): "))
            except (TypeError, ValueError):
                print("Error!")
                print("Invalid input (code 1)")
                print()
            if(abs(bigger)<abs(smaller)):
                print()
                print("Error!")
                print("The second number entered is greater than the first number")
                print()
                Calc()
            else:
                print(bigger-smaller*int(bigger/smaller))
                print()
        elif calc == "mod":
            print()
            try:
                number1 = int(input("Type the first number(greater): "))
                number2 = int(input("Type the second number(smaller): "))
            except (TypeError, ValueError): #If you inputted wrong
                print("Error!")
                print("Invalid input (code 1)")
                print()
            if(abs(number1)<abs(number2)): #If you put the numbers in wrong order
                print()
                print("Error!")
                print("The second number entered is greater than the first number")
                print()
            else:
                print(number1-number2*int(number1/number2))
                print()
#AREA
        elif calc == "ar":
            print("If struggling in Python 2, in the code, look at the following line (there's a comment)")
            exec("area.py")    #If struggling in python 2, change to execfile("area.py")
        elif calc == "#":
            exec("area.py")
#VOLUME
        elif calc == "vol":
            exec("volume.py") #More secure than os.system but currently doesn't work because it doesnt call any functions FROM volume.py
#CUBE
        elif calc == "{}":
            print()
            cubedNumber = int(input("Type the number to be cubed: "))
            print()
            print(cubedNumber * cubedNumber * cubedNumber)
            print()
#EXIT
        elif calc == "exit":
            exit()
        elif calc == "EXIT":
            exit()
#EXPONENTS (had the idea during bike ride on 18/9/2019 19hsomething after the BBQ)
        elif calc == "ex":
            exponent2Use = int(input("Exponent? (Coded: 2,3,4,5)"))
            if exponent2Use == 2:
                print("Please Note; this is the same as running sq or []")
                ex2()
            elif exponent2Use == 3:
                ex3()
            elif exponent2Use == 4:
                ex4()
            elif exponent2Use == 5:
                ex5()
            elif exponent2Use == 1:
                ex1()
            elif exponent2Use == 6:
                ex6()
            else:
                print("ERROR: not coded. (Coded: 1 2 3 4 5 6)")
#ROOTS
        elif calc == "root":
            root = input("Square root or cube root?(square/cube case-sensitive)")
            if root == "square":
                sq()
            elif root == "cube":
                cu()
#EASTER EGG!
        elif calc == "=":
            print()
            number = int(input("Type in a number:"))
            if number == 42:
                print("=42 -- the answer to life, the universe, and everything")
            else:
                print("=" +number)
#OTHERWISE
        else:
            print('''
            I don't understand your request. Here are the currently supported calculations: * or x; / or div; -, min, or sub; + or add; % or mod (modulo); sq or [] (square); ar or # (area); vol (volume); {} (cube); ex (exponents); and root (roots). Sorry for the inconvenience
            ''')
print()
print("Welcome to Palc!")
palc() #run the Calc() command above
#EOF