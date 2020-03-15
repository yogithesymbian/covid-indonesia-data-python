import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://polnes.ac.id/'

# Connect to the URL
response = requests.get(url)
print(response.status_code)
# print(response.content)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify)
# data1 = soup.findAll('a')
data = soup.findAll('a', class_='moduleItemTitle')
# print(data)
for data in soup.findAll('a', class_='moduleItemTitle'):
    show_data = data.get_text()
    print("\n",show_data, "\n")
    print("debug")
