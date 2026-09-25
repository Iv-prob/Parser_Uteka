from playwright.sync_api import sync_playwright


def get_uteka_data(map_url, channel='chrome'):
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            'user_data',
            channel=channel,
            headless=False,
            args=['--start-maximized'],
            no_viewport=True,
        )

        page = browser.pages[0]
        page.goto(map_url)
        page.evaluate('window.scrollTo(0,0)')

        # page.mouse.move(x=960, y=540)
        # page.mouse.wheel(delta_y=500, delta_x=0)
        # page.mouse.wheel(delta_y=500, delta_x=0)
        # page.mouse.wheel(delta_y=500, delta_x=0)
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
