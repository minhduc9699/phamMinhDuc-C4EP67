import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient('localhost:27017')
db = client['c4e']
kpop_collection = db['Kpop']

kpop_content = requests.get('https://dbkpop.com/db/all-k-pop-idols')
soup = BeautifulSoup(kpop_content.text, 'html.parser') #xml. xhtml, ...

# html_file = open("kpop.html","w")
# html_file.write(soup.prettify())
# html_file.close()
table_content = soup.find('tbody')
tr_content = table_content.find_all('tr')
idol_list = []
for tr in tr_content:
  idol_info = []
  td_content = tr.find_all('td')
  for td in td_content:
    idol_info.append(td.string)
  idol_list.append(idol_info) 
print(idol_list)


# for idol in idol_list:


  



# li_content = ul_content.find_all('li') #list
# for li in li_content:
#   news_link = li.h4.a['href']
#   news_title = str(li.h4.a.string).strip()
#   new_dict = {
#     'title': news_title,
#     'link': news_link
#   }
#   dantri_collection.insert_one(new_dict)