import unittest
import os
import tempfile
from task1 import highest_salary_per_department

class TestHighestSalary(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for tests
        self.tmpdir = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmpdir.name, "employees.csv")
        content = (
            "Name,Department,Salary\n"
            "Alice,Engineering,70000\n"
            "Bob,Engineering,80000\n"
            "Carol,HR,65000\n"
            "Dan,HR,65000\n"
            "Eve,Sales,\"$90,000\"\n"
        )
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            f.write(content)

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_highest_salary_basic(self):
        res = highest_salary_per_department(self.path)
        expected = {
            "Engineering": ("Bob", 80000.0),
            "HR": ("Carol", 65000.0),
            "Sales": ("Eve", 90000.0),
        }
        self.assertEqual(res, expected)

    def test_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            highest_salary_per_department(os.path.join(self.tmpdir.name, "missing.csv"))

    def test_invalid_columns(self):
        p = os.path.join(self.tmpdir.name, "bad.csv")
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write("Name,Department\nAlice,Engineering\n")
        with self.assertRaises(ValueError):
            highest_salary_per_department(p)

    def test_empty_file(self):
        empty_path = os.path.join(self.tmpdir.name, "empty.csv")
        with open(empty_path, "w", encoding="utf-8", newline="") as f:
            f.write("")
        result = highest_salary_per_department(empty_path)
        self.assertEqual(result, {})

    def test_incomplete_rows(self):
        incomplete_path = os.path.join(self.tmpdir.name, "incomplete.csv")
        with open(incomplete_path, "w", encoding="utf-8", newline="") as f:
            f.write("Name,Department,Salary\n")
            f.write("Alice,Engineering,\n")
            f.write(",HR,65000\n")
            f.write("Eve,Sales,\"$90,000\"\n")
        result = highest_salary_per_department(incomplete_path)
        expected = {
            "Sales": ("Eve", 90000.0),
        }
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()