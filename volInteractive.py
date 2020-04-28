from volfunc import *
print('''Options:
1 - Cube
2 - Cuboid
3 - Cylinder
4 - Hollow cylinder
5 - Cone
6 - Sphere
8 - Hollow sphere
9 - Triangular prism
10 - Pentagonal prism
11 - Hexagonal prism
12 - Square-based pyramid
13 - Triangular pyramid
14 - Pentagon-based pyramid
15 - Hexagon-based pyramid''')
while True:
    try:
        choice = int(input("Please type one: "))
    except (ValueError, TypeError):
        print("Please type an integer")
    if choice == 7:
        print("Sorry, that was not an option. >:)")
    elif choice == 1:
        cuvol()
        break
    elif choice == 2:
        cuboid()
        break
    elif choice == 3:
        cylindervol()
        break
    elif choice == 4:
        hollow_cylinder()
        break
    elif choice == 5:
        cone()
        break
    elif choice == 6:
        sphere()
        break
    elif choice == 8:
        hollow_sphere()
        break
    elif choice == 9:
        triprism()
        break
    elif choice == 10:
        pentprism()
        break
    elif choice == 11:
        hexaprism()
        break
    elif choice == 12:
        squiramid()
        break
    elif choice == 13:
        trimarid()
        break
    elif choice == 14:
        pantapyr()
        break
    elif choice == 15:
        hexramid()
        break   
