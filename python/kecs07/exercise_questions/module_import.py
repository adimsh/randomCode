# we will be importing various modules/functions from mensuration package

# import individual functions

from mensuration.triangle import area, equil_area, peri, herons_area
from mensuration.cylinder import TSA as surface_area

# import entire modules

import mensuration.square, mensuration.rectangle, mensuration.circle
# we can also do from mensuration import square, rectangle, circle

a = 5
b = 10
r = 7
d = 4
e = 3

# area
# triangle
print(area(a, b))

#circle
print(mensuration.circle.area(r))

#rectangle
print(mensuration.rectangle.area(a, b))

#cylinder
print(surface_area(r, d))