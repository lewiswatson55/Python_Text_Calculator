def sq():
    from math import *
    num2Root = input("Number to be rooted? ")
    print(sqrt(num2Root))
def cubeInternal(x):
    # all credit goes to user4466285's answer to "https://stackoverflow.com/questions/28014241/how-to-find-cube-root-using-python"
    if 0<=x: return x**(1./3.)
    return -(-x)**(1./3.)
def cube():
    cubeInternal()
    print(cube(input("Number to be rooted? ")))