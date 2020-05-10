import logging
def getNum(): #ask for two numbers and then return to function
    n1 = int(input(_("Please enter the first number: ")))
    n2 = int(input(_("Please enter the second number: ")))
    logging.info(("Palc got two numbers: ", n1, " and ", n2))
    return n1, n2
def h():
    print(_('''
     Current list of commands: multiplication (*), division (/), addition (+), square (sq), subtraction (-), modulo (%), area (#), volume (vol), cube ({}), cube twice ({2}), exponents (ex), root (root), equals (=), logarithm (log), memory (mem), fibonacci sequence (fib), percentage (percent), and convert number systems (base). Type e to e.
     Bugs? Head on over to https://github.com/thetechrobo/support/
     To contribute: go to https://github.com/thetechrobo/python-text-calculator/
     '''))
def multi(): #multiplication
    n1, n2 = getNum()
    print(_("\nThat equals..."))
    print(n1 * n2)
    logging.info(("User multiplied ", n1, " by ", n2, " and got result ", (n1 * n2)))
def div(): #division
    n1, n2 = getNum()
    print(_("\nThat equals..."))
    try:
        print(n1 / n2)
    except ZeroDivisionError:
        print(_("Do not divide by zero!"))
        logging.error("User attempted to divide by zero.")
    except:
        print(_("There was an unknown issue dividing your Numbers..."))
    logging.info(("User divvied ", n1, " by ", n2, ", getting a result of ", (n1 / n2)))
def sub(): #subtraction
    n1, n2 = getNum()
    print(_("\nThat equals..."))
    print(n1 - n2)
    logging.info(("User subtracted ", n1, " to ", n2, " and got result ", (n1 - n2)))
def add(): #addition
    n1, n2 = getNum()
    print(_("\nThat equals..."))
    print(n1 + n2)
    logging.info(("User added ", n1, " to ", n2, " and got result ", (n1 + n2)))
def mod(): #modulo
    try:
        bigger = int(input(_("\nType the first number (greater): ")))
        smaller = int(input(_("Type the second number (smaller): ")))
    except (TypeError, ValueError):
        print(_("\nError!"))
        print(_("Invalid input (code 1)\n"))
        logging.error(("ERROR: attempted to modulo numbers ", bigger, " and ", smaller, ", but errored code 1."))
    if(abs(bigger)<abs(smaller)):
        print(_("\nError!"))
        print(_("The second number entered is greater than the first number (code 2)\n"))
        logging.error(("ERROR: attempted to modulo numbers ", bigger, " and ", smaller, ", but errored code 2."))
    else:
        print(_("\nThat equals..."))
        print(bigger-smaller*int(bigger/smaller))
        logging.info(("User attempted to modulo numbers ", bigger, " and ", smaller, ", and got result ", (bigger-smaller*int(bigger/smaller))))
        print()
def base():
    base = int(input('''What base would you like to use?
    Available: 2 (binary) 8 (octo) 10 (decimal (normal)) 16 (hex)
    Type 2, 8, 10, or 16: '''))
    if base == 2:
        result = bin(int(input(_("Type the original number: ")))) #bin() the number
        printThis = "=" +str(result)
        logging.info(("User binaried number ", result, ", getting a result of ", printThis))
        print(printThis)
    elif base == 8:
            result = oct(int(input(_("Type the original number: ")))) #oct() the number
            printThis = "=" +str(result)
            logging.info(("User oct'ed number ", result, ", getting a result of ", printThis))
            print(printThis)
    elif base == 10:
        goodanswer = False
        while goodanswer is False:
            whichType = input(_("Which type is the Number (ord, binary, octo, or hex): "))
            if whichType == "ord":
                goodanswer = True
                result = int(ord(input(_("Type the original number: ")))) #int() the number
            elif whichType == "binary":
                goodanswer = True
                result = int(bin(input(_("Type the original number: ")))) #int() the number
            elif whichType == "octo":
                goodanswer = True
                result = int(oct(input(_("Type the original number: ")))) #int() the number
            elif whichType == "hex":
                goodanswer = True
                result = int(hex(input(_("Type the original number: ")))) #int() the number
            else:
                print(_("That was an invalid answer. Try again."))
            printThis = "=" +str(result)
            logging.info(("User int'ed number ", result, ", getting a result of ", printThis))
            print(printThis)
    elif base == 16:
        result = hex(int(input(_("Type the original number: ")))) #ask for original number
        printThis = "=" +str(result)
        logging.info(("User hexed number ", result, ", getting a result of ", printThis))
        print(printThis)
