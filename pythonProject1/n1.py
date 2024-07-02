import requests

cookies = {
    'vid': 'db0e9f93151b5389434d',
    'mkmgsgp': 'SFZP2Y',
    'mkmgrgp': 'SFZP2Y',
}

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'vid=db0e9f93151b5389434d; mkmgsgp=SFZP2Y; mkmgrgp=SFZP2Y',
    'priority': 'i',
    'referer': 'https://www.avito.ru/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'id': '8',
    'vid': 'SNkHj8xAZbCaADyb37WbKA',
}

response = requests.get('https://dm.hybrid.ai/match', params=params, cookies=cookies, headers=headers)
print(response.text)