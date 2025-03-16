'''
Name: Amir Khoshpour
Student ID: 100993995
'''
from math import pi

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")

def trapezium_area(a, b, h):
    if all(isinstance(i, (int, float)) and i >= 0 for i in [a, b, h]):
        return 0.5 * (a + b) * h
    else:
        raise ValueError("All inputs must be non-negative numbers.")

def ellipse_area(a, b):
    if isinstance(a, (int, float)) and a >= 0 and isinstance(b, (int, float)) and b >= 0:
        return pi * a * b
    else:
        raise ValueError("Invalid semi-axes. Must be non-negative numbers.")

def rhombus_area(d1, d2):
    if isinstance(d1, (int, float)) and d1 >= 0 and isinstance(d2, (int, float)) and d2 >= 0:
        return 0.5 * d1 * d2
    else:
        raise ValueError("Invalid diagonals. Must be non-negative numbers.")


if __name__ == "__main__":
    print("Testing the area functions...")
    try:
        print(f"Circle Area (r=3): {circle_area(3)}")
        print(f"Trapezium Area (a=3, b=5, h=4): {trapezium_area(3, 5, 4)}")
        print(f"Ellipse Area (a=3, b=5): {ellipse_area(3, 5)}")
        print(f"Rhombus Area (d1=3, d2=5): {rhombus_area(3, 5)}")
    except ValueError as e:
        print(f"Error: {e}")
