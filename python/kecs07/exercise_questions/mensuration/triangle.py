def area(base, height):
    return (1/2*base*height)

def equil_area(side):
    return (3**0.5/4*side**2)

def herons_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c))**0.5

def peri(a, b, c):
    return a + b + c