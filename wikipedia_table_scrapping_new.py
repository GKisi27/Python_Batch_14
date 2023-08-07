import requests
from bs4 import BeautifulSoup
import csv


url = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population").text

soup = BeautifulSoup(url,'lxml')
# print(soup.prettify())

webpage_name = soup.title.string
# print(webpage_name)

#get right table to scrap
right_table = soup.find('table',{'class':'wikitable sortable'})
# print(right_table)

headers = ["Country", "Population", "% in world", "Last update date"]

table_rows = right_table.find_all('tr')
# print(table_rows)

table_datas = []
for tr in table_rows[3:]:
    inner_dict = {}
    table_data = tr.find_all('td')
    for i,td in enumerate(table_data):
        if i in [4,5,6]:
            continue
        else:
            if i == 0:
                inner_dict[headers[0]] = td.text
            elif i == 1:
                inner_dict[headers[1]] = td.text
            elif i == 2:
                d = td.text
                inner_dict[headers[2]] = d.strip()
            else:
                d = td.text
                inner_dict[headers[3]] = d.strip()
    table_datas.append(inner_dict)

# for data in table_datas:
#     print(data)
#     print()

with open('Countries.csv','w') as wf:
    w = csv.DictWriter(wf,headers)
    w.writeheader()
    for data in table_datas:
        w.writerow(data)


