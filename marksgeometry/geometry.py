import math

class Square():
    def __init__(self, side=None):
        self.side = side
        if side is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return str(self.side ** 2) + "cm²"
class Rectangle():
    def __init__(self, base=None, height=None):
        self.base = base
        self.height = height
        if base is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return str(self.base * self.height) + "cm²"


class Triangle():
    def __init__(self, base=None, height=None):
        self.base = base
        self.height = height
        if base is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")
    def area(self):
        return str(self.base * self.height / 2)
class RegularPolygon():
    def __init__(self, side=None, sidesnumber=None, apothem=None):
        self.side = side
        self.sidesnumber = sidesnumber
        self.apothem = apothem
        if side is None or sidesnumber is None or apothem is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return str(self.side * self.sidesnumber * self.apothem / 2) + "cm²"

class Circle():
    def __init__(self, radius=None):
        self.radius= radius
        if radius is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return str(math.pi * self.radius ** 2) + "cm²"
class Trapezoid():
    def __init__(self, largebase=None, smallbase=None, height=None):
        self.largebase = largebase
        self.smallbase = smallbase
        self.height = height
        if largebase is None or smallbase is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return str((self.largebase + self.smallbase) * self.height / 2) + "cm²"

class Rhombus():
    def __init__(self, largediagonal=None, smalldiagonal=None):
        self.largediagonal = largediagonal
        self.smalldiagonal = smalldiagonal
        if largediagonal is None or smalldiagonal is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return str(self.largediagonal * self.smalldiagonal / 2) + "cm²"

class Parallelogram():
    def __init__(self, base=None, height=None):
        self.base = base
        self.height = height
        if base is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return str(self.base * self.height) + "cm²"


class RegularPolygonPrism():
    def __init__(self, side=None, apothem=None, sidesnumber=None, height=None, base=None):
        self.side = side
        self.apothem = apothem
        self.sidesnumber = sidesnumber
        self.height = height
        self.base = base
        if side is None or apothem is None or sidesnumber is None or height is None or base is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(self.side * self.sidesnumber * self.apothem / 2 * self.height) + "cm³"
    def area(self):
        return str((2 * self.side *  self.sidesnumber * self.apothem / 2) + (self.base * self.height * self.sidesnumber)) + "cm²"

class TriangularPrism():
    def __init__(self, base=None, theight=None, pheight=None):
        self.base = base
        self.heighttriangle = theight
        self.heightpolygon = pheight
        if base is None or theight is None or pheight is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(self.base * self.heighttriangle / 2 * self.heightpolygon) + "cm³"
    def area(self):
        return str(2 * self.heighttriangle * self.base / 2 + (self.base * self.heighttriangle * 3)) + "cm²"


class QuadrangularPrism():
    def __init__(self, side1=None, side2=None, height=None, base=None):
        self.side1 = side1
        self.side2 = side2
        self.height = height
        self.base = base
        if side1 is None or side2 is None or height is None or base is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(self.side1 * self.side2 * self.height) + "cm³"

    def area(self):
        return str((2 * self.side1 * self.side2) + (self.base * self.height * 4)) + "cm²"

class RectangularPrism():
    def __init__(self, side1=None, side2=None, side3=None, height=None):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height
        if side1 is None or side2 is None or height is None or side3 is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")           


    def volume(self):
            return str(self.side1 * self.side2 * self.height) + "cm³"
    def area(self):
        return str(2 * self.side1 * self.side2 + self.side1 * self.side3 + self.side2 * self.side3) + "cm²"

class TrapezoidalPrism():
    def __init__(self, largebase=None, smallbase=None, baseheight=None, pheight=None, pbase=None):
        self.largebase = largebase
        self.smallbase = smallbase
        self.heightbase = baseheight
        self.heightpolygon = pheight
        self.basepolygon = pbase
        if largebase is None or smallbase is None or baseheight is None or pheight is None or pbase is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str((self.largebase + self.smallbase) * self.heightbase / 2 * self.heightpolygon) + "cm³"
    def area(self):

            return str((self.largebase + self.smallbase) * self.heightbase + self.basepolygon * self.heightpolygon * 4) + "cm²"
    

class Sphere():
    def __init__(self, radius=None):
        self.radius = radius
        if radius is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volum(self):
        return str(4/3 * math.pi * self.radius ** 3) + "cm³"
    def area(self):
        return str(4 * math.pi * self.radius ** 2) + "cm²"

class Cube():
    def __init__(self, side=None):
        self.side = side
        if side is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(self.side ** 3) + "cm³"
    def area(self):
        return str(6 * self.side ** 2) + "cm²"

class Cylinder():
    def __init__(self, radius=None, height=None):
        self.radius = radius
        self.height = height
        if radius is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(math.pi * self.radius** 2 * self.height) + "cm³"
    def area(self):
        return str(2 * math.pi * self.radius ** 2 + (2 * math.pi * self.radius * self.height)) + "cm²"

