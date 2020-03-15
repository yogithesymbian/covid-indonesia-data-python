import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)
print(response)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

#We use the method .findAll to locate all of our <a> tags.
data = soup.findAll('a')[35]
print(data)
link = data['href']
print(link)
print(data[''])


# download_url = 'http://web.mta.info/developers/'+ link
# urllib.request.urlretrieve(download_url,'./’'link[link.find('/turnstile_')+1:])

# time.sleep(1)

# =======================
# To download the whole data set, let's do a for loop through all a tags
# line_count = 1 #variable to track what line you are on
# for data in soup.findAll('a'):  #'a' tags are for links
#     if line_count >= 36: #code for text files starts at line 36
#         link = data['href']
#         download_url = 'http://web.mta.info/developers/'+ link
#         urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
#         time.sleep(1)
#         print(link)
#         print(download_url)
#     line_count += 1