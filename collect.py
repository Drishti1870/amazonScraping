from bs4 import BeautifulSoup
import os
import pandas as pd
from urllib.parse import unquote, urlparse, parse_qs

rows = []

for file in os.listdir("data"):
    with open(f"data/{file}", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # title
    title_tag = soup.select_one("h2.a-size-base-plus span")
    if not title_tag:
        continue
    title = title_tag.get_text(strip=True)

    # link (handle sponsored redirect)
    a_tag = soup.select_one("a.a-link-normal[href]")
    if not a_tag:
        continue

    href = a_tag["href"]
    if "sspa/click" in href:
        parsed = parse_qs(urlparse(href).query)
        href = parsed.get("url", [href])[0]
        href = unquote(href)

    link = "https://www.amazon.in" + href

    # price
    price_tag = soup.select_one("span.a-price-whole")
    price = price_tag.get_text(strip=True) if price_tag else None

    rows.append({
        "title": title,
        "price": price,
        "link": link
    })

print("Products extracted:", len(rows))
pd.DataFrame(rows).to_csv("data.csv", index=False)
