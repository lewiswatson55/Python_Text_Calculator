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
    a = int(input("What is the length of the base? "))
    h = int(input("What is the height of the pyramid? "))
    sqp(a, h)
def sector():
    from area import cirsector
    r = int(input("What is the radius of the circular sector? "))
    cirsector(r)
def ring():
    from area import ring
    ro = int(input("What is the radius of the outer circle? "))
    rs = int(input("What is the radius of the inner circle? "))
    ring(ro, rs)
def ellipse():
    from area import ellipse
    a = int(input("What is the length of the major axis? "))
    b = int(input("What is the length of the minor axis? "))
    ellipse(a, b)
