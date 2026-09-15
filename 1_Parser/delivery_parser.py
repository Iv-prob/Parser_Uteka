import requests
from bs4 import BeautifulSoup

# Прямой адрес каталога книг (обходя развилку)
url = "https://books.toscrape.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("--- НАЧИНАЕМ СКАЧИВАНИЕ КАТАЛОГА КНИГ ---")

try:
    # Загружаем страницу с таймаутом безопасности
    response = requests.get(url, headers=headers, timeout=5)
    response.encoding = "utf-8"
    print(f"Статус ответа сервера: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")

    # Находим все контейнеры книг на странице
    products = soup.find_all("article", class_="product_pod")
    print(f"Найдено книг на странице: {len(products)}")

    print("\n--- СПИСОК КНИГ И ЦЕН ---")
    for product in products:
        # Выуживаем полный заголовок книги из атрибута 'title' ссылки
        title = product.h3.a["title"]
        # Выуживаем цену и очищаем её от лишних символов валюты
        price = product.find("p", class_="price_color").text.replace("£", "").strip()

        print(f"Книга: {title} | Цена: {price} GBP")

except requests.exceptions.RequestException as e:
    print(f"🚨 ОШИБКА СЕТИ: {e}")