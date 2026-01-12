#WAP using user defined function that accepts length and breadth as arguments and returns area and perimeter

l = float(input("Enter length of the rectangle: "))
b = float(input("Enter breadth of the rectangle: "))

def rect_anp(length, breadth):
    area = length * breadth
    peri = 2*(length + breadth)
    values = (area, peri) #alt: return (area, peri)
    return values

temp = rect_anp(l, b) #alt: area, peri = rect_anp(l, b); values in tuple assigned in order
print("Area:", temp[0], "Perimeter:", temp[1])