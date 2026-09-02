import sqlite3


def add_publisher(cursor, name):
    """Add a publisher without creating duplicates."""
    try:
        cursor.execute(
            "INSERT OR IGNORE INTO publishers (name) VALUES (?)",
            (name,)
        )
    except sqlite3.Error as error:
        print(f"Error adding publisher: {error}")


def get_publisher_id(cursor, name):
    """Return the database ID for a publisher."""
    cursor.execute(
        "SELECT id FROM publishers WHERE name = ?",
        (name,)
    )

    row = cursor.fetchone()

    return row[0] if row else None


def add_magazine(cursor, name, publisher_name):
    """Add a magazine using the actual publisher ID."""
    try:
        publisher_id = get_publisher_id(cursor, publisher_name)

        if publisher_id is None:
            print(f"Publisher not found: {publisher_name}")
            return

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
    """Add a subscriber without duplicating name/address pairs."""
    try:
        cursor.execute(
            """
            INSERT OR IGNORE INTO subscribers (name, address)
            VALUES (?, ?)
            """,
            (name, address)
        )

    except sqlite3.Error as error:
        print(f"Error adding subscriber: {error}")


def get_subscriber_id(cursor, name, address):
    """Return the database ID for a subscriber."""
    cursor.execute(
        """
        SELECT id
        FROM subscribers
        WHERE name = ? AND address = ?
        """,
        (name, address)
    )

    row = cursor.fetchone()

    return row[0] if row else None


def get_magazine_id(cursor, name):
    """Return the database ID for a magazine."""
    cursor.execute(
        "SELECT id FROM magazines WHERE name = ?",
        (name,)
    )

    row = cursor.fetchone()

    return row[0] if row else None


def add_subscription(
    cursor,
    subscriber_name,
    subscriber_address,
    magazine_name,
    expiration_date
):
    """Add a subscription using IDs looked up from the database."""

    try:
        subscriber_id = get_subscriber_id(
            cursor,
            subscriber_name,
            subscriber_address
        )

        magazine_id = get_magazine_id(
            cursor,
            magazine_name
        )

        if subscriber_id is None:
            print(f"Subscriber not found: {subscriber_name}")
            return

        if magazine_id is None:
            print(f"Magazine not found: {magazine_name}")
            return

        cursor.execute(
            """
            INSERT OR IGNORE INTO subscriptions
            (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
            """,
            (
                subscriber_id,
                magazine_id,
                expiration_date
            )
        )

    except sqlite3.Error as error:
        print(f"Error adding subscription: {error}")


try:
    # Connect to the magazines database.
    connection = sqlite3.connect("../db/magazines.db")

    # Turn on foreign key enforcement.
    connection.execute("PRAGMA foreign_keys = ON")

    cursor = connection.cursor()

    print("Database created and connected successfully.")


    # --------------------------------------------------
    # Task 2: Create the database tables
    # --------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """
    )


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,

            FOREIGN KEY (publisher_id)
            REFERENCES publishers(id)
        )
        """
    )


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,

            UNIQUE (name, address)
        )
        """
    )


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,

            FOREIGN KEY (subscriber_id)
            REFERENCES subscribers(id),

            FOREIGN KEY (magazine_id)
            REFERENCES magazines(id),

            UNIQUE (
                subscriber_id,
                magazine_id,
                expiration_date
            )
        )
        """
    )


    print("Tables created successfully.")


    # --------------------------------------------------
    # Task 3: Populate publishers
    # --------------------------------------------------

    add_publisher(
        cursor,
        "Time Publishing"
    )

    add_publisher(
        cursor,
        "National Media"
    )

    add_publisher(
        cursor,
        "Technology Press"
    )


    # --------------------------------------------------
    # Task 3: Populate magazines
    # --------------------------------------------------

    add_magazine(
        cursor,
        "World Today",
        "Time Publishing"
    )

    add_magazine(
        cursor,
        "Nature Weekly",
        "National Media"
    )

    add_magazine(
        cursor,
        "Tech Monthly",
        "Technology Press"
    )


    # --------------------------------------------------
    # Task 3: Populate subscribers
    # --------------------------------------------------

    add_subscriber(
        cursor,
        "Alice Smith",
        "100 Main Street"
    )

    add_subscriber(
        cursor,
        "Bob Jones",
        "200 Oak Avenue"
    )

    add_subscriber(
        cursor,
        "Charlie Brown",
        "300 Pine Road"
    )


    # --------------------------------------------------
    # Task 3: Populate subscriptions
    # --------------------------------------------------

    add_subscription(
        cursor,
        "Alice Smith",
        "100 Main Street",
        "World Today",
        "2027-01-01"
    )

    add_subscription(
        cursor,
        "Bob Jones",
        "200 Oak Avenue",
        "Nature Weekly",
        "2027-02-01"
    )

    add_subscription(
        cursor,
        "Charlie Brown",
        "300 Pine Road",
        "Tech Monthly",
        "2027-03-01"
    )


    # Save the inserted data.
    connection.commit()

    print("Data added successfully.")


    # --------------------------------------------------
    # Task 4 - Query 1
    # Retrieve all subscriber information
    # --------------------------------------------------

    print("\nAll subscribers:")

    cursor.execute(
        """
        SELECT *
        FROM subscribers
        """
    )

    for row in cursor.fetchall():
        print(row)


    # --------------------------------------------------
    # Task 4 - Query 2
    # Retrieve all magazines sorted by name
    # --------------------------------------------------

    print("\nMagazines sorted by name:")

    cursor.execute(
        """
        SELECT *
        FROM magazines
        ORDER BY name
        """
    )

    for row in cursor.fetchall():
        print(row)


    # --------------------------------------------------
    # Task 4 - Query 3
    # Find magazines for a particular publisher
    # --------------------------------------------------

    publisher_name = "Time Publishing"

    print(
        f"\nMagazines published by {publisher_name}:"
    )

    cursor.execute(
        """
        SELECT magazines.*
        FROM magazines

        JOIN publishers
        ON magazines.publisher_id = publishers.id

        WHERE publishers.name = ?
        """,
        (publisher_name,)
    )

    for row in cursor.fetchall():
        print(row)


except sqlite3.Error as error:
    print(f"Database error: {error}")


finally:
    if "connection" in locals():
        connection.close()

        print("Database connection closed.")