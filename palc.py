#SETUP
#THANKS TO https://simpleit.rocks/python/how-to-translate-a-python-project-with-gettext-the-easy-way/ and https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/ for their GETTEXT guides! :)
# THANKS TO @ErdoğanOnal for their comment on this SO question: https://stackoverflow.com/questions/61621821/any-secure-alternatives-for-this?noredirect=1#comment109002742_61621821
import sys, os
try: 
    import msvcrt 
    _IS_WINDOWS = True 
except ImportError: 
    import tty 
    import termios 
    _IS_WINDOWS = False 
import logging #so I can log
logging.basicConfig(filename="palc.log", level=logging.DEBUG) #set up logging
import gettext #to translate Palc
language = input("English or Francais? (do not add accents to letters/ne pas ajouter les accents aux lettres): ")
language = language.lower()
if language == "francais":
    logging.info("Set language to French")
    global lang_translations
    gettext.bindtextdomain('base', localedir="locales")
    lang_translations = gettext.translation('base',localedir='locales', languages=["fr"])
elif language == "english":
    logging.info("Set language to English")
    global l_translations
    gettext.bindtextdomain('base', localedir="locales")
    l_translations = gettext.translation('base', localedir='locales', languages=["en"])
try:
    lang_translations.install()
    _ = lang_translations.gettext
except:
    l_translations.install()
    _ = l_translations.gettext
couldNotFindRoot = False #so that I can prevent errors
from sys import exit as e #so that we can exit later on
import time
try:
    from root import *
except:
    couldNotFindRoot = True
    logging.error("Could not access file root.py")
    print(_("I can't find file root.py, and therefore you cannot calculate roots."))
try:
    from func import *
except:
    logging.critical("Could not access file func.py")
    e(_("I can't access the file func.py. This file is necessary for proper function of the Software."))
print(_("Loading...............\n"))
time.sleep(2)
def palc():
    while True:
       print(_("Press any key to continue..."), end='', flush=True) 
       if _IS_WINDOWS: 
           msvcrt.getch() 
       else: 
           fd = sys.stdin.fileno() 
           settings = termios.tcgetattr(fd) 
           try: 
               tty.setraw(sys.stdin.fileno()) 
               sys.stdin.read(1) 
           finally: 
               termios.tcsetattr(fd, termios.TCSADRAIN, settings)
       os.system('cls' if os.name == 'nt' else 'clear')
#CALCULATION CHOICE
       calc = input(_("What calculation do you wish to do? (Type `?' for a list of commands)\nType: "))
       calc = calc.lower() #make variable "calc" lowercase
#HELP
       if "?" in calc:
           logging.info("User needed help")
           help()
       elif "help" in calc:
           logging.info("User needed help")
           help()
#MULTIPLICATION
       elif "*" in calc:
            multi()
       elif "x" in calc:
            multi()
#SQUARE
       elif "sq" in calc:
            n = int(input(_("Number? ")))
            print(n * n)
            logging.info(("User squared number ", n, " got result ", (n * n)))
       elif "[]" in calc:
            n = int(input(_("Number? ")))
            logging.info(("User squared number ", n, " got result ", (n * n)))
            print(n * n)
#DIVISION
       elif "/" in calc:
            div()
       elif "div" in calc:
            div()
#SUBTRACTION
       elif "-" in calc:
            sub()
       elif "sub" in calc:
            sub()
       elif "min" in calc:
            sub()
#ADDITION
       elif "+" in calc:
            add()
       elif "add" in calc:
            add()
#MODULO
       elif "%" in calc:
            mod()
       elif "mod" in calc:
            mod()
#AREA
       elif "ar" in calc:
            area()
       elif "#" in calc:
            area()
       elif "area" in calc:
            area()
#VOLUME
       elif "vol" in calc:
            uc()
#CUBE
       elif "{}" in calc:
            cubedNumber = int(input("\nType the number to be cubed: "))
            print()
            print(cubedNumber ** 3) #Manually cube number
            logging.info(("User cubed number ", cubedNumber, " got result ", (cubedNumber ** 3)))
            print()
#EXIT
       elif "exit" in calc:
            logging.info("User exited using `exit' command")
            e("Looks like you exited.")
#EXPONENTS
       elif "ex" in calc:
            origin = int(input("Original number?"))
            ex = int(input("Exponent? "))
            print(origin ** ex)
            logging.info(("User exponented number ", origin, " with ", ex, "getting ", (origin ** ex)))
#ROOTS
       elif "root" in calc:
            if couldNotFindRoot is True:
                root = input("Square root or cube root?(square/cube)")
                root = root.lower()
                if "square" in root:
                    num = input("Number to be rooted?")
                    print(_("That equals.....\n", num ** 0.5))
                    logging.info(("user sqrooted number ", (num**0.5)))
                elif "cube" in root:
                    cu()
                else:
                    print(_("Currently I don't support the root you chose. Hopefully this will change :)"))
            else:
                print(_("The root.py file could not be found at startup. Therefore you cannot calculate roots."))
#EASTER EGG!
       elif "=" in calc:
            print()
            number = int(input("Type in a number: "))
            if number == 42:
                print(_("=42 -- the answer to life, the universe, and everything"))
                logging.info("User got the easter egg")
            else:
                print("=" +number)
                logging.info("User used the `=' feature for number ", number)
#NUMBER SYSTEMS
       elif "base" in calc:
            base()
#ORD
       elif "ord" in calc:
           logging.info(("User ord'ed to get result ", result))
           result = str(ord(int(input(_("Type in the number to ord: ")))))
           print("=", result)
#LOGARITHM
       elif "log" in calc:
           log()
#MEMORY
       elif "mem" in calc:
            memOrRecall = input("Would you like to set the memory or recall? (set / recall)\nType: ")
            if memOrRecall.lower() in "set":
                remember()
            elif memOrRecall.lower() in "recall":
                readMyMemory()
            else:
                print(_("You did not type an answer.\nAbort."))
                logging.error("User didn't type an answer in MEM function")
#OTHERWISE
       elif calc == "":
            logging.error("User attempted to type nothing as a command")
            print(_("Type something!"))
       elif calc is None:
            logging.error("User attempted to type nothing as a command")
            print(_("Type something!"))
       else:
            logging.error("User typed an invalid command")
            print(_('''
            I don't understand your request. Here are the currently supported calculations:
            * or x; / or div; -, min, or sub; + or add; % or mod (modulo); sq or [] (square); ar or # (area); vol (volume); {} (cube); ex (exponents); root (roots); = (equals); log (logarithm); mem (memory); and base (convert number system). Sorry for the inconvenience
            '''))
print(_("\nWelcome to Palc!"))
try:
    palc() #run all that code
except KeyboardInterrupt: #if ^C
    logging.info("KeyboardInterrupt")
    e(_("\nNote that you CAN type `exit' instead of the interrupt key"))
except EOFError: #if ^D
    logging.info("EOFError")
    e(_("\nWhy ^D? Why not just type `exit'?"))
except (ValueError, TypeError):
    logging.critical("ValueError or TypeError")
    print(_("You typed in an invalid integer or float. Or maybe the program needs debugging. Either way, it's a pretty big error."))
#except:
    #logging.critical("Unknown Error")
    #print(_("An unknown error occured. For debugging info, see Line 164")) #To debug, comment lines 162, 163 and 164
#EOF
