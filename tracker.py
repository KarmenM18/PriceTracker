# GOAL: to track price volatility on any given day, so that you can buy your product when the price drops.

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://www.alibaba.com/product-detail/Graphics-Card-DELL-NVIDIA-RTX-3090_1600922927454.html?spm=a2700.galleryofferlist.normal_offer.d_price.61b97976PKJbEt"
#webpage = requests.get(URL, headers=HEADERS)

def get_data(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup






