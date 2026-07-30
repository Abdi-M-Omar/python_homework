import pandas as pd

# ===========================
# Task 1.1 - Create DataFrame
# ===========================

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)

print(task1_data_frame)

# ===========================
# Task 1.2 - Add Salary Column
# ===========================

task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]

print(task1_with_salary)

# ===========================
# Task 1.3 - Modify Age Column
# ===========================

task1_older = task1_with_salary.copy()

task1_older["Age"] = task1_older["Age"] + 1

print(task1_older)

# ===========================
# Task 1.4 - Save CSV
# ===========================

task1_older.to_csv("employees.csv", index=False)

# ===========================
# Task 2.1 - Read CSV
# ===========================

task2_employees = pd.read_csv("employees.csv")

print(task2_employees)

# ===========================
# Task 2.2 - Read JSON
# ===========================

json_employees = pd.read_json("additional_employees.json")

print(json_employees)

# ===========================
# Task 2.3 - Combine DataFrames
# ===========================

more_employees = pd.concat(
    [task2_employees, json_employees],
    ignore_index=True
)

print(more_employees)

# ===========================
# Task 3.1 - First 3 rows
# ===========================

first_three = more_employees.head(3)

print(first_three)


# ===========================
# Task 3.2 - Last 2 rows
# ===========================

last_two = more_employees.tail(2)

print(last_two)


# ===========================
# Task 3.3 - Shape
# ===========================

employee_shape = more_employees.shape

print(employee_shape)


# ===========================
# Task 3.4 - DataFrame Info
# ===========================

more_employees.info()

# ===========================
# Task 4: Data Cleaning
# ===========================

# Read the dirty CSV file into a DataFrame.
dirty_data = pd.read_csv("dirty_data.csv")

# Display the original dirty data.
print(dirty_data)

# Create a copy so the original DataFrame remains unchanged.
clean_data = dirty_data.copy()


# ===========================
# Task 4.2 - Remove Duplicates
# ===========================

# Remove any duplicate rows from the copied DataFrame.
clean_data = clean_data.drop_duplicates()

print(clean_data)


# ===========================
# Task 4.3 - Convert Age
# ===========================

# Convert Age values to numbers.
# Invalid values become NaN because of errors="coerce".
clean_data["Age"] = pd.to_numeric(
    clean_data["Age"],
    errors="coerce"
)

print(clean_data)


# ===========================
# Task 4.4 - Convert Salary
# ===========================

# Replace known placeholder values with missing values.
clean_data["Salary"] = clean_data["Salary"].replace(
    ["unknown", "n/a"],
    pd.NA
)

# Convert Salary values to numbers.
# Any remaining invalid values become NaN.
clean_data["Salary"] = pd.to_numeric(
    clean_data["Salary"],
    errors="coerce"
)

print(clean_data)


# ===========================
# Task 4.5 - Fill Missing Values
# ===========================

# Fill missing Age values with the mean age.
clean_data["Age"] = clean_data["Age"].fillna(
    clean_data["Age"].mean()
)

# Fill missing Salary values with the median salary.
clean_data["Salary"] = clean_data["Salary"].fillna(
    clean_data["Salary"].median()
)

print(clean_data)


# ===========================
# ===========================
# Task 4.6 - Convert Hire Date
# ===========================

# Convert the Hire Date column to datetime.
clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"],
    errors="coerce"
)

# Fill any missing dates with a valid date.
clean_data["Hire Date"] = clean_data["Hire Date"].fillna(
    pd.Timestamp("2000-01-01")
)

print(clean_data)


# ===========================
# Task 4.7 - Clean Text Columns
# ===========================

# Remove extra spaces from Name and convert it to uppercase.
clean_data["Name"] = (
    clean_data["Name"]
    .str.strip()
    .str.upper()
)

# Remove extra spaces from Department and convert it to uppercase.
clean_data["Department"] = (
    clean_data["Department"]
    .str.strip()
    .str.upper()
)

print(clean_data)