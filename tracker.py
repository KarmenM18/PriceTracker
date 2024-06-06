# GOAL: to track price volatility on any given day, so that you can buy your product when the price drops.

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=graphics+card&_sacat=0"


# html = request.urlopen(URL).read()
# soup = BeautifulSoup(html, features="html.parser")

def get_data(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    product_list = []
    # parse out each item on the page
    #results = soup.find_all('div', {'class': 's-item__info clearfix'}) - void due to CAPTCHA block
    results = soup.find('div', {'class': 'srp-river-results clearfix'}).find_all('li', {
        'class': 's-item s-item__pl-on-bottom'})

    for item in results:
        # extract key info from each item
        product = {
            'title': item.find('div', {'class': 's-item__title'}).text,
            #'soldprice': float(item.find('span', {'class': 's-item__price'}).text.replace('C $', '').replace(',', '').strip()),
            #'bids': item.find('span', {'class': 's-item__bids s-item__bidCount'}).text,
            'link': item.find('a', {'class': 's-item__link'})['href'],
        }
        #print(product)
        product_list.append(product)
    print(len(results))
    return product_list


def output(product_list):
    prod_df = pd.DataFrame(product_list)
    prod_df.to_csv('output.csv', index=False)
    print('Saved to CSV')
    return

soup = get_data(URL)
product_list = parse(soup)
output(product_list)
