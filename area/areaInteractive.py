from areafunc import *
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
while True:
    try:
        choice = int(input("Please type one: "))
    except (ValueError, TypeError):
        print("Please type an integer")
    if choice == 7:
        print("I was too lazy to change 7.")
    elif choice == 1:
        equ_triangle()
        break
    elif choice == 2:
        right_triangle()
        break
    elif choice == 3:
        acute_triangle()
        break
    elif choice == 4:
        obtuse_triangle()
        break
    elif choice == 5:
        square()
        break
    elif choice == 6:
        rectangle()
        break
    elif choice == 8:
        parallelogram()
        break
    elif choice == 9:
        rhombus()
        break
    elif choice == 10:
        trapezium()
        break
    elif choice == 11:
        circle()
        break
    elif choice == 12:
        semicircle()
        break
    elif choice == 13:
        sector()
        break
    elif choice == 14:
        ring()
        break
    elif choice == 15:
        ellipse()
        break   
