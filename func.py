def 2num(): #ask for two numbers and then return to function
    n1 = int(input("Please enter the first number: "))
    n2 = int(input("Please enter the second number: "))
    return n1, n2
def help():
    print('''
     Currently supported: multiplication (*), division (/), addition (+), square (sq), subtraction (-), modulo (%), area (#), volume (vol), cube ({}), cube twice ({2}), exponents (ex), root (root), equals (=), and convert number systems (base). Type exit to exit.
     To access support: go to https://github.com/thetechrobo/support/
     To contribute: go to https://github.com/thetechrobo/python-text-calculator/
     ''')
def multi(): #multiplication
    2num()
    print("\nThat equals...")
    print(n1 * n2)
def div(): #division
    2num()
    print("\nThat equals...")
    print(n1 / n2)
def sub(): #subtraction
    2num()
    print("\nThat equals...")
    print(n1 - n2)
def add(): #addition
    2num()
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