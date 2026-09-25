from playwright.sync_api import sync_playwright


all_responses = []


def scale(count, page):
    for _ in range(count):
        page.wait_for_timeout(600)
        page.mouse.wheel(delta_y=300, delta_x=0)


def scroll(page):
    current_scroll = 0
    scroll_step = 600
    while True:
        max_height = page.evaluate('document.body.scrollHeight')

        current_scroll += scroll_step
        page.evaluate(f'window.scrollTo(0, {current_scroll})')
        page.wait_for_timeout(600)

        if current_scroll >= max_height:
            page.wait_for_timeout(3000)
            break


def handle_response(response):
    global all_responses
    if 'map.Pharmacies' in response.url and response.status == 200:
        try:
            all_responses.append(response.json())
        except Exception:
            pass


def get_uteka_data(map_url, channel='chrome', city='Москва'):
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            'user_data',
            channel=channel,
            headless=False,
            args=['--start-maximized'],
            no_viewport=True,
        )

        # создаём окно браузера
        page = browser.pages[0]
        page.goto(map_url)
        page.wait_for_timeout(600)
        page.evaluate('window.scrollTo(0,0)')
        page.wait_for_timeout(600)

        # переводим поиск в нужный город
        page.get_by_role('button', name='1').click()
        page.locator('.pickup-picker-filters-content__city').wait_for(state='visible')
        page.locator('.pickup-picker-filters-content__city').click()
        page.wait_for_timeout(600)
        page.get_by_role('link', name=city, exact=True).click()
        page.wait_for_timeout(1000)

        # узнаём высоту и ширину экрана заказчика
        dimensions = {'width': page.evaluate('window.innerWidth'), 'height': page.evaluate('window.innerHeight')}

        # перемещаем курсор в центр экрана
        page.mouse.move(x=dimensions['width'] // 2, y=dimensions['height'] // 2)

        # отдаляем карту
        scale(5, page)

        page.get_by_role('button', name='Смотреть списком').click()
        page.wait_for_timeout(2000)

        page.locator('.ui-price_theme_primary').first.wait_for(state="visible")
        cards = page.locator('.pickup-picker-pharmacy-option-info').all()
        first_result = []
        for card in cards:
            title = card.locator('._size-tablet-300').inner_text()
            price = card.locator('.ui-price_theme_primary').inner_text()
            price = price.split('\\')[0]
            address = card.locator('[data-test="address"]').inner_text()
            first_result.append([price, title, address])
        print(first_result)

        page.on('response', handle_response)

        # скроллим вниз аптеки, формируем список
        scroll(page)

        page.remove_listener('response', handle_response)

        return all_responses, first_result


if __name__ == '__main__':
    pass
