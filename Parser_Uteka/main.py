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

    count = 1
    result = []
    for i in all_response:
        for y in i['result']['pharmacies']:
            title = i['result']['pharmacies'][str(y)]['pharmacy']['title']
            address = i['result']['pharmacies'][str(y)]['pharmacy']['address']
            price = i['result']['pharmacies'][str(y)]['cart'][0]['price']
            result.append([price, title, address])
            count += 1

    result.sort()
    for i in result:
        print(i)
    print(count)

