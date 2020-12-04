import requests
from bs4 import BeautifulSoup

#URL of crawled page
#baseurl = 'https://www.responseelectronics.com'
baseurl = 'https://www.thewhiskyexchange.com'

headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

r = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky')


soup = BeautifulSoup(r.content, 'lxml')

productlist = soup.find_all('div', class_='item')

productlinks = []

for item in productlist:
    for link in item.find_all('a', href=True):
        productlinks.append(baseurl + link['href'])
        # print(link['href'])
print(len(productlinks))
# print(productlist)


# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'


#if __name__ == '__main__':
#    pass