class Pyramid():
    def __init__(self, base=None, side=None, sidesnumber=None, apothem=None, side1=None, side2=None, height=None):
        self.side1 = side1
        self.side2 = side2
        self.height = height
        self.side = side
        self.base = base
        self.sidesnumber = sidesnumber
        self.apothem = apothem
        if side1 is None or side2 is None or height is None or side is None or sidesnumber is None or base is None or apothem is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(1/3 * self.side1 * self.side2 * self.height) + "cm³"
    def area(self):
        return str(self.side * self.sidesnumber * self.apothem + (self.base * self.height / 2 * self.sidesnumber)) + "cm²"

class Cone():
    def __init__(self, radius=None, geometry=None):
        self.radius = radius
        self.geometry = geometry
        if radius is None or geometry is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(1/3 * math.pi * self.radius ** 2 * self.geometry) + "cm³"
    def area(self):
        return str(math.pi * self.radius ** 2 + (math.pi * self.radius * self.geometry)) + "cm²"

class RhomboidalPrism():
    def __init__(self, largediagonal=None, smalldiagonal=None, height=None, base=None):
        self.largediagonal = largediagonal
        self.smalldiagonal = smalldiagonal
        self.height = height
        self.base = base
        if height is None or largediagonal is None or smalldiagonal is None or base is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")
    def volume(self):
        return str(self.largediagonal * self.smalldiagonal / 2 * self.height) + "cm³"
    def area(self):
        return str(2 * self.largediagonal * self.smalldiagonal / 2 + (self.base * self.height * 4)) + "cm²"
class Tetrahedron():
    def __init__(self, side=None, height=None):
        self.height = height
        self.side = side
        if height is None or side is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str((self.side ** 3) * (math.sqrt(2) / 12)) + "cm³"
    def area(self):
        return str(self.side ** 2 * math.sqrt(3)) + "cm²"

class Octohedron():
    def __init__(self, side=None):
        self.side = side
        if side is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        if self.side == 0:
            return str((self.side ** 3) * (math.sqrt(2) / 3)) + "cm³"
    def area(self):
        if self.side == 0:
            return str((self.side ** 2) * (2 * math.sqrt(3))) + "cm²"

class Dodecahedron():
    def __init__(self, side=None, apothem=None):
        self.side = side
        self.apothem = apothem
        if side is None or apothem is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(1/4 * (15 + 7 * math.sqrt(5)) * self.side ** 3) + "cm³"

    def area(self):
        return str(30 * self.side * self.apothem) + "cm²"

class Icosahedron():
    def __init__(self, side=None):
        self.side = side
        if side is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(5 * self.side ** 3 / 12 * math.sqrt(3 + math.sqrt(5))) + "cm³"
    
    def area(self):
        return str(5 * self.side ** 2 * math.sqrt(3)) + "cm²"
class PyramidTrunk():
    def __init__(self, sbside=None, sidesnumber=None, sbapothem=None, lbside=None, lbapothem=None, latlargebase=None, latsmallbase=None, latheight=None, height=None):
        self.sbside = sbside
        self.sidesnumber = sidesnumber
        self.sbapothem = sbapothem
        self.lbside = lbside
        self.lbapothem = lbapothem
        self.latlargebase = latlargebase
        self.latsmallbase = latsmallbase
        self.latheight = latheight
        self.height = height
        if sbside is None or height is None or sidesnumber is None or sbapothem is None or lbside is None or lbapothem is None or latlargebase is None or latsmallbase is None or latheight is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(1/3 * (self.sbside * self.sidesnumber * self.sbapothem / 2 + self.lbside * self.sidesnumber * self.lbapothem / 2 + math.sqrt(self.sbside * self.sidesnumber * self.sbapothem / 2 * self.lbside * self.sidesnumber * self.lbapothem / 2) * self.height)) + "cm³"
    
    def area(self):
        return str((self.sbside * self.sidesnumber * self.sbapothem / 2) + (self.lbside * self.sidesnumber * self.lbapothem / 2) + ((self.latlargebase + self.latsmallbase) * self.latheight / 2)) + "cm²"
    
class ConeTrunk():
    def __init__(self, sbradius=None, geometry=None, lbradius=None, height=None):
        self.sbradius = sbradius
        self.geometry = geometry
        self.lbradius = lbradius
        self.height = height
        if sbradius is None or geometry is None or lbradius is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return str(1/3 * (math.pi * self.lbradius ** 2 + math.pi * self.sbradius ** 2 + math.sqrt(math.pi * self.lbradius ** 2 * math.pi * self.sbradius ** 2) * self.height)) + "cm³"
    
    def area(self):
        return str(math.pi * self.lbradius ** 2 + math.pi * self.sbradius ** 2 + math.pi * (self.lbradius + self.sbradius) * self.geometry) + "cm²"