# ....existing code....
r"""
task1.py
Read an employees CSV file and find the employee with the highest salary in each department.

CSV expected columns: Name, Department, Salary

Usage:
 - To process a file named "employees.csv" located in the same folder:
     python "c:\Users\supri\OneDrive\Desktop\AIAC\LAB FINAL TEST\task1.py"
 - To run unit tests:
     python "c:\Users\supri\OneDrive\Desktop\AIAC\LAB FINAL TEST\task1.py" test
"""
from typing import Dict, Tuple
import csv
import os
import sys
import tempfile
import unittest

def _parse_salary(value: str) -> float:
    """Parse salary string to float. Handles commas and optional currency symbol."""
    if value is None:
        raise ValueError("Salary value is None")
    cleaned = value.replace(",", "").replace("$", "").strip()
    return float(cleaned)

def highest_salary_per_department(csv_path: str) -> Dict[str, Tuple[str, float]]:
    """
    Read csv_path and return a mapping: department -> (employee_name, salary)
    The function keeps the employee with the highest numeric salary for each department.
    """ 
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    best: Dict[str, Tuple[str, float]] = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # Ensure required columns are present
        required = {"Name", "Department", "Salary"}
        if not required.issubset(set(reader.fieldnames or [])):
            raise ValueError(f"CSV must contain columns: {', '.join(required)}")

        for row in reader:
            name = (row.get("Name") or "").strip()
            dept = (row.get("Department") or "").strip()
            salary_raw = row.get("Salary")
            if not dept or not name or salary_raw is None:
                # skip incomplete rows
                continue
            try:
                salary = _parse_salary(salary_raw)
            except Exception:
                # skip rows with invalid salary
                continue

            current = best.get(dept)
            if current is None or salary > current[1]:
                best[dept] = (name, salary)

    return best

def print_highest_salaries(results: Dict[str, Tuple[str, float]]) -> None:
    """Print results to stdout in a readable form."""
    if not results:
        print("No data to display.")
        return
    for dept in sorted(results):
        name, salary = results[dept]
        print(f"Department: {dept} - Employee: {name} - Salary: {salary:.2f}")

# Simple CLI behavior
def _main_cli():
    # Default file path: employees.csv in same directory as this script
    default_path = os.path.join(os.path.dirname(__file__) or ".", "employees.csv")
    csv_path = default_path
    # Allow user to supply alternate path as first argument
    if len(sys.argv) >= 2 and sys.argv[1].lower() != "test":
        csv_path = sys.argv[1]
    results = highest_salary_per_department(csv_path)
    print_highest_salaries(results)

# Unit tests
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
            "Eve,Sales,$90,000\n"  # intentionally has comma and $ to test parsing
        )
        # Fix the Eve salary cell so csv is valid (escape comma in salary)
        # We'll create a valid CSV row with quoted salary
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            f.write("Name,Department,Salary\n")
            f.write("Alice,Engineering,70000\n")
            f.write("Bob,Engineering,80000\n")
            f.write("Carol,HR,65000\n")
            f.write("Dan,HR,65000\n")
            f.write('Eve,Sales,"$90,000"\n')

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_highest_salary_basic(self):
        res = highest_salary_per_department(self.path)
        expected = {
            "Engineering": ("Bob", 80000.0),
            "HR": ("Carol", 65000.0),  # Carol and Dan tie; first encountered (Carol) kept
            "Sales": ("Eve", 90000.0),
        }
        self.assertEqual(res, expected)

    def test_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            highest_salary_per_department(os.path.join(self.tmpdir.name, "missing.csv"))

    def test_invalid_columns(self):
        # create a csv missing Salary column
        p = os.path.join(self.tmpdir.name, "bad.csv")
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write("Name,Department\nAlice,Engineering\n")
        with self.assertRaises(ValueError):
            highest_salary_per_department(p)

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1].lower() == "test":
        # run unit tests
        unittest.main(argv=[sys.argv[0]])
    else:
        try:
            _main_cli()
        except FileNotFoundError as e:
            print(e)