import json

settings = {
    'city': 'Санкт-Петербург',
    'browser': 'chrome'
}


with open('settings.json', 'w', encoding='utf-8') as file:
    json.dump(settings, file, indent=4, ensure_ascii=False)
