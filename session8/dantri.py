import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient('localhost:27017')
db = client['c4e']
dantri_collection = db['dantri']

dantri_content = requests.get('https://dantri.com.vn/')

soup = BeautifulSoup(dantri_content.text, 'html.parser') #xml. xhtml, ...

div_content = soup.find('div', {'class': 'xnano'})

ul_content = div_content.find('ul', {'class': 'ul1 ulnew'})

li_content = ul_content.find_all('li') #list
for li in li_content:
  news_link = li.h4.a['href']
  news_title = str(li.h4.a.string).strip()
  new_dict = {
    'title': news_title,
    'link': news_link
  }
  dantri_collection.insert_one(new_dict)