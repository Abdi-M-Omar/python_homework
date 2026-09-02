import sqlite3
import pandas as pd


connection = sqlite3.connect("../db/Lesson.db")

query = """
    SELECT
        line_items.line_item_id,
        line_items.quantity,
        products.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products
        ON line_items.product_id = products.product_id
"""

df = pd.read_sql_query(query, connection)

print(df.head())

# Task 5 - Step 4:
# Add a total column by multiplying quantity by price.
df["total"] = df["quantity"] * df["price"]

print("\nDataFrame with total:")
print(df.head())

# Task 5 - Step 5:
# Group the data by product_id and summarize each product.
summary_df = df.groupby("product_id").agg({
    "line_item_id": "count",
    "total": "sum",
    "product_name": "first"
})

print("\nGrouped DataFrame:")
print(summary_df.head())

# Task 5 - Step 6:
# Sort the summary DataFrame by product_name.
summary_df = summary_df.sort_values(by="product_name")

print("\nSorted DataFrame:")
print(summary_df.head())

# Task 5 - Step 7:
# Write the sorted summary DataFrame to a CSV file.
summary_df.to_csv("order_summary.csv", index=False)

print("\norder_summary.csv created successfully.")

connection.close()