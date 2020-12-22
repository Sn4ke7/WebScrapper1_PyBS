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

productlinks = []