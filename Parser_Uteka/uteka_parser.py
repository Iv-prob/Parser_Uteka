from playwright.sync_api import sync_playwright


def get_uteka_data(map_url, channel='chrome'):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel=channel)

        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        page.goto(map_url)
        page.wait_for_timeout(5000)

        page.mouse.move(x=960, y=540)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.wait_for_timeout(1000)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.mouse.wheel(delta_y=500, delta_x=0)
        page.wait_for_timeout(10000)

        with page.expect_response(lambda response: 'map.Cluster' in response.url) as response_info:
            page.get_by_role("button", name='Сегодня').click()
            page.wait_for_timeout(5000)

        return response_info.value.json()


if __name__ == '__main__':
    pass
    # city = 'spb.'
    # url = 'https://spb.uteka.ru/product/prezervativy-durex-pleasuremax-343397/'
    # id_product = url.split('/')[4].split('-')[-1]
    # product_url = ''.join(
    #     ['https://', city, 'uteka.ru/checkout/pickup/picker/?fastOrderProductCount=1&fastOrderProductId=', id_product])
    #
    # json_data = get_uteka_data(product_url)
    #
    # count = len(json_data['result']['pharmacyLists']['byMinPrice'])
    #
    # partners = json_data['result']['partners']
    # result = []
    # for i in range(count):
    #     partner_id = json_data['result']['pharmacyLists']['byMinPrice'][i]['partnerId']
    #     price = (json_data['result']['pharmacyLists']['byMinPrice'][i]['price'])
    #     name_partner = partners[str(partner_id)]['title']
    #
    #     result.append({f'{partner_id}': [price, name_partner]})
    #
    # print(result)
    # print(json_data['result']['count'])

