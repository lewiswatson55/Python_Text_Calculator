#SETUP
from sys import exit
import time
import os
try:
    from root import *
except:
    print("I can't find file root.py, and thus you cannot run roots.")
try:
    from func inport *
except:
    exit("I can't access the file func.py. This file is necessary for proper function of the Software.")
print("Loading...............\n")
time.sleep(2)
def palc():
    while True:
       for i in range (0, 13): #13 blank lines
            print()
#CALCULATION CHOICE
       calc = input("Calculation?  (type ? for help): ")
       calc.lower() #make variable "calc" lowercase
#HELP
        if calc == "?":
            help()
        elif calc == "help":
            help()
#MULTIPLICATION
       elif calc == "*":
            multi()
       elif calc == "x":
            multi()
#SQUARE
       elif calc == "sq":
            n = int(input("Number? "))
            print(n * n)
       elif calc == "[]":
            n = int(input("Number? "))
            print(n * n)
#DIVISION
       elif calc == "/":
            div()
       elif calc == "div":
            div()
#SUBTRACTION
       elif calc == "-":
            sub()
       elif calc == "sub":
            sub()
       elif calc == "min":
            sub()
#ADDITION
       elif calc == "+":
            add()
       elif calc == "add":
            add()
#MODULO
       elif calc == "%":
            mod()
       elif calc == "mod":
            mod()
#AREA
       elif calc == "ar":
            print("Under construction")
       elif calc == "#":
            print("Under construction")
#VOLUME
       elif calc == "vol":
            print("Under construction")
#CUBE
       elif calc == "{}":
            cubedNumber = int(input("\nType the number to be cubed: "))
            print()
            print(cubedNumber * cubedNumber * cubedNumber) #Manually cube number
            print()
#EXIT
       elif calc == "exit":
            exit()
#EXPONENTS (had the idea during bike ride on 18/9/2019 19hsomething after the BBQ)
       elif calc == "ex":
            try:
                origin = int(input("Original number?"))
                ex = int(input("Exponent? ")
                print("That equals.......\n", origin ** ex)
            except ValueError or TypeError:
                print("ERROR: try typing in a Number!")
#ROOTS
       elif calc == "root":
            root = input("Square root or cube root?(square/cube case-sensitive)")
            if root == "square":
                num = input("Number to be rooted?")
                print("That equals.....\n", num ** 0.5)
            elif root == "cube":
                cu()
            else:
                print("Currently I don't support any other roots. Hopefully this will change :)")
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
            base()
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
