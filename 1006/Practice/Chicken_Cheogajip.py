import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count

#import ssl

#[CODE 1]
def CheogajipAddress(result):
    for page_idx in count():
        Cheogajip_URL = 'https://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=%s' %str(page_idx + 1)
        print(Cheogajip_URL)
        response = urllib.request.urlopen(Cheogajip_URL)
        soupData = BeautifulSoup(response, 'html.parser')
        tbody_tag = soupData.find('tbody')
    
        for store_tr in tbody_tag.findAll('tr'):
            if(len(store_tr) <= 3):
                #마지막 페이지 이상을 넘어가지 않도록 크롤링을 끝낸다.
                print("LAST PAGE = ", page_idx)
                return
            tr_tag = list(store_tr.strings)
            store_name = tr_tag[1]
            store_address = tr_tag[3]
            store_sido_gu = store_address.split()[:2]
            store_phone = tr_tag[5]
            result.append([store_name] + store_sido_gu + [store_address] + [store_phone])

        #print(tr_tag)

#[CODE 0]
def cswin_Cheogajip():
    result = []

    print("CHEOGAJIP ADDRESS CRAWLING START")
    CheogajipAddress(result) #[CODE 1] 호출
    cheogajip_table = pd.DataFrame(result, columns = ('store', 'sido', 'gungu', 'store_address', 'store_phone'))
    cheogajip_table.to_csv("./cheogajip.csv", encoding = "cp949", mode = 'w', index = True)
    del result[:]

    print('FINISHED')

if __name__ == '__main__':
    cswin_Cheogajip()
