# marksgeometrys

A mathematical library to calculate many figures area or volume.

Developed by Marc Pérez (c) 2024

## Examples of How To Use

Calculate The Area of a 2D Figure

```python
from marksgeometrys import Square

print(Square(side=3).area())
```

Calculate The Area of a 3D Figure

```python
from marksgeometrys import Icosahedron

print(Icosahedron(side=10).area())
```

Calculate The Volume of a 3D Figure

```python
from marksgeometrys import PyramidTrunk

print(PyramideTrunk(sbside=5, sidesnumber=7, sbapothem=4, lbside=10, lbapothem=8, latlargebase=8, latsmallbase=5, latheight=9, height=10.5).volume())
```
