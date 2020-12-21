import requests
from bs4 import BeautifulSoup
import pandas as pd

#URL of crawled page
#baseurl = 'https://www.responseelectronics.com'
baseurl = 'https://www.thewhiskyexchange.com'

#required for being able to pull out page response (some pages block request if it's not acting as user)
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
# binding request from page to variable
# r = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky')

productlinks = []

for x in range(1,3):
    r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}#productlist-filter')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='item')
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])
           #print(link['href'])

#testlink = 'https://www.thewhiskyexchange.com/p/37325/suntory-torys-classic'
whiskylist = []
for link in productlinks:

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('h1', class_='product-main__name').text.strip()
    try:
        price = soup.find('p', class_='product-action__price').text.strip()
    except:
        price = 'no price'
   # reviews = soup.find('span', class_='review-overview__count').text.strip()
    try:
        rating = soup.find('div', class_='review-overview__rating star-rating star-rating--30').text.strip()
    except:
        rating = 'no rating'
    whisky = {
        'name':name,
        'rating':rating,
        #'reviews': reviews,
        'price': price

        }
    #print(whisky)
    whiskylist.append(whisky)
    print("Saving: ", whisky['name'])

df = pd.DataFrame(whiskylist)
print(df.head(-1))
#print(name,rating,reviews,price)
''' DONE: error to handle https://tinyurl.com/y3dm3h86 (32/64 bit problem)
 Solution : pip install numpy==1.19.3 '''

# TODO: Find loop that would function as checker of page count (while with try except finally?)
# TODO: Check if simplest form works with other sites
# TODO: Experiment more with request and types of returned values


# name = soup.find('h1', class_='product-main__name').text.strip()
# rating = soup.find('span', class_="review-overview__rating star-rating start-rating--30").text
# price = soup.find('p', class_='product-action__price').text.strip()
# print(name,rating,price)
# print(len(productlinks))
# print(productlinks)
# print(productlist)

#if __name__ == '__main__':
#    pass
