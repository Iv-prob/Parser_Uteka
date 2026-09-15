from bs4 import BeautifulSoup


# def prev_element(element):
#     return


def parsing(adress):
    with open(adress, encoding='utf-8') as file:
        data = file.read()
        soup = BeautifulSoup(data, 'html.parser')
        lines = soup.find_all('td', class_='istr', attrs={'width': '400'})

        catalog = []
        for i in lines:
            name_and_garbage = i.text.split(',')
            name = name_and_garbage[0].strip()

            prev = i.find_previous_sibling('td')
            img = prev.find('img')
            link_1 = img['src']

            prev_prev = prev.find_previous_sibling('td')
            img_2 = prev_prev.find('img')
            link_2 = img_2['src']

            catalog

if __name__ == '__main__':
    parsing('МирОптик 35 (1) (1).html')
