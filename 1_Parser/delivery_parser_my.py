import requests
from bs4 import BeautifulSoup


def get_books():
    count_page = 50

    catalog = []
    for i in range(1, count_page + 1):
        url = 'https://books.toscrape.com/catalogue/page-'f'{i}''.html'

        # создаём данные, имитирующие простого человека
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"}

        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.find_all('article', class_="product_pod")
            print(f'Найдено книг: {len(products)}')

            for book in products:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                catalog.append({'title': title, 'price': price})

        except requests.exceptions.RequestException as e:
            print(f'Ошибка сети: {e}')
            return []

    return catalog


if __name__ == '__main__':
    print(get_books())
