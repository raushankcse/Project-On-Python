import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com'
r = requests.get(url)



soup = BeautifulSoup(r.content,'lxml')
title=soup.find_all('h1',{'class':'title'})
print(title)