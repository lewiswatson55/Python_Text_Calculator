def cuvol():
    from volume import vol_cube as cu
    a = int(input("What length is the side of the cube? "))
    cu(a)
def cuboid():
    from volume import vol_cuboid as cub
    b = int(input("What length is the breadth of the cuboid? "))
    h = int(input("What length is the height of the triangle? "))
    cub(b=b, h=h, l=l)
def cylindervol():
    from volume import vol_cylinder as cy
    r = int(input("What is the radius of the cylinder? "))
    h = int(input("what is the height of the cylinder? "))
    cy(r, h)
def hollow_cylinder():
    from volume import vol_hollow_cylinder as cy
    ro = int(input("What is the radius of the hollow space? "))
    rs = int(input("what is the radius of the cylinder? "))
    h = int(input("What is the height of the cylinder? "))
    obtri(ro, rs, h)
def cone():
    from volume import vol_cone as co
    r = int(input("What is the radius of the cone? "))
    h = int(input("What is the height of the cone? "))
    sq(a)
def sphere():
    from volume import vol_sphere as sp
    r = int(input("What is the radius of the rectangle? "))
    sp(r)
def hollow_sphere():
    from volume import vol_hollow_sphere as sp
    ro = int(input("What is the radius of the sphere? "))
    rs = int(input("What is the radius of the hollow space? "))
    para(ro, rs)
def triprism():
    from volume import vol_tri_prism as tripr
    a = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the prism? "))
    tripr(a, h)
def pentprism():
    from volume import vol_penta_prism as pentaprism
    a = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the prism? "))
    pentaprism(a, h)
def hexaprism():
    from volume import vol_hexa_prism as hexy
    r = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the prism? "))
    hexy(r, h)
def squiramid():
    from volume import vol_sqr_pyramid as sqp
    a = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the pyramid? "))
    sqp(a, h)
def triramid():
    from volume import vol_tri_pyramid as trip
    a = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the pyramid? "))
    trip(a, h)
def pentapyr():
    from volume import vol_penta_pyramid as pentapenta
    ro = int(input("What is the length of the side of the base? "))
    rs = int(input("What is the height of the pyramid? "))
    pentapenta(ro, rs)
def hexramid():
    from volume import vol_hexa_pyramid as hexyhexa
    a = int(input("What is the length of the side of the base? "))
    h = int(input("What is the height of the pyramid? "))
hexyhexa(a, h)
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
