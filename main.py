from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# web = requests.get("https://www.iplt20.com/points-table/men")

options = webdriver.ChromeOptions()
options.add_argument("--heading")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.iplt20.com/points-table/men")
html = driver.page_source
driver.quit()


soup = BeautifulSoup(html, "html.parser")


with open ("page.html","w", encoding="utf-8")as f:
    f.write(soup.prettify())

driver.quit()
    

