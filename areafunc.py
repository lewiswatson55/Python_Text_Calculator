def equ_triangle():
    from area import equtri as eq
    a = int(input("What length is the side of the triangle? "))
    eq(a)
def right_triangle():
    from area import righttri as ri
    b = int(input("What length is the base of the triangle? "))
    h = int(input("What length is the height of the triangle? "))
    ri(b, h)
def acute_triangle():
    from area import actri as ac
    a = int(input("What is the length of the first side? "))
    b = int(input("what is the length of the second side? "))
    c = int(input("What is the length of the third side? "))
    ac(a, b, c)
def obtuse_triangle():
    from area import obtri
    a = int(input("What is the length of the first side? "))
    b = int(input("what is the length of the second side? "))
    c = int(input("What is the length of the third side? "))
    obtri(a, b, c)
def square():
    from area import sq
    a = int(input("What is the length of the side of the square? "))
    sq(a)
def rectangle():
    from area import rectangle
    l = int(input("What is the length of the rectangle? "))
    b = int(input("What is the height of the rectangle? "))
    rectangle(l, b)
def parallelogram():
    from area import parallelogram as para
    b = int(input("What is the length of the base? "))
    h = int(input("What is the height of the shape? "))
    para(b, h)
def rhombus():
    from area import rhombus as rh
    do = int(input("What is the length of the first diagonal? "))
    ds = int(input("What is the length of the 2nd diagonal? "))
    rh(do, ds)
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