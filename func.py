def getNum(): #ask for two numbers and then return to function
    n1 = int(input("Please enter the first number: "))
    n2 = int(input("Please enter the second number: "))
    return n1, n2
def help():
    print('''
     Current list of commands: multiplication (*), division (/), addition (+), square (sq), subtraction (-), modulo (%), area (#), volume (vol), cube ({}), cube twice ({2}), exponents (ex), root (root), equals (=), and convert number systems (base). Type exit to exit.
     Bugs? Head over to https://github.com/thetechrobo/support/
     To contribute: go to https://github.com/thetechrobo/python-text-calculator/
     ''')
def multi(): #multiplication
    n1, n2 = getNum()
    print("\nThat equals...")
    print(n1 * n2)
def div(): #division
    n1, n2 = getNum()
    print("\nThat equals...")
    print(n1 / n2)
def sub(): #subtraction
    n1, n2 = getNum()
    print("\nThat equals...")
    print(n1 - n2)
def add(): #addition
    n1, n2 = getNum()
    print("\nThat equals...")
    print(n1 + n2)
def mod(): #modulo
    try:
        bigger = int(input("\nType the first number (greater): "))
        smaller = int(input("Type the second number (smaller): "))
    except (TypeError, ValueError):
        print("\nError!")
        print("Invalid input (code 1)\n")
    if(abs(bigger)<abs(smaller)):
        print("\nError!")
        print("The second number entered is greater than the first number (code 2)\n")
    else:
        print("\nThat equals...")
        print(bigger-smaller*int(bigger/smaller))
        print()
def base():
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
                printThis = "type ord, binary, octo, hex"
            printThis = "=" +str(result)
            print(printThis)
    elif base == 16:
        result = hex(int(input("Type the original number: "))) #ask for original number
        printThis = "=" +str(result)
        print(printThis)
def uc():
    print("Under construction -- This feature currently has not been made interactive.")
def area():
    import runpy
    runpy.run_path(path_name='areaInteractive.py')