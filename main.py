from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

os.makedirs("data", exist_ok=True)

driver = webdriver.Chrome()
query = "laptop"
file = 0

for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}")
    time.sleep(2)

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"Page {i}: {len(elems)} items found")

    for elem in elems:
        html = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(html)
        file += 1

driver.quit()
