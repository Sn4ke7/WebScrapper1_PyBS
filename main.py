import requests
from bs4 import BeautifulSoup

#URL of crawled page
#baseurl = 'https://www.responseelectronics.com'
baseurl = 'https://www.thewhiskyexchange.com'

headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

# r = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky')



productlinks = []
for x in range(1,2):
    r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}#productlist-filter')
    soup = BeautifulSoup(r.content, 'lxml')

    productlist = soup.find_all('div', class_='item')

    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])
            # print(link['href'])

print(len(productlinks))
print(productlinks)
# print(productlist)

# TODO: Find loop that would function as checker of page count (while with try except finally?)

# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'


#if __name__ == '__main__':
#    pass
