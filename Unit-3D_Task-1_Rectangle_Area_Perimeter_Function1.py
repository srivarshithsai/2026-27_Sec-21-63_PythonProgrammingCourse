def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

Length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

area, perimeter = rectangle(Length,breadth)

print("Area", area)
print("Perimeter", perimeter)
