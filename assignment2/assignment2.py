# Task 2: Read a CSV File

import csv
import traceback
import os
import custom_module
from datetime import datetime



def read_employees():
    employees = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r", encoding="utf-8") as employee_file:
            csv_reader = csv.reader(employee_file)

            for index, row in enumerate(csv_reader):
                if index == 0:
                    employees["fields"] = row
                else:
                    rows.append(row)

            employees["rows"] = rows
            return employees

    except Exception as e:
        print("An exception occurred.")
        print(f"Exception type: {type(e).__name__}")

        message = str(e)
        if message:
            print(f"Exception message: {message}")

        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File: {trace[0]}, Line: {trace[1]}, "
                f"Func.Name: {trace[2]}, Message: {trace[3]}"
            )

        print(f"Stack trace: {stack_trace}")
        return {}


employees = read_employees()
print(employees)

# --------------------------------------------------
# Task 3: Find the Column Index
# --------------------------------------------------

def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")

# --------------------------------------------------
# Task 4: Find the Employee First Name
# --------------------------------------------------
def first_name(row_number):
    first_name_column = column_index("first_name")
    row = employees["rows"][row_number]
    return row[first_name_column]

# --------------------------------------------------
# Task 5: Find the Employee
# --------------------------------------------------

# Search for an employee by their employee ID.
def employee_find(employee_id):

    # Check whether the current row matches the employee ID.
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    # Filter the employee rows to find matching employee IDs.
    matches = list(filter(employee_match, employees["rows"]))

    # Return the matching employee row(s).
    return matches

# --------------------------------------------------
# Task 6: Find the Employee with a Lambda
# --------------------------------------------------

# Search for an employee by their employee ID using a lambda function.
def employee_find_2(employee_id):

    # Filter the employee rows using a lambda expression.
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id,
                          employees["rows"]))

    # Return the matching employee row(s).
    return matches

# --------------------------------------------------
# Task 7: Sort the Rows by Last Name Using a Lambda
# --------------------------------------------------

# Sort the employee rows by last name.
def sort_by_last_name():

    # Find the column index for the last name.
    last_name_column = column_index("last_name")

    # Sort the employee rows in place using a lambda.
    employees["rows"].sort(key=lambda row: row[last_name_column])

    # Return the sorted rows.
    return employees["rows"]


# Sort the employee data by last name.
sort_by_last_name()

# Display the sorted employee dictionary.
print(employees)

# --------------------------------------------------
# Task 8: Create a Dictionary for an Employee
# --------------------------------------------------

# Create a dictionary from an employee row.
def employee_dict(row):

    # Create an empty dictionary.
    employee = {}

    # Loop through each column.
    for i in range(len(employees["fields"])):

        # Skip the employee_id column.
        if employees["fields"][i] == "employee_id":
            continue

        # Store the field name and its value.
        employee[employees["fields"][i]] = row[i]

    # Return the completed employee dictionary.
    return employee


# Create and display an employee dictionary.
print(employee_dict(employees["rows"][0]))

# --------------------------------------------------
# Task 9: Create a Dictionary of All Employees
# --------------------------------------------------

# Create a dictionary containing all employees.
def all_employees_dict():

    # Create an empty dictionary.
    all_employees = {}

    # Loop through each employee row.
    for row in employees["rows"]:

        # Get the employee ID from the row.
        employee_id = row[employee_id_column]

        # Store the employee dictionary using the employee ID as the key.
        all_employees[employee_id] = employee_dict(row)

    # Return the completed dictionary.
    return all_employees


# Create and display the dictionary of all employees.
print(all_employees_dict())

# --------------------------------------------------
# Task 10: Use the os Module
# --------------------------------------------------

# Return the value of the THISVALUE environment variable.
def get_this_value():

    # Read and return the environment variable.
    return os.getenv("THISVALUE")

# --------------------------------------------------
# Task 11: Creating Your Own Module
# --------------------------------------------------

# Set the secret value in the custom module.
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


# Change and display the secret.
set_that_secret("Python Rules!")
print(custom_module.secret)

# --------------------------------------------------
# Task 12: Read minutes1.csv and minutes2.csv
# --------------------------------------------------

# Read one minutes CSV file and return its fields and rows.
def read_minutes_file(file_path):
    minutes = {
        "fields": [],
        "rows": []
    }

    with open(file_path, "r", encoding="utf-8") as minutes_file:
        csv_reader = csv.reader(minutes_file)

        for index, row in enumerate(csv_reader):
            if index == 0:
                minutes["fields"] = row
            else:
                minutes["rows"].append(tuple(row))

    return minutes


# Read both minutes CSV files.
def read_minutes():
    minutes1 = read_minutes_file("../csv/minutes1.csv")
    minutes2 = read_minutes_file("../csv/minutes2.csv")

    return minutes1, minutes2


# Store both returned dictionaries in global variables.
minutes1, minutes2 = read_minutes()

# Display both dictionaries.
print(minutes1)
print(minutes2)

# --------------------------------------------------
# Task 13: Create minutes_set
# --------------------------------------------------

# Combine the rows from both minutes files into one set.
def create_minutes_set():
    # Convert each list of rows into a set.
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])

    # Combine both sets into one.
    return minutes1_set.union(minutes2_set)


# Store the combined set in a global variable.
minutes_set = create_minutes_set()

# Display the combined set.
print(minutes_set)

# --------------------------------------------------
# Task 14: Convert to datetime
# --------------------------------------------------

# Convert the minutes set into a list with datetime objects.
def create_minutes_list():
    # Convert the set into a list.
    minutes = list(minutes_set)

    # Convert each date string into a datetime object.
    minutes = list(
        map(
            lambda x: (
                x[0],
                datetime.strptime(x[1], "%B %d, %Y")
            ),
            minutes
        )
    )

    return minutes


# Store the converted list in a global variable.
minutes_list = create_minutes_list()

# Display the converted list.
print(minutes_list)

# --------------------------------------------------
# Task 15: Write Out Sorted List
# --------------------------------------------------

# Sort the minutes list and write it to a CSV file.
def write_sorted_list():
    # Create a sorted copy using the datetime value.
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])

    # Convert each datetime object back into a string.
    converted_list = list(
        map(
            lambda x: (
                x[0],
                datetime.strftime(x[1], "%B %d, %Y")
            ),
            sorted_minutes
        )
    )

    # Write the sorted data to minutes.csv.
    with open("./minutes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list


# Call the function without replacing the original minutes_list.
sorted_minutes_list = write_sorted_list()

# Display the sorted list.
print(sorted_minutes_list)