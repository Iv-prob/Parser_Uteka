from bs4 import BeautifulSoup
import os
import requests
import pandas as pd


def unloading(data_list):
    df = pd.DataFrame(data_list)
    df.to_excel('123.xlsx', index=False)


def parsing(address):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/120.0.0.0 Safari/537.36"}

    with open(address, encoding='utf-8') as f:
        data = f.read()
        soup = BeautifulSoup(data, 'html.parser')
        lines = soup.find_all('td', class_='istr', attrs={'width': '400'})

        catalog = []
        for i in lines:
            name_and_garbage = i.text.split(',')
            name = name_and_garbage[0].strip()

            prev = i.find_previous_sibling('td')
            img_1 = prev.find('img')
            link_side = img_1['src']

            prev_prev = prev.find_previous_sibling('td')
            img_2 = prev_prev.find('img')
            link_front = img_2['src']

            with open(f'images/{name} front.jpg', 'wb') as f_2:
                img_b_front = requests.get(link_front, headers=headers, timeout=5)
                f_2.write(img_b_front.content)
            with open(f'images/{name} side.jpg', 'wb') as f_2:
                img_b_side = requests.get(link_side, headers=headers, timeout=5)
                f_2.write(img_b_side.content)

            i_parent = i.parent
            text_now = i_parent.find_all('td', attrs={'class': 'istr', 'width': '100'})
            catalog.append({'name': name,
                            'link_front': link_front,
                            'link_side': link_side,
                            'diopters': text_now[0].text,
                            'price': text_now[3].text})

            i_parent_next = i_parent.find_next_sibling('tr')
            while i_parent_next:
                text_now = i_parent_next.find_all('td', attrs={'class': 'istr', 'width': '100'})
                catalog.append({'name': name,
                                'link_front': link_front,
                                'link_side': link_side,
                                'diopters': text_now[0].text,
                                'price': text_now[3].text})
                i_parent_next = i_parent_next.find_next_sibling('tr')

        return catalog


if __name__ == '__main__':
    if not os.path.exists('images'):
        os.makedirs('images')

    data_list_dict = parsing('МирОптик 35 (1) (1).html')
    unloading(data_list_dict)

