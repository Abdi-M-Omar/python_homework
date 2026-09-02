import sqlite3


def add_publisher(cursor, name):
    try:
        cursor.execute(
            "INSERT OR IGNORE INTO publishers (name) VALUES (?)",
            (name,)
        )
    except sqlite3.Error as error:
        print(f"Error adding publisher: {error}")


def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute(
            """
            INSERT OR IGNORE INTO magazines (name, publisher_id)
            VALUES (?, ?)
            """,
            (name, publisher_id)
        )
    except sqlite3.Error as error:
        print(f"Error adding magazine: {error}")


def add_subscriber(cursor, name, address):
    try:
        cursor.execute(
            """
            SELECT id
            FROM subscribers
            WHERE name = ? AND address = ?
            """,
            (name, address)
        )

        existing_subscriber = cursor.fetchone()

        if existing_subscriber is None:
            cursor.execute(
                """
                INSERT INTO subscribers (name, address)
                VALUES (?, ?)
                """,
                (name, address)
            )

    except sqlite3.Error as error:
        print(f"Error adding subscriber: {error}")


def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute(
            """
            SELECT id
            FROM subscriptions
            WHERE subscriber_id = ?
              AND magazine_id = ?
              AND expiration_date = ?
            """,
            (subscriber_id, magazine_id, expiration_date)
        )

        existing_subscription = cursor.fetchone()

        if existing_subscription is None:
            cursor.execute(
                """
                INSERT INTO subscriptions
                (subscriber_id, magazine_id, expiration_date)
                VALUES (?, ?, ?)
                """,
                (subscriber_id, magazine_id, expiration_date)
            )

    except sqlite3.Error as error:
        print(f"Error adding subscription: {error}")


try:
    # Task 1: Connect to the database.
    connection = sqlite3.connect("../db/magazines.db")

    # Task 3: Turn on foreign-key enforcement.
    connection.execute("PRAGMA foreign_keys = ON")

    cursor = connection.cursor()

    print("Database created and connected successfully.")

    # Task 2: Create the publishers table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
    """)

    # Task 2: Create the magazines table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id)
        )
    """)

    # Task 2: Create the subscribers table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    # Task 2: Create the subscriptions table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        )
    """)

    print("Tables created successfully.")

    # Task 3: Populate publishers.
    add_publisher(cursor, "Time Publishing")
    add_publisher(cursor, "National Media")
    add_publisher(cursor, "Technology Press")

    # Task 3: Populate magazines.
    add_magazine(cursor, "World Today", 1)
    add_magazine(cursor, "Nature Weekly", 2)
    add_magazine(cursor, "Tech Monthly", 3)

    # Task 3: Populate subscribers.
    add_subscriber(cursor, "Alice Smith", "100 Main Street")
    add_subscriber(cursor, "Bob Jones", "200 Oak Avenue")
    add_subscriber(cursor, "Charlie Brown", "300 Pine Road")

    # Task 3: Populate subscriptions.
    add_subscription(cursor, 1, 1, "2027-01-01")
    add_subscription(cursor, 2, 2, "2027-02-01")
    add_subscription(cursor, 3, 3, "2027-03-01")

    # Save all database changes.
    connection.commit()

    print("Data added successfully.")

    # Task 4: Write SQL Queries

    # Query 1:
    # Retrieve all information from the subscribers table.
    print("\nAll subscribers:")

    cursor.execute("""
        SELECT *
        FROM subscribers
    """)

    subscribers = cursor.fetchall()

    for subscriber in subscribers:
        print(subscriber)


    # Query 2:
    # Retrieve all magazines sorted alphabetically by name.
    print("\nMagazines sorted by name:")

    cursor.execute("""
        SELECT *
        FROM magazines
        ORDER BY name
    """)

    magazines = cursor.fetchall()

    for magazine in magazines:
        print(magazine)


    # Query 3:
    # Find all magazines published by a particular publisher.
    # This query uses a JOIN between magazines and publishers.
    print("\nMagazines published by Time Publishing:")

    cursor.execute("""
        SELECT magazines.*
        FROM magazines
        JOIN publishers
            ON magazines.publisher_id = publishers.id
        WHERE publishers.name = ?
    """, ("Time Publishing",))

    publisher_magazines = cursor.fetchall()

    for magazine in publisher_magazines:
        print(magazine)

except sqlite3.Error as error:
    print(f"Database error: {error}")

finally:
    if "connection" in locals():
        connection.close()
        print("Database connection closed.")