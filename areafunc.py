def equ_triangle():
    a = input("What length is the side of the triangle? ")
    equtri_area(a)
def right_triangle():
    b = input("What length is the base of the triangle? ")
    h = input("What length is the height of the triangle? ")
    righttri_area(b, h)
def acute_triangle():
    a = input("What is the length of the first side? ")
    b = input("what is the length of the second side? ")
    c = input("What is the length of the third side? ")
    acute_triangle_area(a, b, c)
def obtuse_triangle():
    a = input("What is the length of the first side? ")
    b = input("what is the length of the second side? ")
    c = input("What is the length of the third side? ")
    obtuse_triangle_area(a, b, c)
def square():
    a = input("What is the length of the side of the square? ")
    square_area(a)
def rectangle():
    l = input("What is the length of the rectangle? ")
    b = input("What is the height of the rectangle? ")
    rectangle_area(l, b)
def parallelogram():
    b = input("What is the length of the base? ")
    h = input("What is the height of the shape? ")
    parallelogram_area(b, h)
def rhombus():
    do = input("What is the length of the first diagonal? ")
    ds = input("What is the length of the 2nd diagonal? ")
    rhombus_area(do, ds)
def trapezium():
    a = input("What is the length of the 1st set of parallel sides? ")
    b = input("What is the length of the 2nd set of parallel sides? ")
    h = input("What is the height of the trapezium? ")
    trapezium_area(a, b, h)
def circle():
    r = input("What is the radius of the circle? ")
    circle_area(r)
def semicircle():
    r = input("What is the radius of the semicircle? ")
    semicircle_area(r)
def sector():
    r = input("What is the radius of the circular sector? ")
    cirsector_area(r)
def ring():
    ro = input("What is the radius of the outer circle? ")
    rs = input("What is the radius of the inner circle? ")
    cirring_area(ro, rs)
def ellipse():
    a = input("What is the length of the major axis? ")
    b = input("What is the length of the minor axis? ")
    ellipse_area(a, b)