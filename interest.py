import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.siddharthabank.com/interest-rates').text

soup = BeautifulSoup(url,'lxml')


# get right table to scrap
interest_table=soup.find_all('div', {"class":'col-lg-6 mb-3'})
first_table_body = interest_table[1].find('tbody')
upper_table_row = first_table_body.find('tr').text
print(upper_table_row)