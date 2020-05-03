from volume import *
def cuvol():
    a = int(input("What length is the side of the cube? "))
    vol_cube(a)
def cuboid():
    b = int(input("What length is the breadth of the cuboid? "))
    h = int(input("What length is the height of the triangle? "))
    vol_cuboid(b=b, h=h, l=l)
def cylindervol():
    r = int(input("What is the radius of the cylinder? "))
    h = int(input("what is the height of the cylinder? "))
    vol_cylinder(r, h)
def hollow_cylinder():
    ro = int(input("What is the radius of the hollow space? "))
    rs = int(input("what is the radius of the cylinder? "))
    h = int(input("What is the height of the cylinder? "))
    vol_hollow_cylinder(ro, rs, h)
def cone():
    r = int(input("What is the radius of the cone? "))
    h = int(input("What is the height of the cone? "))
    vol_cone(a)
def sphere():
    r = int(input("What is the radius of the rectangle? "))
    vol_sphere(r)
def hollow_sphere():
    ro = int(input("What is the radius of the sphere? "))
    rs = int(input("What is the radius of the hollow space? "))
    vol_hollow_sphere(ro, rs)
def triprism():
    a = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the prism? "))
    vol_tri_prism(a, h)
def pentprism():
    a = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the prism? "))
    vol_penta_prism(a, h)
def hexaprism():
    r = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the prism? "))
    vol_hexa_prism(r, h)
def squiramid():
    a = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the pyramid? "))
    vol_sqr_pyramid(a, h)
def triramid():
    a = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the pyramid? "))
    vol_tri_pyramid(a, h)
def pentapyr():
    ro = int(input("What is the length of the side of the base? "))
    rs = int(input("What is the height of the pyramid? "))
    vol_penta_pyramid(ro, rs)
def hexramid():
    a = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the pyramid? "))
    vol_hexa_pyramid(a, h)
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
        pentapyr()
        break
    elif choice == 15:
        hexramid()
        break   
