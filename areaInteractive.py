from areafunc import *
done = False
def true():
    done = True
while done == False:
print('''Please select one:
1 - Equilateral triangle
2 - Right angle triangle
3 - Acute triangle
4 - Obtuse triangle
5 - Square
6 - Rectangle
7 - See more''')
choice = input()
if choice == 7:
    print('''
    8 - Parallelogram
    9 - Rhombus
    10 - Trapezium
    11 - Circle
    12 - Semicircle
    13 - Circular sector
    14 - Ring
    15 - Ellipse''')
elif choice == 1:
    true()
    equ_triangle()
elif choice == 2:
    true()
    right_triangle()
elif choice == 3:
    true()
    acute_triangle()
elif choice == 4:
    true()
    obtuse_triangle()
elif choice == 5:
    true()
    square()
elif choice == 6:
    true()
    rectangle()
elif choice == 8:
    true()
    parallelogram()
elif choice == 9:
    true()
    rhombus()
elif choice == 10:
    true()
    trapezium()
elif choice == 11:
    true()
    circle()
elif choice == 12:
    true()
    semicircle()
elif choice == 13:
    true()
    sector()
elif choice == 14:
    true()
    ring()
elif choice == 15:
    true()
    ellipse()