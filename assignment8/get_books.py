# Task 3 - Step 1: Import required libraries

import json
from pathlib import Path

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# Store the location of the assignment8 folder
BASE_DIR = Path(__file__).resolve().parent


# Task 3 - Step 2: Load the web page

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver.get(url)


# Task 3 - Step 3: Find all book search-result li elements

books = driver.find_elements(
    By.XPATH,
    "//li[contains(@class, 'cp-search-result-item')]"
)

print("Number of books found:", len(books))


# Task 3 - Step 4: Create an empty results list

results = []


# Task 3 - Step 5: Extract information from each book

for book in books:

    # Task 3 - Step 5a: Find the title
    title_element = book.find_element(
        By.XPATH,
        ".//span[contains(@class, 'title-content')]"
    )

    title = title_element.text


    # Task 3 - Step 5b: Find the author or authors
    author_elements = book.find_elements(
        By.XPATH,
        ".//a[contains(@class, 'author-link')]"
    )

    authors = []

    for author in author_elements:
        authors.append(author.text)

    author_text = "; ".join(authors)


    # Task 3 - Step 5c: Find the format and year
    format_div = book.find_element(
        By.XPATH,
        ".//div[contains(@class, 'cp-format-info')]"
    )

    format_span = format_div.find_element(
        By.TAG_NAME,
        "span"
    )

    format_year = format_span.text


    # Task 3 - Step 5d: Create a dictionary for the book
    book_data = {
        "Title": title,
        "Author": author_text,
        "Format-Year": format_year
    }


    # Task 3 - Step 5e: Add the dictionary to the results list
    results.append(book_data)


# Task 3 - Step 6: Create and print a DataFrame

df = pd.DataFrame(results)

print(df)


# Task 4 - Step 1: Write the DataFrame to get_books.csv

df.to_csv(
    BASE_DIR / "get_books.csv",
    index=False
)


# Task 4 - Step 2: Write the results list to get_books.json

with open(
    BASE_DIR / "get_books.json",
    "w",
    encoding="utf-8"
) as json_file:

    json.dump(
        results,
        json_file,
        indent=4,
        ensure_ascii=False
    )


# Close the browser

driver.quit()