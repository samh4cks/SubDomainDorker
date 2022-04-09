from urllib.error import HTTPError, URLError
import urllib.request
from urllib.request import Request, urlopen
from banner import banner, banner1
from termcolor import colored
from googlesearch import search
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin
import time

print(colored(banner1,"blue"))

print (colored(banner,"yellow"))  ## Banner Printing

url = input("Enter the URL: ")  ## Taking URL as input
final_url = "{url}"

domain_parse = urlparse(url).netloc               
domain = ('.'.join(domain_parse.split('.')[-2:]) or '.'.join(domain_parse.split('.')[-3:]) or '.'.join(domain_parse.split('.')[-4:]))   ## Parsing domain from URL
print (domain)

 ## Getting URL Status Code
try:
        status_code = urllib.request.urlopen(url).getcode()
        if status_code == 200:
                print("\nURL is active\n")
        elif status_code != 200:
                print("\nURL is down\n")
except urllib.error.HTTPError as e:
        print("HTTPError")
        exit (0)
except urllib.error.URLError as e:
        print("URLError")
        exit (0)
################################ Web-Scraping from Google Dorks ##############################

# try:
#         from googlesearch import search
#         from urllib.error import HTTPError, URLError
#         import urllib.request
#         from urllib.request import Request, urlopen
#         from banner import banner, banner1
#         from termcolor import colored
#         from bs4 import BeautifulSoup
#         import requests
#         from urllib.parse import urlparse, urljoin
# except ImportError:
#         print("No module named 'google' found")

# to search
query = "site:"+domain
print (query,"\n")

soup = BeautifulSoup(requests.get("https://www.google.com/search?q="+query).content, "html.parser")
s = "https://www.google.com/search?q="+query

res = []
for a_tag in soup.find_all("a"):
 
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
       #     # href empty tag
          continue
        parsed_href = urlparse(href)
        # print(parsed_href)
        href = parsed_href.query
        #print(href)
        host = href.partition("://")[2]
        sub_domain = host.partition(".")[0]
        #print("tiger zinda hai 3")
        # print(sub_domain)
        final_sub_domain = '{}.{}'.format(sub_domain, domain)
        #print(final_sub_domain)
        sub_domain_append = res.append(final_sub_domain)
#print(res)

sub_domain_dic = str(res)
sub_dom = []
for i in res:
        if i not in sub_dom:
                sub_dom.append(i)

print(str(sub_dom))


