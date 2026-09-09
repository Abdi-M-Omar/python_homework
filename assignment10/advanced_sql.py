import sqlite3


# Open the database
connection = sqlite3.connect("../db/lesson.db")
connection.execute("PRAGMA foreign_keys = 1")
cursor = connection.cursor()


# Task 1: Find the total price of the first 5 orders
sql = """
SELECT orders.order_id,
       SUM(products.price * line_items.quantity) AS total_price
FROM orders
JOIN line_items
    ON orders.order_id = line_items.order_id
JOIN products
    ON line_items.product_id = products.product_id
GROUP BY orders.order_id
ORDER BY orders.order_id
LIMIT 5;
"""


# Execute the SQL statement
cursor.execute(sql)


# Get all returned rows
results = cursor.fetchall()


# Print the order ID and total price
for order_id, total_price in results:
    print(order_id, f"{total_price:.2f}")

# Task 2: Find the average order total for each customer
sql = """
SELECT customers.customer_name,
       AVG(order_totals.total_price) AS average_total_price
FROM customers
LEFT JOIN (
    SELECT orders.customer_id AS customer_id_b,
           orders.order_id,
           SUM(products.price * line_items.quantity) AS total_price
    FROM orders
    JOIN line_items
        ON orders.order_id = line_items.order_id
    JOIN products
        ON line_items.product_id = products.product_id
    GROUP BY orders.order_id, orders.customer_id
) AS order_totals
    ON customers.customer_id = order_totals.customer_id_b
GROUP BY customers.customer_id;
"""

cursor.execute(sql)

results = cursor.fetchall()

print("\nTask 2:")

for customer_name, average_total_price in results:
    if average_total_price is None:
        print(customer_name, None)
    else:
        print(customer_name, f"{average_total_price:.2f}")


# Task 3: Create an order for Perez and Sons
# with Miranda Harris as the employee.
# The customer wants 10 of each of the 5 least expensive products.

# Find the customer ID
cursor.execute("""
SELECT customer_id
FROM customers
WHERE customer_name = 'Perez and Sons';
""")

customer_id = cursor.fetchone()[0]


# Find the employee ID
cursor.execute("""
SELECT employee_id
FROM employees
WHERE first_name = 'Miranda'
  AND last_name = 'Harris';
""")

employee_id = cursor.fetchone()[0]


# Find the 5 least expensive products
cursor.execute("""
SELECT product_id
FROM products
ORDER BY price
LIMIT 5;
""")

product_ids = cursor.fetchall()


# Create the order and line items in one transaction
with connection:

    cursor.execute("""
    INSERT INTO orders (customer_id, employee_id, date)
    VALUES (?, ?, DATE('now'))
    RETURNING order_id;
    """, (customer_id, employee_id))

    order_id = cursor.fetchone()[0]


    for product_id_tuple in product_ids:
        product_id = product_id_tuple[0]

        cursor.execute("""
        INSERT INTO line_items (order_id, product_id, quantity)
        VALUES (?, ?, ?);
        """, (order_id, product_id, 10))


# Print the line items for the new order
cursor.execute("""
SELECT line_items.line_item_id,
       line_items.quantity,
       products.product_name
FROM line_items
JOIN products
    ON line_items.product_id = products.product_id
WHERE line_items.order_id = ?;
""", (order_id,))

results = cursor.fetchall()

print("\nTask 3:")

for line_item_id, quantity, product_name in results:
    print(line_item_id, quantity, product_name)

# Task 4: Find employees associated with more than 5 orders
sql = """
SELECT employees.employee_id,
       employees.first_name,
       employees.last_name,
       COUNT(orders.order_id) AS order_count
FROM employees
JOIN orders
    ON employees.employee_id = orders.employee_id
GROUP BY employees.employee_id,
         employees.first_name,
         employees.last_name
HAVING COUNT(orders.order_id) > 5;
"""

cursor.execute(sql)

results = cursor.fetchall()

print("\nTask 4:")

for employee_id, first_name, last_name, order_count in results:
    print(employee_id, first_name, last_name, order_count)
# Close the database
connection.close()