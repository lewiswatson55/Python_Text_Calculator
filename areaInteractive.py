from areafunc import *
from area import *
done = 0
print('''Options:
1 - Equilateral triangle
2 - Right angle triangle
3 - Acute triangle
4 - Obtuse triangle
5 - Square
6 - Rectangle
8 - Parallelogram
9 - Rhombus
10 - Trapezium
11 - Circle
12 - Semicircle
13 - Circular sector
14 - Ring
15 - Ellipse''')
while done == 0:
    try:
        choice = int(input("Please type one:"))
    except (ValueError, TypeError):
        print("Please type an integer")
    if choice == 7:
        print("I was too lazy to change 7.")
    elif choice == 1:
        global done
        done = 1
        equ_triangle()
    elif choice == 2:
        global done
        done = 1
        right_triangle()
    elif choice == 3:
        done = 1
        acute_triangle()
    elif choice == 4:
        done = 1
        obtuse_triangle()
    elif choice == 5:
        done = 1
        square()
    elif choice == 6:
        done = 1
        rectangle()
    elif choice == 8:
        done = 1
        parallelogram()
    elif choice == 9:
        done = 1
        rhombus()
    elif choice == 10:
        done = 1
        trapezium()
    elif choice == 11:
        done = 1
        circle()
    elif choice == 12:
        done = 1
        semicircle()
    elif choice == 13:
        done = 1
        sector()
    elif choice == 14:
        done = 1
        ring()
    elif choice == 15:
        done = 1
        ellipse()