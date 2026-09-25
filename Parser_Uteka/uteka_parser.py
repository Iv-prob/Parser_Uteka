from playwright.sync_api import sync_playwright


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
        page.evaluate('window.scrollTo(0,0)')

        # переводим поиск в нужный город
        page.get_by_role('button', name='1').click()
        page.locator('.pickup-picker-filters-content__city').click()
        page.wait_for_timeout(600)
        page.get_by_role('link', name=city, exact=True).click()
        page.evaluate('window.scrollTo(0,0)')
        page.wait_for_timeout(600)

        # узнаём высоту и ширину экрана заказчика
        dimensions = page.viewport_size

        page.mouse.move(x=dimensions['width'] // 2, y=dimensions['hight'] // 2)
        page.wait_for_timeout(600)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.wait_for_timeout(1000)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.wait_for_timeout(1000)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.wait_for_timeout(1000)
        # page.mouse.wheel(delta_y=500, delta_x=0)
        # page.wait_for_timeout(1000)
        # page.mouse.wheel(delta_y=500, delta_x=0)
        # page.mouse.wheel(delta_y=500, delta_x=0)
        # page.mouse.wheel(delta_y=500, delta_x=0)
        # page.mouse.wheel(delta_y=500, delta_x=0)
        # page.wait_for_timeout(10000)
        #
        # with page.expect_response(lambda response: 'map.Cluster' in response.url) as response_info:
        #     page.get_by_role("button", name='Сегодня').click()
        #     page.wait_for_timeout(5000)
        #
        # return response_info.value.json()
        page.wait_for_timeout(4000000)


if __name__ == '__main__':
    pass
