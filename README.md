<h5># WebCrawling</h5>
<h2><b> A Keyword Specification Web Crawling with R and Python</b></h2>
<pre>
How to gather the data from the web?
If you look for 'web crawling' on any search engines,
you will get the information about various tools.

But I found an unpleasant matter while I was doing a research for the web crawling.
I could not specify for a keyword search with scrapy nor python package 'beautifulsoup'.

So here is the curious question arose.
Is there no way to specify a certain word when we extract data from the web?
Here let's explore the domain to find the answer.

References:
[1] Rcrawler: https://github.com/salimk/Rcrawler#how-to-cite-rcrawler
Khalil, S., & Fakir, M. (2017).
RCrawler: An R package for parallel web crawling and scraping. SoftwareX, 6, 98-106.
[2] Scrapy: https://scrapy.org/
[3] beautifulsoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

As I mentioned above, there are various tools for web crawling.
Here we are going to deal data with three tools:
<a href="#scrapy">1. Scrapy with python</a>
<a href="#beautifulsoup">2. Python package -  beautifulsoup</a>
<a href="#rcrawler">3. R library - Rcrawler</a>

And whatever you use, it is not avoidable to install <b>JAVA</b>.
There are plenty of information about the installation which you can find easily on the internet.
So I will not handle the object here.

Now let's choose the keyword to collect the information about.
I select this one: <b>Mars travel</b>
(There is no special reason to pick the topic but only the curiosity.)

Then we need to choose a website where we get the information.
As you guess there are tons of information on the web so we need to pick a certain website.
Then I decide to scrap webpages from the British news company <b>BBC (https://www.bbc.com)</b>.
(You can choose any topics and any websites whatever you want.)

The website offers an in-site search:
https://www.bbc.co.uk/search?q=mars+travel
We will start from here.

<b><u>CODE</b></u>
<b><h4 id="scrapy">1. Scrapy with python</h4></b>
<pre><code></code></pre>
<pre><code></code></pre>
<pre><code></code></pre>

<b><h4 id="beautifulsoup">2. Python package -  BeautifulSoup</h4></b>
This package BeautifulSoup is a useful when we read web pages.<br>
Let's import libraries to use.
<pre><code>
from bs4 import BeautifulSoup
import urllib.request
</code></pre>
Then we address the web page as 'url', open it, and read it.
<pre><code>
url = "https://www.bbc.co.uk/search?q=mars+travel"
html_doc = urllib.request.urlopen(url)
soup.BeautifulSoup(html_doc, 'html.parser')
</code></pre>
We can print the content on IPython console.
<pre><code>
print(soup.prettify())
</code></pre>
This output shows the search results briefly, however we need full contents for each article.<br>
So let's extract links only from the output then tidy it.
<pre><code>
soup.find_all('a')
websites_list = []
for link in soup.find_all('a'):    
    links = link.get('href')
    websites_list.append(links)
websites_list
len(websites_list)
websites_list = websites_list[36:66]
websites_list
</code></pre>
Let's inspect the first webpage in the list and save it into the file.<br>
Since the content is written in the form of bytes, we need to encode a data from binary to string.
<pre><code>
url = websites_list[0]
html_doc = urllib.request.urlopen(url)
soup = BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify().encode('utf-8')

import base64
result_b64 = base64.b64encode(result)
result_decode_b64 = base64.b64decode(result_b64)
with open("bbc_mars_travel.html", "xb") as outfile:
    outfile.write(result_decode_b64)
outfile.close()
</code></pre>
Then we can save each content with 'for' loop.
<pre><code>
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
</code></pre>
The contents have been saved into bbc_mars_travel.html and bbc_mars_travel_[i].html<br>
(You can find the files in bbc_mars_travel.zip.)<br>
Now we need to clean the data precisely from each file for the analysis.<br>
This step will be conducted after we collect the data with R.<br>

Mostly, multiple pages are needed to collect.<br>
In that case:
<pre><code>
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
</pre></code>


<b><h4 id="rcrawler">3. R library - Rcrawler</h4></b>
There is a simple way to download webpages directly with R.
<pre><code>
download.file("https://www.bbc.co.uk/search?q=mars+travel", "bbc_search_result.html")
</code></pre>
To download more pages, we need write a for loop.
<pre><code>
for (i in 2:10) {
i <- as.character(i)
target <- paste("https://www.bbc.co.uk/search?q=mars+travel#page=", i, sep="")
destination = paste("bbc_search_result", i, ".html", sep="")
download.file(target,destination)}
</code></pre>
But do not forget the purpose of this research.
The plan is collecting web pages about the Mars travel.
So I present the package Rcrawler.[1]
Let's install and upload it.
<pre><code>
install.packagest("Rcrawler")
library(Rcrawler)
</code></pre>
Now we can filter and scrap web pages by the keywords 'mars' and 'travel' with this.
Let's collect only webpages that has an accuracy percentage higher than 50% of matching 'mars' and 'travel'.
<pre><code>
Rcrawler(Website="https://www.bbc.com",
KeywordsFilter = c("mars", "travel"),
KeywordsAccuracy = 50,
no_cores=4, no_conn=4)
</code></pre>
Or try this one to see the connection of webpages.
<pre><code>
Rcrawler(Website="https://www.bbc.com",
KeywordsFilter = c("mars", "travel"),
KeywordsAccuracy = 50,
NetworkData = TRUE, NetwExtLinks =TRUE,
statslinks = TRUE,
no_cores=4, no_conn=4)
</code></pre>

Next step to data analysis will be continued.

<b>Citation Request</b><br>
If you use anything obtained from this repository, then, in your acknowledgements,
please note the assistance you received by using this repository.
Thank you.
</pre>

