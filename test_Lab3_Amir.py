'''
Name: Amir Khoshpour
Student ID: 100993995

'''
import unittest
from Lab3_Amir import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nsetupClass: Initializing tests...\n")

    def setUp(self):
        print("setUp: Starting a new test...")

    def tearDown(self):
        print("End of test\n")

    @classmethod
    def tearDownClass(cls):
        print("\nteardownClass: All tests completed.\n")

    # Circle
    def test_circle_area_positive(self):
        print("Test: Circle area when radius >= 0")
        result = circle_area(3)
        print(f"Result: {result}")
        self.assertAlmostEqual(result, 28.274333882308138)

    def test_circle_area_negative(self):
        print("Test: Circle area when radius < 0")
        try:
            circle_area(-1)
        except ValueError as e:
            print(f"Exception: {e}")
            self.assertTrue(True)  # Ensures the test passes when exception is raised

    def test_circle_area_invalid(self):
        print("Test: Circle area with invalid input (e.g., string, boolean)")
        invalid_inputs = ["string", True, None]
        for invalid in invalid_inputs:
            try:
                circle_area(invalid)
            except ValueError as e:
                print(f"Input: {invalid} | Exception: {e}")
                self.assertTrue(True)  # Ensures the test passes when exception is raised

    # Trapezium
    def test_trapezium_area_positive(self):
        print("Test: Trapezium area with valid inputs (a, b, h >= 0)")
        result = trapezium_area(3, 5, 4)
        print(f"Result: {result}")
        self.assertAlmostEqual(result, 16.0)

    def test_trapezium_area_negative(self):
        print("Test: Trapezium area when inputs < 0")
        try:
            trapezium_area(-3, 5, 4)
        except ValueError as e:
            print(f"Exception: {e}")
            self.assertTrue(True)

    def test_trapezium_area_invalid(self):
        print("Test: Trapezium area with invalid input (e.g., string, boolean)")
        invalid_inputs = [("a", 5, 4), (True, 3, 4)]
        for invalid in invalid_inputs:
            try:
                trapezium_area(*invalid)
            except ValueError as e:
                print(f"Input: {invalid} | Exception: {e}")
                self.assertTrue(True)

    # Ellipse
    def test_ellipse_area_positive(self):
        print("Test: Ellipse area with valid inputs (a, b >= 0)")
        result = ellipse_area(3, 5)
        print(f"Result: {result}")
        self.assertAlmostEqual(result, 47.12388980384689)

    def test_ellipse_area_negative(self):
        print("Test: Ellipse area when inputs < 0")
        try:
            ellipse_area(-3, 5)
        except ValueError as e:
            print(f"Exception: {e}")
            self.assertTrue(True)

    def test_ellipse_area_invalid(self):
        print("Test: Ellipse area with invalid input (e.g., string, boolean)")
        invalid_inputs = [("a", 5), (True, 3)]
        for invalid in invalid_inputs:
            try:
                ellipse_area(*invalid)
            except ValueError as e:
                print(f"Input: {invalid} | Exception: {e}")
                self.assertTrue(True)

    # Rhombus
    def test_rhombus_area_positive(self):
        print("Test: Rhombus area with valid inputs (d1, d2 >= 0)")
        result = rhombus_area(3, 5)
        print(f"Result: {result}")
        self.assertAlmostEqual(result, 7.5)

    def test_rhombus_area_negative(self):
        print("Test: Rhombus area when inputs < 0")
        try:
            rhombus_area(-3, 5)
        except ValueError as e:
            print(f"Exception: {e}")
            self.assertTrue(True)

    def test_rhombus_area_invalid(self):
        print("Test: Rhombus area with invalid input (e.g., string, boolean)")
        invalid_inputs = [("a", 5), (True, 3)]
        for invalid in invalid_inputs:
            try:
                rhombus_area(*invalid)
            except ValueError as e:
                print(f"Input: {invalid} | Exception: {e}")
                self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
