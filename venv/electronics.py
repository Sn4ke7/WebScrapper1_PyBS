import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://www.responseelectronics.com'

headers = {
    'User-Agent' :
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

r = requests.get('https://www.responseelectronics.com/shop/safety-and-security/cameras/era-protect-wifi-outdoor-1080p-security-camera/')


print(r)
soup = BeautifulSoup(r.content,'lxml')
price = soup.find_all('h2', class_='productDetailPrice priceClearance ng-binding')#.text.strip()
print(price)

productlist = soup.find_all('div', class_='col-xs-12')
#detail = []
#detail = soup.find(class_='productDetailPrice').text
#print(detail)
#print(productlist)
name = soup.find('h1', class_="h3").text
print(name)
price = soup.find('h2')
print(price)
prod_img = []
prod_img = soup.find_all('img', class_="img-responsive bordered")

print(prod_img)

# TODO: Getting images from site
# https://www.responseelectronics.com/globalassets/response/images/scaexwh1080_2.jpg
#scaexwh1080_2.jpg
'''
<img alt="ERA Protect WiFi Outdoor 1080p Security Camera" class="img-responsive" itemprop="image" ng-src="/globalassets/response/images/scaexwh1080_2.jpg" src="/globalassets/response/images/scaexwh1080_2.jpg">
'''

#print(productlist)
# productlinks = []