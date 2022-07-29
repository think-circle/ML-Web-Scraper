
from bs4 import BeautifulSoup
import requests
from random import choice


def get_proxies():
    proxy_url = 'https://github.com/clarketm/proxy-list/blob/394e323c7aabb47339886ddfe34ff4b57e0338e4/proxy-list-raw.txt'
    r = requests.get(proxy_url)
    soup = BeautifulSoup(r.content,'lxml').find_all("td",{"class":"blob-code blob-code-inner js-file-line"})

    proxies = [proxy.text for proxy in soup]
    return proxies

proxies = get_proxies()

def get_random_proxy(proxies):
    return {'https': choice(proxies)}


def get_working_proxies():
    for i in range(30):
        proxy = get_random_proxy(proxies)
        print(f"Using proxy {proxy}")
        try:
            r = requests.get('https://ewww.google.com/',proxies= proxy,timeout=3)
            print(r.status_code)
        except:
            pass

get_working_proxies()