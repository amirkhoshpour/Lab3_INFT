'''
Name: Amir Khoshpour
Student ID: 100993995

'''
import unittest

def run_tests(choice):
    print("\nRunning tests...\n")
    test_map = {
        'c': [
            'test_Lab3_Amir.TestShapes.test_circle_area_positive',
            'test_Lab3_Amir.TestShapes.test_circle_area_negative',
            'test_Lab3_Amir.TestShapes.test_circle_area_invalid',
        ],
        't': [
            'test_Lab3_Amir.TestShapes.test_trapezium_area_positive',
            'test_Lab3_Amir.TestShapes.test_trapezium_area_negative',
            'test_Lab3_Amir.TestShapes.test_trapezium_area_invalid',
        ],
        'e': [
            'test_Lab3_Amir.TestShapes.test_ellipse_area_positive',
            'test_Lab3_Amir.TestShapes.test_ellipse_area_negative',
            'test_Lab3_Amir.TestShapes.test_ellipse_area_invalid',
        ],
        'r': [
            'test_Lab3_Amir.TestShapes.test_rhombus_area_positive',
            'test_Lab3_Amir.TestShapes.test_rhombus_area_negative',
            'test_Lab3_Amir.TestShapes.test_rhombus_area_invalid',
        ]
    }

    if choice in test_map:
        # Create a combined test suite for the selected shape
        suite = unittest.TestSuite()
        for test in test_map[choice]:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))

        # Run the combined test suite
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    elif choice == 'q':
        print("Exiting program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Please enter one of the following options:")
    print("  - 'c' for testing all cases for circle area")
    print("  - 't' for testing all cases for trapezium area")
    print("  - 'e' for testing all cases for ellipse area")
    print("  - 'r' for testing all cases for rhombus area")
    print("  - 'q' to quit")
    while True:
        choice = input("What would you like to do? ").strip().lower()
        if choice == 'q':
            break
        run_tests(choice)
