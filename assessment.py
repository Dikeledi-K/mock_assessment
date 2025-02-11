'''Instructions:
You have 90 minutes to complete this assessment.
You must git add, git commit, and git push your work regularly.
Read the requirements carefully.
Each function should handle edge cases and follow best practices.
Use print statements to test before submitting.'''

#Problem 1: Student Score Analysis (35 Marks)
'''Write a function analyze_scores(students) that takes a list of student dictionaries and returns a dictionary containing:

"average": The average score of all students.
"highest_scorer": The name of the student with the highest score.
"passed_students": A list of students who scored above or equal to 50.'''

'''input Format:
students = [
    {"name": "Alice", "age": 20, "score": 85},
    {"name": "Bob", "age": 22, "score": 40},
    {"name": "Charlie", "age": 21, "score": 92},
    {"name": "Derek", "age": 23, "score": 67}
]

🔹 Expected Output:
{
    "average": 71.0,
    "highest_scorer": "Charlie",
    "passed_students": ["Alice", "Charlie", "Derek"]
}'''


#Problem 2: Product Stock Tracker (30 Marks)
'''Write a function update_stock(inventory, sold_items) that:

Takes a dictionary inventory where keys are product names and values are stock counts.
Takes a list sold_items where each item represents a product that was sold.
Updates the inventory by reducing stock for each sold item.
If a product is out of stock, it should remain at 0 and not go negative.
If a sold item is not in the inventory, ignore it.

🔹 Input Format:
inventory = {"apple": 10, "banana": 5, "orange": 8}
sold_items = ["apple", "banana", "apple", "grape", "orange", "banana"]

🔹 Expected Output:
{"apple": 8, "banana": 3, "orange": 7}'''


#Problem 3: Employee Salary Bonus (25 Marks)
'''Write a function calculate_bonus(employees, min_salary, bonus_percentage) that:

Takes a dictionary employees where keys are employee names and values are their salaries.
Takes a minimum salary min_salary, where employees earning below this value get a bonus.
Takes bonus_percentage which is added to those who qualify.
Returns a dictionary with updated salaries.

🔹 Input Format:
employees = {"Alice": 4000, "Bob": 2500, "Charlie": 3000, "Derek": 4500}
min_salary = 3000
bonus_percentage = 10  # 10% increase

🔹 Expected Output:
{"Alice": 4000, "Bob": 2750, "Charlie": 3300, "Derek": 4500}'''