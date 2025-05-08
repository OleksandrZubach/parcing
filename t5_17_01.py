import re

import requests, lxml
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

try:
    url='https://realpython.github.io/fake-jobs/'
    response=requests.get(url)
    # content = response.text
    # print(content.find('title'))
    soup = BeautifulSoup(response.text,'lxml')
    # print(soup.title.text)

    c = soup.find_all('h2')
    # print(c)
    list_t=[]
    for i in c:
        list_t.append(i.text)
    print(list_t)

    # conten=soup.find_all('h3',class_='subtitle is-6 company')
    # print(conten)

    # conten2=soup.find(class_='card-footer').find_all(class_='card-footer-item')
    # [print(i.text) for i in conten2]
    # print(conten2)

    # conten3 = soup.find(class_='card-footer').find_all(class_='card-footer-item')
    # conten4 = soup.find_all('a')
    # for i in conten4:
    #     print(i.get('href'))
    # print(conten3)

    # c = soup.find_all('h2')
    # print(c)
    # list_t = []
    # for i in c:
    #     if "Python" in i.text:
    #         list_t.append(i.text)
    #     else:
    #         pass
    # print(list_t)
    # lis=[]
    # conten5 = soup.find_all('h2', string=re.compile('[Ee]ngineer'))
    # print(conten5)
    # for i in conten5:
    #     lis.append(i.text)
    # print(lis)

except HTTPError as er:
    print(f'Error is {er}')
except Exception as r:
    print(f'Error {r}')