from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html').read()
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify)

table = soup.find('table',{'id':'giftList'})

rows = table.find_all('tr')

for row in rows:
    data = row.find_all('td')

    if (len(data) > 0):
        cell = data[0]
        print(cell.text)