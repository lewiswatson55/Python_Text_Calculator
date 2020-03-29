#SETUP
try:
    from root import *
except:
    print("Are you sure that the file root.py exists? You can't use command 'root'")
import time
print("Loading...............\n")
time.sleep(2)
import os
def palc():
    while True:
       for i in range (0, 13): #13 blank lines
            print()
#CALCULATION CHOICE
       calc = input("Calculation?  (type ? for help): ")
#HELP
       if calc == "?":
           print('''
            Currently supported: multiplication (*), division (/), addition (+), square (sq), subtraction (-), modulo (%), area (#), volume (vol), cube ({}), cube twice ({2}), exponents (ex), root (root), equals (=), and convert number systems (base). Type exit to exit. Commands are case-sensitive
            To access support: go to https://github.com/thetechrobo/support/
            To contribute: go to https://github.com/thetechrobo/python-text-calculator/
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
            n = int(input("Number? "))
            print(n * n)
       elif calc == "[]":
            n = int(input("Number? "))
            print(n * n)
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
            exec("area.py") 
       elif calc == "#":
            exec("area.py")
#VOLUME
       elif calc == "vol":
            exec("volume.py") #More secure than os.system but currently doesn't work because it doesnt call any functions FROM volume.py, os.system had the same problem
#CUBE
       elif calc == "{}":
            print()
            cubedNumber = int(input("Type the number to be cubed: "))
            print()
            print(cubedNumber * cubedNumber * cubedNumber) #Manually cube number
            print()
#EXIT
       elif calc == "exit":
            exit()
       elif calc == "EXIT":
            exit()
#EXPONENTS (had the idea during bike ride on 18/9/2019 19hsomething after the BBQ)
       elif calc == "ex":
            try:
                origin = int(input("Original number?"))
                ex = int(input("Exponent? ")
                print("That equals.......\n", origin ** ex)
            except ValueError:
                print("ERROR: try typing in a Number!")
#ROOTS
       elif calc == "root":
            root = input("Square root or cube root?(square/cube case-sensitive)")
            if root == "square":
                num = input("Number to be rooted?")
                print("That equals.....\n", num ** 0.5)
            elif root == "cube":
                cu()
#EASTER EGG!
       elif calc == "=":
            print()
            number = int(input("Type in a number: "))
            if number == 42:
                print("=42 -- the answer to life, the universe, and everything")
            else:
                print("=" +number)
#NUMBER SYSTEMS
       elif calc == "base":
            base = int(input('''What base would you like to use?
Available: 2 (binary) 8 (octo) 10 (decimal (normal)) 16 (hex)
Type 2, 8, 10, or 16: '''))
            if base == 2:
                result = bin(int(input("Type the original number: "))) #bin() the number
                printThis = "=" +str(result)
                print(printThis)
            elif base == 8:
                result = oct(int(input("Type the original number: "))) #oct() teh number
                printThis = "=" +str(result)
                print(printThis)
            elif base == 10:
                whichType = input("Which type is the Number (ord, binary, octo, or hex): ")
                if whichType == "ord":
                    result = int(ord(input("Type the original number: "))) #int() the number
                elif whichType == "binary":
                    result = int(bin(input("Type the original number: "))) #int() the number
                elif whichType == "octo":
                    result = int(oct(input("Type the original number: "))) #int() the number
                elif whichType == "hex":
                    result = int(hex(input("Type the original number: "))) #int() the number
                else:
                    print("type ord, binary, octo, hex")
                printThis = "=" +str(result)
                print(printThis)
            elif base == 16:
                result = hex(int(input("Type the original number: "))) #
                printThis = "=" +str(result)
                print(printThis)
#ORD
       elif calc == "ord":
           result = str(ord(int(input("Type in the number to ord: "))))
           print("=", result)
#OTHERWISE
       else:
            print('''
            I don't understand your request. Here are the currently supported calculations: 
            * or x; / or div; -, min, or sub; + or add; % or mod (modulo); sq or [] (square); ar or # (area); vol (volume); {} (cube); ex (exponents); root (roots); = (equals); and base (convert number system). Sorry for the inconvenience
            ''')
print("\nWelcome to Palc!")
try:
    palc() #run all that code
except KeyboardInterrupt: #if ^C
    print("\nNote that you CAN type exit instead of the interrupt key")
    exit()
except ValueError:
    print("You typed in an invalid integer / float")
except:
    print("An unknown error occured. For debugging info, see Line 236") #To debug, comment lines 235 and 236
#EOF
