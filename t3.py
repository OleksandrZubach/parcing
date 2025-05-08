# import requests
# from requests.exceptions import HTTPError
# from my_token import API_TOKEN
#
# try:
#     headers = {
#         "Accept": "application/json",
#         "Accept-Encoding": "gzip, deflate, br, zstd",
#         "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
#         "Host": "httpbin.org",
#         "Priority": "u=1, i",
#         "Referer": "https://httpbin.org/",
#         "Sec-Ch-Ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
#         "Sec-Ch-Ua-Mobile": "?0",
#         "Sec-Ch-Ua-Platform": "\"Windows\"",
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-origin",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#         "X-Amzn-Trace-Id": "Root=1-67652a5b-52d9f2e731314ffc7a380020"
#     }
#     url = 'https://httpbin.org/headers'
#     response=requests.get(url, headers = headers)
#     response.raise_for_status()
#     print(response.json())
# except (HTTPError, ValueError) as er:
#     print(f'Error is {er}')
#












import requests, fake_useragent
from requests.exceptions import HTTPError
from my_token import API_TOKEN

try:
    user = fake_useragent.UserAgent().random
    headers = {"User-Agent":user
    }
    url = 'https://httpbin.org/headers'
    response=requests.get(url, headers = headers)
    response.raise_for_status()
    print(response.json())
except (HTTPError, ValueError) as er:
    print(f'Error is {er}')
