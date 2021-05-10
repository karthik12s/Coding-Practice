import requests
from bs4 import BeautifulSoup
import wikipedia
hyd  = wikipedia.page("Hyderabad")
response = requests.get(
	url=hyd.url,
)
response = response.text
soup = BeautifulSoup(response, 'html.parser')

title = soup.find_all('table')
l1 = str(title[0]).split('srcset="')
s = str(l1[0])
for i in range(1,len(l1)):
  s = s + 'srcset="https:'+l1[i]
import io
with io.open('test.html', "w", encoding="utf-8") as f:
    f.write(s)
