import requests
from bs4 import BeautifulSoup
import csv

def clean_data(data):
    cleaned_list = []
    for d in data:
        i = d.strip()
        if i==";" or i.startswith("[") or i=="":
            continue
        else:
            if i.endswith(","):
                cleaned_list.append(i[:-1])
            else:
                cleaned_list.append(i)
    s = ", ".join(cleaned_list)
    if s.endswith(","):
        final_string = s[:-1]
    else:
        final_string = s

    return f"{final_string}\t"     


url = requests.get('https://simple.wikipedia.org/wiki/List_of_countries').text

soup = BeautifulSoup(url,'lxml')
# print(soup.prettify())

# title of Wikipedia page
webpage_name = soup.title.string

# get right table to scrap
right_table=soup.find('table', {"class":'sortable wikitable'})

# number of rows in the table including header
rows = right_table.findAll("tr")
# print(len(rows))

# header attributes of the table
header = [th.text.rstrip() for th in rows[0].find_all('th')]
# print(header)
# print('------------')
# print(len(header))

output_file = open("List_of_countries.csv",'w', encoding="utf-8")
output_writer = csv.writer(output_file)
output_writer.writerow(header)


lst_data = []
for row in rows[1:]:
    data = [d.text.rstrip() for d in row.find_all('td')]
    lst_data.append(data)

# sample records
# print(lst_data[0:3])
cols = len(lst_data[0])
# print(cols)

# #Scrap the data and append to respective lists
for row in right_table.findAll("tr"):
    data_to_write = []
    cells = row.findAll('td')
    if len(cells)==4: #Only extract table body not heading
        c1_data = cells[0].findAll (text=True)
        c1_cleaned = clean_data(c1_data)
        data_to_write.append(c1_cleaned)

        c2_data = cells[1].findAll (text=True)
        c2_cleaned = clean_data(c2_data)
        data_to_write.append(c2_cleaned)

        c3_data = cells[2].findAll (text=True)
        c3_cleaned = clean_data(c3_data)
        data_to_write.append(c3_cleaned)

        c4_data = cells[3].findAll (text=True)
        c4_cleaned = clean_data(c4_data)
        data_to_write.append(c4_cleaned)

       
    output_writer.writerow(data_to_write)

output_file.close()


# with open('mycsvfile.csv', 'w') as f:
#     w = csv.DictWriter(f, headers)
#     w.writeheader()
#     for data in table_datas:
#         w.writerow(data)
