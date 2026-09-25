from uteka_parser import get_uteka_data
import json

if __name__ == '__main__':
    with open('settings.json', 'r', encoding='utf-8') as file:
        settings = json.load(file)

    url = 'https://spb.uteka.ru/product/prezervativy-durex-pleasuremax-343397/'

    id_product = url.split('/')[4].split('-')[-1]
    map_url = ''.join(['https://uteka.ru/checkout/pickup/picker/?isPickupOnly=true&fastOrderProductId=',
                       id_product,
                       '&fastOrderProductCount=1']
                      )

    all_response = get_uteka_data(map_url=map_url, channel=settings['browser'], city=settings['city'])
    print(all_response)
