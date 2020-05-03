#SETUP
from sys import exit
import time
try:
    from root import *
except:
    log("Could not access file root.py")
    print("I can't find file root.py, and thus you cannot calculate roots.")
try:
    from func import *
except:
    log("Could not access file func.py")
    exit("I can't access the file func.py. This file is necessary for proper function of the Software.")
print("Loading...............\n")
time.sleep(2)
def palc():
    while True:
       for i in range (0, 13): #13 blank lines
            print()
#CALCULATION CHOICE
       calc = input("What calculation do you wish to do? (Type `?' for a list of commands)\nType: ")
       calc = calc.lower() #make variable "calc" lowercase
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
            log(("User squared number ", n, " got result ", (n * n)))
       elif calc == "[]":
            n = int(input("Number? "))
            log(("User squared number ", n, " got result ", (n * n)))
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
            area()
       elif calc == "#":
            area()
#VOLUME
       elif calc == "vol":
            uc()
#CUBE
       elif calc == "{}":
            cubedNumber = int(input("\nType the number to be cubed: "))
            print()
            print(cubedNumber ** 3) #Manually cube number
            log(("User cubed number ", cubedNumber, " got result ", (cubedNumber ** 3)))
            print()
#EXIT
       elif calc == "exit":
            log("User exited using `exit' command")
            exit("Looks like you exited.")
#EXPONENTS
       elif calc == "ex":
            try:
                origin = int(input("Original number?"))
                ex = int(input("Exponent? "))
                print(origin ** ex)
                logger("User exponented number ", origin, " with ", ex, "getting ", (origin ** ex))
#ROOTS
       elif calc == "root":
            root = input("Square root or cube root?(square/cube)")
            root = root.lower()
            if root == "square":
                num = input("Number to be rooted?")
                print("That equals.....\n", num ** 0.5)
                logger(("user sqrooted number ", (num**0.5)))
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
                logger("User got the easter egg")
            else:
                print("=" +number)
                logger("User used the `=' feature for number ", number)
#NUMBER SYSTEMS
       elif calc == "base":
            base()
#ORD
       elif calc == "ord":
           logger(("User ord'ed to get result ", result))
           result = str(ord(int(input("Type in the number to ord: "))))
           print("=", result)
#LOGARITHM
       elif calc == "log":
           log()
#MEMORY
       elif calc == "mem":
            memOrRecall = input("Would you like to set the memory or recall? (set / recall)\nType: ")
            #slot = input("What slot would you like to use? (Currently avaliable: 1)\nType: ") # For future, when I add memory slots
            if memOrRecall.lower() == "set":
                remember()
            elif memOrRecall.lower() == "recall":
                readMyMemory()
            else:
                print("You did not type an answer.\nAbort.")
#OTHERWISE
       elif calc == "":
            logger("User attempted to type nothing as a command")
            print("Type something!")
       elif calc is None:
            logger("User attempted to type nothing as a command")
            print("Type something!")
       else:
            print('''
            I don't understand your request. Here are the currently supported calculations: 
            * or x; / or div; -, min, or sub; + or add; % or mod (modulo); sq or [] (square); ar or # (area); vol (volume); {} (cube); ex (exponents); root (roots); = (equals); log (logarithm); mem (memory); and base (convert number system). Sorry for the inconvenience
            ''')
print("\nWelcome to Palc!")
try:
    palc() #run all that code
except KeyboardInterrupt: #if ^C
    logger("KeyboardInterrupt")
    exit("\nNote that you CAN type `exit' instead of the interrupt key")
except EOFError: #if ^D
    logger("EOFError")
    exit("\nWhy ^D? Why not just type `exit'?")
#except (ValueError, TypeError):
    #print("You typed in an invalid integer or float.")
except EOFError:
    print("An unknown error occured. For debugging info, see Line 136") #To debug, comment lines 135 and 136
#EOF
