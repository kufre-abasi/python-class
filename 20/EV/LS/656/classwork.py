#CLASS WORK
# Calculate the total area of the hexagon
import math

def heron_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def hexagon_area(side_lengths):
    total_area = 0
    for a, b, c in side_lengths:
        total_area += heron_area(a, b, c)
    return total_area

# Assuming each triangular section is an isosceles triangle with sides 50, 50, and 35 (given in the image)
side_lengths = [
    (50, 50, 35),  # P1
    (50, 50, 35),  # P2
    (50, 50, 35),  # P3
    (50, 50, 35),  # P4
    (50, 50, 35),  # P5
    (50, 50, 35)   # P6
]

# Calculate the total area of the hexagon
total_hexagon_area = hexagon_area(side_lengths)
print("Total area of the hexagon:", total_hexagon_area)
