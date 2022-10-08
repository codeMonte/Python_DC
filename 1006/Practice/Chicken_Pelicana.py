import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count

import ssl

def get_request_url(url, enc='utf-8'):
    req = urllib.request.Request(url)

    try:
        ssl_create_default_https_context = ssl._create_unverified_context #접속 보안 허용

        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')

            return ret

    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getPelicanaAddress(result):
    for page_idx in count(): #itertools 안에 있는 count()
        Pelicana_URL = 'https://pelicana.co.kr/store/stroe_search.html?page=%s&branch_name=&gu=&si=' %str(page_idx + 1)
        print("[Pelicana Page] : [%s]" % (str(page_idx + 1)))

        rcv_data = get_request_url(Pelicana_URL)
        soupData = BeautifulSoup(rcv_data, 'html.parser')

        store_table = soupData.find('table', attrs={'class':'table mt20'})
        tbody = store_table.find('tbody')
        bEnd = True
        for store_tr in tbody.findAll('tr'):
            bEnd = False
            tr_tag = list(store_tr.strings)
            store_name = tr_tag[1]
            store_address = tr_tag[3]
            store_sido_gu = store_address.split()[:2]

            result.append([store_name] + store_sido_gu + [store_address])

        if(bEnd == True):
            print(result[0]) #확인용 출력
            print(" == 데이터 수 : %d", len(result))
            return

    return

def cswin_pelicana():
    result = []
    print("PELICANA ADDRESS CRAWLING START")
    getPelicanaAddress(result)
    pelicana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    pelicana_table.to_csv("./pelicana.csv", encoding = "cp949", mode = 'w', index = True)
    del result[:] #종료하지 않고 여러 번 실행 한 경우 중복(누적) 저장이 됨
    print("FINISHED")

if __name__ == '__main__':
    cswin_pelicana()
