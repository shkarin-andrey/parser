from bs4 import BeautifulSoup
import requests


def save():
    with open('parse_info.txt', 'a') as file:
        file.write(f'{comp["title"]} -> Price: {comp["price"]}\n')


def parse():
    URL = 'https://www.toy.ru/catalog/producers/L.O.L./'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36', 'accept': '*/*'
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='product-card')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('a', class_='d-block p-1 product-name gtm-click').get_text(strip=True),
            'price': item.find('span', class_='price').get_text(strip=True),
        })

        global comp
        for comp in comps:
            print(f'{comp["title"]} -> Price: {comp["price"]}')
            save()


parse()
