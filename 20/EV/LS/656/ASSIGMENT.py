# ASSIGMENT 
# Program to calculate the area of a polygon with given coordinates
def compute_area(coords):
    n = len(coords)  # Number of vertices
    area = 0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

# Coordinates from the image
coordinates = [
    (391687.537, 553798.753),  # P1
    (391862.721, 553797.475),  # P2
    (391650.979, 553806.169),  # P3
    (391649.124, 553826.698),  # P4
    (391656.860, 553839.871),  # P5
    (391663.943, 553841.014)   # P6
]

# Calculate the area
area = compute_area(coordinates)
print(f"The area of the polygon is: {area} square units")
