# -*- coding: utf-8 -*-
"""
Web crawling with Python - BeautifulSoup
Created on Sat Oct  6 02:51:38 2018

@author: Seji OH
"""

# Set a working directory.
import os

os.chdir("F:/github_codes/web_crawling/")
os.listdir()

# Import the library.
from bs4 import BeautifulSoup
import urllib.request

# Address the URL to read.
url = "https://www.bbc.co.uk/search?q=mars+travel"

# Open the page.
html_doc = urllib.request.urlopen(url)

# Read the webpage.
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

# Let's extract links only since the website shows the search result.
soup.find_all('a')

websites_list = []

for link in soup.find_all('a'):
    # print(link.get('href'))
    links = link.get('href')
    websites_list.append(links)
    
print(websites_list)
websites_list

# Now we can collect webpages.
# At first, extract links what we want to get data.
len(websites_list)
websites_list[35]
websites_list[66]

websites_list = websites_list[36:66]
websites_list

# Let's inspect the first webpage in the list.
url = websites_list[0]
html_doc = urllib.request.urlopen(url)

soup = BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify().encode('utf-8')

# We want to save the content in a file.
# Since the content is written in the form of bytes,
# we need to encode a data from binary to string.
import base64

result_b64 = base64.b64encode(result)

result_decode_b64 = base64.b64decode(result_b64)

with open("bbc_mars_travel.html", "xb") as outfile:
    outfile.write(result_decode_b64)
outfile.close()

# Then we can save each content with 'for' loop.
for i in range(len(websites_list)):
    with open("bbc_mars_travel_%s.html"%(i), "xb") as outfile:

        url = websites_list[i]
        html_doc = urllib.request.urlopen(url)
   
        soup = BeautifulSoup(html_doc, 'html.parser')
        result = soup.prettify().encode('utf-8')
        result_b64 = base64.b64encode(result)
        result_decode_b64 = base64.b64decode(result_b64)

        outfile.write(result_decode_b64)
    outfile.close()
    
# Read multiple webpages.
urls = []
websites_list = []
for i in range(2,11):
    i = str(i)
    url = "https://www.bbc.co.uk/search?q=mars+travel#page="+i
    # print(url)    
    urls.append(url)
    # print(urls)
    for url in urls:
        html_doc = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        for link in soup.find_all('a'):
            links = link.get('href')
            websites_list.append(links)

websites_list
    
        
    