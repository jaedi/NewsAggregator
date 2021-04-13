from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

site = "https://www.inquirer.net/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

for a in soup.select('#tr_boxs3'):
    data = {
        'title': a.find('h2').text,
        'source': a.find('a')['href'],
        'date': a.find('span').text
    }

    print(data)

"""
def getImage(url):
    req = Request(url, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    for a in soup.select('#article_content'):
        return a.find('img')['src']

"""