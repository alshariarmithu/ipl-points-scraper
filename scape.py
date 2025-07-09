from bs4 import BeautifulSoup
import pandas as pd

with open("page.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

table = soup.find("table", class_="ih-td-tab")
thead = table.find_all("th") 
tbody = table.find("tbody", id="pointsdata") 

headers = []
for th in thead:
    headers.append(th.get_text(strip=True))

all_rows = []
for tr in tbody.find_all("tr"):
    row = []
    for td in tr.find_all("td"):
        data = td.get_text(strip=True)
        row.append(data)
    all_rows.append(row)

print(f"Headers: {len(headers)}")
print(f"Number of rows: {len(all_rows)}")
    
# Ensure all rows have the same number of columns as headers
for row in all_rows:
    if len(row) < len(headers):
        row.extend([''] * (len(headers) - len(row)))

df = pd.DataFrame(all_rows, columns=headers)
df.to_csv("file.csv", index=False, encoding="utf-8") 
print("Data saved to file.csv")