def uc():
    import runpy
    logging.warning(("User ran `volume.py'. Log is currently unavailable for area and volume."))
    runpy.run_path(path_name='volInteractive.py')
def area():
    import runpy
    logging.warning(("User ran `area.py'. Log is currently unavailable for area and volume."))
    runpy.run_path(path_name='areaInteractive.py')
def log(): #https://stackoverflow.com/questions/33754670/calculate-logarithm-in-python
    import math
    while True:
        base = input(_("What base would you like to use? \nCurrentlysupported: 10 (base 10), e (natural)"))
        if base == "10":
            print(_("Using base 10"))
            number = int(input(_("What is the number? ")))
            print(math.log10(number))
            logging.info(("User used base 10 logarithm with number", number, ", getting a result of ", math.log10(number)))
            break
        elif base.lower() == "e":
            print(_("Using natural logarithm"))
            number = int(input(_("What is the number? ")))
            print(math.log(number))
            logging.info(("User used natural logarithm with number ", number, ", getting a result of ", math.log(number)))
            break
        else:
            print(_("The logarithm you typed is not available."))
            print(_("Try again."))
            logging.info(("User attempted to use a logarithm that is unavailable."))
def remember():
    print(_("This is the memory function.\nIt will save a number into a file that can be used later with Palc... Or you can just read it with a text editor."))
    toRemember = float(input(_("\nPlease enter the number to be saved: ")))
    slot = str(int(input(_("What slot would you like to use? (Hint: you can use any integer you want as long as you remember it)\nType: "))))
    toRemember = str(toRemember)
    memory = open(slot, "w+")
    memory.write(toRemember)
    logging.info(("Saved number ", toRemember, " to memory slot ", slot))
def readMyMemory():
    print(_("This is the remember function.\nIt will read a number that was previously stored in a file."))
    try:
        slot = str(int(input(_("What slot number did you use? "))))
        memory = open(slot, "r")
        print(_("Number: ", memory.read()))
        logging.info(("Retrieved number ", memory.read(), " from memory."))
    except:
        logging.info("There was an error retrieving the file from memory.")
        print(_("There was an error reading the file. Did you save the number by using the save function? Did you accidentally rename the file?"))
def cubeInternal(x):
    # all credit goes to user4466285's answer to "https://stackoverflow.com/questions/28014241/how-to-find-cube-root-using-python"
    if 0 <= x:
        return x**(1./3.)
    return -(-x)**(1./3.)
def cu():
    print(cubeInternal(int(input(_("Number to be rooted? ")))))
def fib():
    import runpy
    runpy.run_path(path_name="fibonacci.py")
def percentage(percent, whole):
    if whole == 0:
        return (_("Please do not type in a zero as the whole."))
    return (percent * whole) / 100.0
def whatIsPercent():
    origin = int(input(_("what is the ORIGINAL NUMBER? ")))
    percent = int(input(_("What is the PERCENTAGE? ")))
    print(percentage(percent, origin))
def getPercentage(part, whole):
    if whole == 0:
        return (_("Please do not type in a zero as the whole."))
    return 100 * float(part)/float(whole)
def getPercentageRN():
    origin = int(input(_("What is the number that would be 100%? ")))
    part = int(input(_("What is the number that you want to convert to percentage (e.g. this number out of the number that would be 100%)? ")))
    print(getPercentage(part, origin))
def calculateInterest():
    while True:
        origin = int(input(_("What is the original number? ")))
        rate = float(input(_("What is the rate of interest in percentage (without the percent sign)? ")))
        inRealNumbers = percentage(whole=origin, percent=rate)
        number = origin + inRealNumbers
        print(_(("The answer is ", number)))
        doItAgain = input("Would you like to do it again (Y/n)? ")
        doItAgain = doItAgain.lower()
        if doItAgain == "y":
            pass
        else:
            print(_("OK. Going back..."))
            break
def cosine():
    which = input(_("Would you like sine or inverse sine? (sin / inverse)\nType: "))
    which = which.lower()
    if which == "sin":
        print(_("Sine it is!"))
        number = float(input(_("Enter the number: ")))
        import math
        res = math.degrees(math.sin(number))
        print(res)
        logging.info(("User cos'ed number ", number, " getting result of ", res))
    elif which == "inverse":
        print(_("Inverse it is!"))
        number = float(input(_("Enter the number: ")))
