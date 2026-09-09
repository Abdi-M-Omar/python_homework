import sqlite3
from pathlib import Path

import pandas as pd


# Get the assignment9 directory.
BASE_DIR = Path(__file__).resolve().parent

# Task 5 requires ../db/lesson.db
DATABASE_PATH = BASE_DIR.parent / "db" / "lesson.db"

# Save the CSV directly inside assignment9.
OUTPUT_PATH = BASE_DIR / "order_summary.csv"


try:
    # Connect to lesson.db.
    connection = sqlite3.connect(DATABASE_PATH)


    # --------------------------------------------------
    # Task 5 - Step 2
    # Read data from line_items and products
    # into a Pandas DataFrame.
    # --------------------------------------------------

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


    df = pd.read_sql_query(
        query,
        connection
    )


    # --------------------------------------------------
    # Task 5 - Step 3
    # Print the first 5 rows.
    # --------------------------------------------------

    print("Original DataFrame:")

    print(
        df.head()
    )


    # --------------------------------------------------
    # Task 5 - Step 4
    # Create the total column.
    # total = quantity * price
    # --------------------------------------------------

    df["total"] = (
        df["quantity"] * df["price"]
    )


    print("\nDataFrame with total:")

    print(
        df.head()
    )


    # --------------------------------------------------
    # Task 5 - Step 5
    # Group by product_id.
    #
    # line_item_id -> count
    # total -> sum
    # product_name -> first
    # --------------------------------------------------

    summary_df = (
        df.groupby("product_id")
        .agg(
            {
                "line_item_id": "count",
                "total": "sum",
                "product_name": "first"
            }
        )
    )


    print("\nGrouped DataFrame:")

    print(
        summary_df.head()
    )


    # --------------------------------------------------
    # Task 5 - Step 6
    # Sort by product_name.
    # --------------------------------------------------

    summary_df = summary_df.sort_values(
        by="product_name"
    )


    print("\nSorted DataFrame:")

    print(
        summary_df.head()
    )


    # --------------------------------------------------
    # Task 5 - Step 7
    # Write the DataFrame to order_summary.csv
    # inside assignment9.
    # --------------------------------------------------

    summary_df.to_csv(
        OUTPUT_PATH,
        index=False
    )


    print(
        f"\norder_summary.csv created successfully at: "
        f"{OUTPUT_PATH}"
    )


except (sqlite3.Error, pd.errors.DatabaseError) as error:
    print(
        f"Database error: {error}"
    )


finally:
    if "connection" in locals():
        connection.close()