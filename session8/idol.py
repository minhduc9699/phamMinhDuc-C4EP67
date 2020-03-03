import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient('localhost:27017')
db = client['c4e']
kpop_collection = db['Kpop']




k_pop_page = requests.get('https://dbkpop.com/db/all-k-pop-idols').text

soup = BeautifulSoup(k_pop_page, 'html.parser')

table = soup.find('tbody')
tr_content = table.find_all('tr')

for tr in tr_content:
  td_content = tr.find_all('td')
  info_value = []
  for td in td_content:
    info_value.append(td.string)
  idol_dict = {
    'stage_name': info_value[1],
    'full_name': info_value[2],
    'k_name': info_value[3]
  }
  kpop_collection.insert_one(idol_dict)