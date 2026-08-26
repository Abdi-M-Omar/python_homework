# Task 6: Scraping Structured Data

from pathlib import Path

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Store the path of the assignment8 folder
BASE_DIR = Path(__file__).resolve().parent


# Task 6 - Step 2:
# Use Selenium to load the OWASP Top Ten page named in the instructions

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://owasp.org/www-project-top-ten/"
driver.get(url)


# Task 6 - Step 3:
# Find the current OWASP Top Ten page from the project page

top_ten_link = driver.find_element(
    By.XPATH,
    "//a[contains(@href, '/Top10/2025')]"
)

top_ten_url = top_ten_link.get_attribute("href")

driver.get(top_ten_url)


# Find the 10 vulnerability links using XPath

links = driver.find_elements(
    By.XPATH,
    "//a["
    "starts-with(normalize-space(.), 'A01:2025') or "
    "starts-with(normalize-space(.), 'A02:2025') or "
    "starts-with(normalize-space(.), 'A03:2025') or "
    "starts-with(normalize-space(.), 'A04:2025') or "
    "starts-with(normalize-space(.), 'A05:2025') or "
    "starts-with(normalize-space(.), 'A06:2025') or "
    "starts-with(normalize-space(.), 'A07:2025') or "
    "starts-with(normalize-space(.), 'A08:2025') or "
    "starts-with(normalize-space(.), 'A09:2025') or "
    "starts-with(normalize-space(.), 'A10:2025')"
    "]"
)


# Store each vulnerability title and link in a dictionary

results = []
seen_titles = set()

for link in links:

    title = link.text.strip()
    href = link.get_attribute("href")

    if title and title not in seen_titles:

        vulnerability = {
            "Title": title,
            "Link": href
        }

        results.append(vulnerability)
        seen_titles.add(title)


# Keep only the first 10 unique vulnerabilities

results = results[:10]


# Print the list to verify the scraped data

print(results)

print("Number found:", len(results))


# Task 6 - Step 4:
# Convert the list to a DataFrame and save it to owasp_top_10.csv

df = pd.DataFrame(results)

print(df)

df.to_csv(
    BASE_DIR / "owasp_top_10.csv",
    index=False
)


# Close the browser

driver.quit()