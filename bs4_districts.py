import requests
from bs4 import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/List_of_districts_of_Thailand'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

districts = []

for row in soup.findAll('tr'):
    if row.get('class') == ['sortbottom']:
        break
    cols = row.findAll('td')
    if cols:
        district_name = cols[1].text.strip()
        districts.append(district_name)

print(districts)
