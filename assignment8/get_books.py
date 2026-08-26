# Task 3 - Step 1: Import required libraries

import json
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Task 3 - Step 2: Load the Durham Library search page

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(url)

# Task 3 - Step 3: Find all book search-result elements

book_entries = driver.find_elements(
    By.CSS_SELECTOR,
    "li.row.cp-search-result-item"
)

print("Number of books found:", len(book_entries))

# Task 3 - Step 4: Create an empty list to store book data

results = []

# Task 3 - Step 5: Extract book information

for book in book_entries:
    title = book.find_element(By.CLASS_NAME, "title-content").text

    author_elements = book.find_elements(By.CLASS_NAME, "author-link")
    authors = "; ".join(author.text for author in author_elements)

    format_container = book.find_element(By.CLASS_NAME, "cp-format-info")
    format_year = format_container.find_element(
        By.CLASS_NAME,
        "display-info-primary"
    ).text

    book_data = {
        "Title": title,
        "Author": authors,
        "Format-Year": format_year
    }

    results.append(book_data)

    # Task 3 - Step 6: Create and print a DataFrame

df = pd.DataFrame(results)
print(df)

# Task 4 - Step 1: Write the DataFrame to a CSV file

df.to_csv("assignment8/get_books.csv", index=False)


# Task 4 - Step 2: Write the results list to a JSON file

with open("assignment8/get_books.json", "w") as json_file:
    json.dump(results, json_file, indent=4)

driver.quit()

#