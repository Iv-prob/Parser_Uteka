from playwright.sync_api import sync_playwright


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
        if page.locator('button', name='1').wait_for(state="visible"):
            page.get_by_role('button', name='1').click()
        page.wait_for_timeout(600)
        page.locator('.pickup-picker-filters-content__city').click()
        page.wait_for_timeout(600)
        page.get_by_role('link', name=city, exact=True).click()
        page.wait_for_timeout(1000)
        # page.evaluate('window.scrollTo(0,0)')
        # page.wait_for_timeout(600)

        # узнаём высоту и ширину экрана заказчика
        dimensions = {'width': page.evaluate('window.innerWidth'), 'height': page.evaluate('window.innerHeight')}

        # скроллим, чтобы весь город было видно
        page.mouse.move(x=dimensions['width'] // 2, y=dimensions['height'] // 2)
        page.wait_for_timeout(600)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.wait_for_timeout(1000)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.wait_for_timeout(1000)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.wait_for_timeout(1000)

        page.get_by_role('button', name='Смотреть списком').click()
        page.wait_for_timeout(600)

        scroll(page)
        # current_scroll = 0
        # scroll_step = 600
        # while True:
        #     max_height = page.evaluate('document.body.scrollHeight')
        #
        #     current_scroll += scroll_step
        #     page.evaluate(f'window.scrollTo(0, {current_scroll})')
        #     page.wait_for_timeout(600)
        #
        #     if current_scroll >= max_height:
        #         page.wait_for_timeout(3000)
        #         break


        #
        # with page.expect_response(lambda response: 'map.Cluster' in response.url) as response_info:
        #     page.get_by_role("button", name='Сегодня').click()
        #     page.wait_for_timeout(5000)
        #
        # return response_info.value.json()
        page.wait_for_timeout(4000000)


if __name__ == '__main__':
    pass
