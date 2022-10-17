import requests
from bs4 import BeautifulSoup
# import csv
from tabulate import tabulate

URL = "https://www.tokyu-sports.com/golf/himonya.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="pbBlock17580224")

wait_times = results.find_all("span", class_="floor_info")
last_update = results.find("span", class_="order-date")

rows = []
for idx in range(3):
    row = [str(idx+1) + "階", wait_times[idx].text]
    rows.append(row)
    # print(row)

# with open('result.csv', 'w') as f:
#     write = csv.writer(f)

#     write.writerow(fields)
#     write.writerows(rows)

print("<<-- " + last_update.text + " -->>")
print(tabulate(rows, headers=["階数", "待ち時間"], stralign="center"))