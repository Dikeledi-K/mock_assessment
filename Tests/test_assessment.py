import unittest
from assessment import analyze_scores, update_stock, calculate_bonus  # Import your functions here

class TestAssessment(unittest.TestCase):

    # Test cases for analyze_scores function
    def test_analyze_scores(self):
        students = [
            {"name": "Alice", "age": 20, "score": 85},
            {"name": "Bob", "age": 22, "score": 40},
            {"name": "Charlie", "age": 21, "score": 92},
            {"name": "Derek", "age": 23, "score": 67}
        ]
        self.assertEqual(analyze_scores(students), {
            "average": 71.0,
            "highest_scorer": "Charlie",
            "passed_students": ["Alice", "Charlie", "Derek"]
        })

        # Edge case: Empty list
        self.assertEqual(analyze_scores([]), {
            "average": 0,
            "highest_scorer": None,
            "passed_students": []
        })

        # Edge case: Only one student
        self.assertEqual(analyze_scores([{"name": "Eve", "age": 21, "score": 50}]), {
            "average": 50.0,
            "highest_scorer": "Eve",
            "passed_students": ["Eve"]
        })

    # Test cases for update_stock function
    def test_update_stock(self):
        inventory = {"apple": 10, "banana": 5, "orange": 8}
        sold_items = ["apple", "banana", "apple", "grape", "orange", "banana"]
        self.assertEqual(update_stock(inventory, sold_items), {
            "apple": 8, "banana": 3, "orange": 7
        })

        # Edge case: Empty inventory
        self.assertEqual(update_stock({}, ["apple"]), {})

        # Edge case: Out of stock scenario
        self.assertEqual(update_stock({"water": 1}, ["water", "water"]), {"water": 0})

        # Edge case: Selling more than available stock
        self.assertEqual(update_stock({"bread": 3, "milk": 2}, ["milk", "bread", "bread", "bread"]), {
            "bread": 0, "milk": 1
        })

    # Test cases for calculate_bonus function
    def test_calculate_bonus(self):
        employees = {"Alice": 4000, "Bob": 2500, "Charlie": 3000, "Derek": 4500}
        self.assertEqual(calculate_bonus(employees, 3000, 10), {
            "Alice": 4000, "Bob": 2750, "Charlie": 3300, "Derek": 4500
        })

        # Edge case: Empty employee dictionary
        self.assertEqual(calculate_bonus({}, 3000, 10), {})

        # Edge case: Single employee gets bonus
        self.assertEqual(calculate_bonus({"Tom": 2000}, 3000, 20), {"Tom": 2400})

        # Edge case: Some employees get bonus, others don’t
        self.assertEqual(calculate_bonus({"Eve": 3500, "Sam": 2500}, 3000, 15), {
            "Eve": 3500, "Sam": 2875
        })

if __name__ == "__main__":
    unittest.main()
