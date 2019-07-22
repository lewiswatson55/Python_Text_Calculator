from math import pi, sqrt


# Contains Volume Calculating Functions

#cube
def vol_cube(a: int) -> 'volume':
    '''
    Takes 'a' As The Side Of The Cube.
    Returns The Volume
    :param a: int
    :return: volume
    '''
    volume = pow(a, 3)
    return volume

#cuboid
def vol_cuboid(l: int, b: int, h: int) -> 'volume':
    '''
    Takes 'l','b','h' As Length, Breadth, Height Respectively.
    Returns The Volume.
    :param l: int
    :param b: int
    :param h: int
    :return: volume
    '''
    volume = l * b * h
    return volume

#cylinder
def vol_cylinder(r: int, h: int) -> 'volume':
    '''
    Takes 'r'&'h' as radius and height, respectively.
    Returns The Volume.
    :param r: int
    :param h: int
    :return: volume
    '''
    volume = pi * pow(r, 2) * h
    return volume

#hollow cylinder
def vol_hollow_cylinder(ro: int, rs: int, h: int) -> 'volume':
    '''
    Takes 'ro','rs','h' As Radius Of Hollow Space, Radius Of The Cylinder,
    Height Of The Cylinder Respectively.
    Returns The Volume.
    :param ro: int
    :param rs: int
    :param h: int
    :return: volume
    '''
    volume = 2 * pi * (ro + rs) * h
    return volume

#cone
def vol_cone(r: int, h: int) -> 'volume':
    '''
    Takes 'r','h' As The Radius and Height Of The Cone, Respectively.
    Returns The Volume.
    :param r: int
    :param h: int
    :return: volume
    '''
    volume = 1 / 3 * pi / pow(r, 2) * h
    return volume

#sphere
def vol_sphere(r: int) -> 'volume':
    '''
    Takes 'r' As The Radius of the Sphere.
    Returns The Volume.
    :param r: int
    :return: volume
    '''
    volume = 4 / 3 * pi * pow(r, 3)
    return volume

#hollow sphere
def vol_hollow_sphere(ro: int, rs: int) -> 'volume':
    '''
    Takes 'ro' and 'rs' As The Full Radius Of The Sphere,
    and Radius Of Hollow Space Of The Sphere, Respectively.
    Returns The Volume.
    :param ro: int
    :param rs: int
    :return: volume
    '''
    volume = 4 / 3 * pi * (pow(ro, 3) - pow(rs, 3))
    return volume

#prism base triangle
def vol_tri_prism(a: int, h: int) -> 'volume':
    '''
    Takes 'a'&'h' As The Length Of A Side Of The Base Triangle,
    and Height Of The Prism, Respectively.
    Returns The Volume.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = (sqrt(3) / 4 * pow(a, 2)) * h
    return volume

#prism base penta
def vol_penta_prism(a: int, h: int) -> 'volume':
    '''
    Takes 'a'&'h' As The Length Of The Side Of The Base Pentagon,
    and Height Of The Prism, Respectively.
    Returns The Volume.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = (sqrt(3) * pow(a, 2)) * h
    return volume


def vol_hexa_prism(a: int, h: int) -> 'volume':
    '''
    Takes 'a'&'h' As The Length Of The Side Of The Base Hexagon,
    and Height Of The Prism, Respectively.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = (2.5981 * pow(a, 2)) * h
    return volume

#pyr. base square
def vol_sqr_pyramid(a: int, h: int) -> 'volume':
    '''
    Takes 'a'&'h' As The Length Of The Side Of The Base Square,
    and Height Of The Pyramid, Respectively.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = (1 / 3 * h) * pow(a, 2)
    return volume

#pyr. base triangle
def vol_tri_pyramid(a: int, h: int) -> 'volume':
    '''
    Takes 'a'&'h' As The Length Of The Side Of The Base Triangle,
    and Height of the Pyramid, Respectively.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = 1 / 3 * h * (sqrt(3) / 4 * pow(a, 2))
    return volume

#pyramid base pentagon
def vol_penta_pyramid(a: int, h: int) -> 'volume':
    '''
    Takes 'a'&'h' As The Length Of The Side Of The Base Pentagon,
    and Height of the Pyramid, Respectively.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = 1 / 3 * h * (sqrt(3) * pow(a, 2))
    return volume

#Pyramid base hexagon
def vol_hexa_pyramid(a: int, h: int) -> 'volume':
    '''
    Takes 'a' and 'h' as the Length of the Side of the Base Hexagon,
    and Height of the Pyramid, Respectively.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = (1 / 3 * h) * (2.5981 * pow(a, 2))
    return volume
print('Forked version 0.1')
