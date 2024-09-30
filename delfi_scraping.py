from bs4 import BeautifulSoup
import requests
import csv

r = requests.get("https://www.delfi.lt/")
soup = BeautifulSoup(r.text, "html.parser")
blocks = soup.find_all("article")

with open("delfi_naujienos.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Category", "Title", "Link"])

    for block in blocks:
        # print(block.prettify())
        try:
            category = block.find(class_="headline-labels__label").get_text().strip()
            title = block.find(class_="headline-title").get_text().strip()
            link = block.find(class_="headline-title").a['href']
            if link.startswith("/"):
                link = "https://www.delfi.lt/" + link
            print(category)
            print(title)
            print(link)
            print()
            csv_writer.writerow([category, title, link])
        except:
            pass