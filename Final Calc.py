from math import *
def sums_x_y(x,y):                               
 return x + y
def subs(x,y):                                   
  return x - y
def mult(x,y):
  return x*y
def divide(x,y):
  return x/y
def expo(x,y):
  return (pow(x,y))
def remain(x,y):
  return x%y
def undrt(x):
  return (sqrt(numz))
def dec_to(x):
 return bin(numa)
def uppr(strng):
 return (ils.upper())


choice = int(input("\033[1;37;40m Enter Your Choice:-\033[1;37;40m '\033[33m'\n1.For SUMS:\n2.For Substraction:\n3.For Multuplication:\n4.For Divide:\n5.For Exponents:\n6.For Remainder:\n7.For Under Root:\n8.For Decimal To Binary:\n9.For UPPERCASE:"))
if(choice < 7):
    numx = float(input("'\033[34m'ENTER A NUMBER:\n"))
    numy = float(input("'\033[31m'ENTER ANOTHER NUMBER :\n"))
elif(choice == 7) :
    numz = float(input("'\033[32m'Enter Your Number:"))
elif(choice == 8):
    numa = int(input("'\033[35m'ENTER YOUR DECIMAL NUMBER:\n"))
elif(choice == 9):
    ils = str(input("Enter Your Lowercase String:\n"))
else :
    print("Invalid Input Please Check")



if choice == 1 :
 print(sums_x_y(numx,numy))
elif choice == 2 :
 print(subs(numx,numy))
elif choice == 3 :
 print(mult(numx,numy))
elif choice ==4 :
 print(divide(numx,numy))
elif choice== 5 :
 print(expo(numx,numy))
elif choice == 6 :
 print(remain(numx,numy))
elif choice == 7 :
 print(undrt(numz))
elif choice == 8 :
 print(dec_to(numa))
elif choice == 9:
  print(uppr(ils))


input('Press ENTER to exit')
