from bs4 import BeautifulSoup
import requests

url = requests.get('https://dzone.com/articles/best-programming-jokes-amp-quotes').text
# print(url)
soup = BeautifulSoup(url,'lxml')
# print(soup)

web_name = soup.title.string
# print(webpage_name)

ordered_list =  soup.find('ol')
# print(ordered_list)
quotes_list = ordered_list.find_all('li')
quotes = []
for ql in quotes_list:
    quotes.append(ql.text)

for q in quotes:
    print(q)
    print()

# with open("Quotes.txt", "w") as wf:
#     for q in quotes:
#         wf.write(q.strip())
#         wf.write("\n")




