import requests, fake_useragent
from requests.exceptions import HTTPError
from my_token import API_TOKEN

try:
    for num in range(5):
        user = fake_useragent.UserAgent().random
        headers = {"User-Agent":user
        }
        url = 'https://picsum.photos/200'
        response=requests.get(url, headers = headers)
        response.raise_for_status()
        with open(f'{num}.jpg', 'wb') as file:
            file.write(response.content)
except (HTTPError, ValueError) as er:
    print(f'Error is {er}')
