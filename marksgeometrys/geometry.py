import math


class Square():
    def __init__(self, side=None, unit="cm"):
        self.side = side
        self.unit = unit
        if side is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return self.side ** 2

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Rectangle():
    def __init__(self, base=None, height=None, unit="cm"):
        self.base = base
        self.height = height
        self.unit = unit
        if base is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return self.base * self.height

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Triangle():
    def __init__(self, base=None, height=None, unit="cm"):
        self.base = base
        self.height = height
        self.unit = unit
        if base is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return self.base * self.height / 2

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class RegularPolygon():
    def __init__(self, side=None, sidesnumber=None, apothem=None, unit="cm"):
        self.side = side
        self.sidesnumber = sidesnumber
        self.apothem = apothem
        self.unit = unit
        if side is None or sidesnumber is None or apothem is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return self.side * self.sidesnumber * self.apothem / 2

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Circle():
    def __init__(self, radius=None, unit="cm"):
        self.radius = radius
        self.unit = unit
        if radius is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return math.pi * self.radius ** 2

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Trapezoid():
    def __init__(self, largebase=None, smallbase=None, height=None, unit="cm"):
        self.largebase = largebase
        self.smallbase = smallbase
        self.height = height
        self.unit = unit
        if largebase is None or smallbase is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return (self.largebase + self.smallbase) * self.height / 2

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Rhombus():
    def __init__(self, largediagonal=None, smalldiagonal=None, unit="cm"):
        self.largediagonal = largediagonal
        self.smalldiagonal = smalldiagonal
        self.unit = unit
        if largediagonal is None or smalldiagonal is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return self.largediagonal * self.smalldiagonal / 2

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Parallelogram():
    def __init__(self, base=None, height=None, unit="cm"):
        self.base = base
        self.height = height
        self.unit = unit
        if base is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def area(self):
        return self.base * self.height

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class RegularPolygonPrism():
    def __init__(self, side=None, apothem=None, sidesnumber=None, height=None, base=None, unit="cm"):
        self.side = side
        self.apothem = apothem
        self.sidesnumber = sidesnumber
        self.height = height
        self.base = base
        self.unit = unit
        if side is None or apothem is None or sidesnumber is None or height is None or base is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return self.side * self.sidesnumber * self.apothem / 2 * self.height

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return (2 * self.side * self.sidesnumber * self.apothem / 2) + (self.base * self.height * self.sidesnumber)

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class TriangularPrism():
    def __init__(self, base=None, theight=None, pheight=None, unit="cm"):
        self.base = base
        self.heighttriangle = theight
        self.heightpolygon = pheight
        self.unit = unit
        if base is None or theight is None or pheight is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return self.base * self.heighttriangle / 2 * self.heightpolygon

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return 2 * self.heighttriangle * self.base / 2 + (self.base * self.heighttriangle * 3)

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class QuadrangularPrism():
    def __init__(self, side1=None, side2=None, height=None, base=None, unit="cm"):
        self.side1 = side1
        self.side2 = side2
        self.height = height
        self.base = base
        self.unit = unit
        if side1 is None or side2 is None or height is None or base is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return self.side1 * self.side2 * self.height

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return (2 * self.side1 * self.side2) + (self.base * self.height * 4)

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class RectangularPrism():
    def __init__(self, side1=None, side2=None, side3=None, height=None, unit="cm"):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height
        self.unit = unit
        if side1 is None or side2 is None or height is None or side3 is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return self.side1 * self.side2 * self.height

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return 2 * self.side1 * self.side2 + self.side1 * self.side3 + self.side2 * self.side3

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class TrapezoidalPrism():
    def __init__(self, largebase=None, smallbase=None, baseheight=None, pheight=None, pbase=None, unit="cm"):
        self.largebase = largebase
        self.smallbase = smallbase
        self.heightbase = baseheight
        self.heightpolygon = pheight
        self.basepolygon = pbase
        self.unit = unit
        if largebase is None or smallbase is None or baseheight is None or pheight is None or pbase is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return (self.largebase + self.smallbase) * self.heightbase / 2 * self.heightpolygon

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return (self.largebase + self.smallbase) * self.heightbase + self.basepolygon * self.heightpolygon * 4

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Sphere():
    def __init__(self, radius=None, unit="cm"):
        self.radius = radius
        self.unit = unit
        if radius is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return 4/3 * math.pi * self.radius ** 3

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Cube():
    def __init__(self, side=None, unit="cm"):
        self.side = side
        self.unit = unit
        if side is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return self.side ** 3

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return 6 * self.side ** 2

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Cylinder():
    def __init__(self, radius=None, height=None, unit="cm"):
        self.radius = radius
        self.height = height
        self.unit = unit
        if radius is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return 2 * math.pi * self.radius ** 2 + (2 * math.pi * self.radius * self.height)

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Pyramid():
    def __init__(self, base=None, side=None, sidesnumber=None, apothem=None, side1=None, side2=None, height=None, unit="cm"):
        self.side1 = side1
        self.side2 = side2
        self.height = height
        self.side = side
        self.base = base
        self.sidesnumber = sidesnumber
        self.apothem = apothem
        self.unit = unit
        if side1 is None or side2 is None or height is None or side is None or sidesnumber is None or base is None or apothem is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return 1/3 * self.side1 * self.side2 * self.height

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return self.side * self.sidesnumber * self.apothem + (self.base * self.height / 2 * self.sidesnumber)

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Cone():
    def __init__(self, radius=None, geometry=None, unit="cm"):
        self.radius = radius
        self.geometry = geometry
        self.unit = unit
        if radius is None or geometry is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return 1/3 * math.pi * self.radius ** 2 * self.geometry

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return math.pi * self.radius ** 2 + (math.pi * self.radius * self.geometry)

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class RhomboidalPrism():
    def __init__(self, largediagonal=None, smalldiagonal=None, height=None, base=None, unit="cm"):
        self.largediagonal = largediagonal
        self.smalldiagonal = smalldiagonal
        self.height = height
        self.base = base
        self.unit = unit
        if height is None or largediagonal is None or smalldiagonal is None or base is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return self.largediagonal * self.smalldiagonal / 2 * self.height

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return 2 * self.largediagonal * self.smalldiagonal / 2 + (self.base * self.height * 4)

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Tetrahedron():
    def __init__(self, side=None, height=None, unit="cm"):
        self.height = height
        self.side = side
        self.unit = unit
        if height is None or side is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return (self.side ** 3) * (math.sqrt(2) / 12)

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return self.side ** 2 * math.sqrt(3)

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Octohedron():
    def __init__(self, side=None, unit="cm"):
        self.side = side
        self.unit = unit
        if side is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return (self.side ** 3) * (math.sqrt(2) / 3)

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return (self.side ** 2) * (2 * math.sqrt(3))

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Dodecahedron():
    def __init__(self, side=None, apothem=None, unit="cm"):
        self.side = side
        self.apothem = apothem
        self.unit = unit
        if side is None or apothem is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return 1/4 * (15 + 7 * math.sqrt(5)) * self.side ** 3

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return 30 * self.side * self.apothem

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class Icosahedron():
    def __init__(self, side=None, unit="cm"):
        self.side = side
        self.unit = unit
        if side is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return 5 * self.side ** 3 / 12 * math.sqrt(3 + math.sqrt(5))

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return 5 * self.side ** 2 * math.sqrt(3)

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class PyramidTrunk():
    def __init__(self, sbside=None, sidesnumber=None, sbapothem=None, lbside=None, lbapothem=None, latlargebase=None, latsmallbase=None, latheight=None, height=None, unit="cm"):
        self.sbside = sbside
        self.sidesnumber = sidesnumber
        self.sbapothem = sbapothem
        self.lbside = lbside
        self.lbapothem = lbapothem
        self.latlargebase = latlargebase
        self.latsmallbase = latsmallbase
        self.latheight = latheight
        self.height = height
        self.unit = unit
        if sbside is None or height is None or sidesnumber is None or sbapothem is None or lbside is None or lbapothem is None or latlargebase is None or latsmallbase is None or latheight is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return 1/3 * (self.sbside * self.sidesnumber * self.sbapothem / 2 + self.lbside * self.sidesnumber * self.lbapothem / 2 + math.sqrt(self.sbside * self.sidesnumber * self.sbapothem / 2 * self.lbside * self.sidesnumber * self.lbapothem / 2) * self.height)

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return (self.sbside * self.sidesnumber * self.sbapothem / 2) + (self.lbside * self.sidesnumber * self.lbapothem / 2) + ((self.latlargebase + self.latsmallbase) * self.latheight / 2)

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"


class ConeTrunk():
    def __init__(self, sbradius=None, geometry=None, lbradius=None, height=None, unit="cm"):
        self.sbradius = sbradius
        self.geometry = geometry
        self.lbradius = lbradius
        self.height = height
        self.unit = unit
        if sbradius is None or geometry is None or lbradius is None or height is None:
            attribute_names = ", ".join(vars(self).keys())
            raise ValueError(f"All parameters must be provided: {attribute_names}")

    def volume(self):
        return 1/3 * (math.pi * self.lbradius ** 2 + math.pi * self.sbradius ** 2 + math.sqrt(math.pi * self.lbradius ** 2 * math.pi * self.sbradius ** 2) * self.height)

    def volume_formatted(self):
        return f"{self.volume()}{self.unit}³"

    def area(self):
        return math.pi * self.lbradius ** 2 + math.pi * self.sbradius ** 2 + math.pi * (self.lbradius + self.sbradius) * self.geometry

    def area_formatted(self):
        return f"{self.area()}{self.unit}²"