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
    rh(a, h)
def trapezium():
    from area import trapezium
    a = int(input("What is the length of the 1st set of parallel sides? "))
    b = int(input("What is the length of the 2nd set of parallel sides? "))
    h = int(input("What is the height of the trapezium? "))
    trapezium(a, b, h)
def circle():
    from area import circle
    r = int(input("What is the radius of the circle? "))
    circle(r)
def semicircle():
    from area import semicircle
    r = int(input("What is the radius of the semicircle? "))
    semicircle(r)
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
