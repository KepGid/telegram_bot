# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def parser_(url):
    url = 'https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&country.impo' \
          'rt.usa.not=-1&price.currency=1&abroad.not=0&custom.not=1&page=0&size=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chr'
                      'ome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.421',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20210324.02.00'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    content = soup.find_all('div', class_='content')

    for i in content:
        name = i.find('a', class_='address').text
        try:
            price = i.find('span', class_='size15').text
        except:
            price = i.find('div', class_='start-price-wrapper mb-5').text

        # image_url = i.find('img', class_='outline m-auto')
        # image = requests.get(url).content
        city = i.find('li', class_='item-char view-location js-location').text
        date = i.find('div', class_='footer_ticket').text
        # name = i.find('span', class_='blue bold')
        print(name, ' - ', price, city, date)



