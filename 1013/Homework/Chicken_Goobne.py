from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from itertools import count

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#[CODE 1]
def Goobne_store(result):
    Goobne_URL = "https://www.goobne.co.kr/store/search_store.asp"
    wd = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    time.sleep(1)
    wd.get(Goobne_URL)
    wd.get(Goobne_URL)
    #wd.execute_script("chgSido('경기도')")
    wd.execute_script("goSearch('N')")
    time.sleep(1)
    GNhtml = wd.page_source
    soupGN = BeautifulSoup(GNhtml, 'html.parser')
    store_GN = soupGN.findAll('div', attrs = {'class':'desc'})
    store_GN = store_GN[5:]

    for i in range(0, 10):
        try:
            store_name = store_GN[i].select("dt")[0].string
            print(store_name)
            store_address = store_GN[i].select("dd.local")[0].string
            print(store_address)
            store_phone = store_GN[i].select("dd.num")[0].string
            print(store_phone)
            print()
            result.append([store_name] + [store_address] + [store_phone])
        except Exception as e:
            print("Exception executed\n", e)
            continue
    return

#[CODE 0]
def main():
    result = []
    print('Goobne store crawling >>>>>>>>>>')
    Goobne_store(result)

    GN_tbl = pd.DataFrame(result, columns = ('store', 'address', 'phone'))
    GN_tbl.to_csv('./Chicken_Goobne.csv', encoding = 'cp949', mode = 'w', index = True)

if __name__ == '__main__':
    main()
