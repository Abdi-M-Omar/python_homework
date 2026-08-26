# Task 6: Scraping Structured Data

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# --------------------------------------------------
# Step 2: Open the OWASP Top 10 page with Selenium
# --------------------------------------------------

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://owasp.org/Top10/2025/0x00_2025-Introduction/"
driver.get(url)


# --------------------------------------------------
# Step 3: Find the OWASP Top 10 vulnerabilities
# --------------------------------------------------

links = driver.find_elements(
    By.XPATH,
    "//a[contains(text(), ':2025 - ')]"
)

results = []

for link in links:

    title = link.text
    href = link.get_attribute("href")

    vulnerability = {
        "Title": title,
        "Link": href
    }

    results.append(vulnerability)


# The page can contain repeated links to the same
# vulnerabilities, so keep only unique titles.
unique_results = []

seen_titles = set()

for item in results:

    if item["Title"] not in seen_titles:

        unique_results.append(item)
        seen_titles.add(item["Title"])


# Keep the first 10 vulnerabilities
results = unique_results[:10]


# Print the results
print(results)

print("Number found:", len(results))


# --------------------------------------------------
# Step 4: Write the results to a CSV file
# --------------------------------------------------

df = pd.DataFrame(results)

print(df)

df.to_csv(
    "assignment8/owasp_top_10.csv",
    index=False
)


# Close the browser
driver.quit()