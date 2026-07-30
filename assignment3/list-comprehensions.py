import csv

# Read employees.csv into a list of lists
employees = []

with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        employees.append(row)

# Print the original data
print(employees)

# Task 3.2
# Create a list of full names (first_name + last_name)
employee_names = [
    employee[1] + " " + employee[2]
    for employee in employees[1:]
]

print(employee_names)

# Task 3.3
# Keep only names containing the letter "e"
names_with_e = [
    name
    for name in employee_names
    if "e" in name
]

print(names_with_e)