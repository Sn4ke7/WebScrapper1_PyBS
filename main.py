import requests
from bs4 import BeautifulSoup

#URL of crawled page
#baseurl = 'https://www.responseelectronics.com'
baseurl = 'https://www.thewhiskyexchange.com'

headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

# r = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky')


productlinks = []
for x in range(1,3):
    r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}#productlist-filter')
    soup = BeautifulSoup(r.content, 'lxml')

    productlist = soup.find_all('div', class_='item')

    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])
            # print(link['href'])

testlink = "https://www.thewhiskyexchange.com/p/37325/suntory-torys-classic"
r = requests.get(testlink, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
print(soup.find('h1'), class_="product-main__name").text

# name = soup.find('h1', class_='product-main__name').text.strip()
# rating = soup.find('span', class_="review-overview__rating star-rating start-rating--30").text
# price = soup.find('p', class_='product-action__price').text.strip()
# print(name,rating,price)
# print(len(productlinks))
# print(productlinks)
# print(productlist)

# TODO: Find loop that would function as checker of page count (while with try except finally?)
# TODO: Check if simplest form works with other sites
# TODO: Experiment more with request and types of returned values

# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'


#if __name__ == '__main__':
#    pass
