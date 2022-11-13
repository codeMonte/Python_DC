import os
import sys
import urllib.request
from datetime import datetime
import calendar
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

import controlDate

#일자별 전국 교통량 //그 중에서도 1종(소형차), 2종(중형차), 6종(경차)
#https://www.data.go.kr/data/15062049/openapi.do
serviceKey = "2841870463"

#URL 요청
def getRequestURL(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            #print ("[%s] Url Request Success" % datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.now(), url))
        return None

def getTrafficData(yyyymmdd):
    service_url = "http://data.ex.co.kr/openapi/trafficapi/nationalTrafficVolumn"

    parameters = "?key=" + serviceKey
    parameters += "&type=json"
    parameters += "&sumDate=" + yyyymmdd

    url = service_url + parameters

    retData = getRequestURL(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

def addDailyTrafficVolume(list, result):
    #월 안의 모든 일 수에 대한 전국 교통량한 합계 반환
    for data in list:
        carType = data['carType']
        volume = int(data['trafficVolumn'])
        #가져온 데이터 중 차종 1/2/6종에 대해서만 교통량 조사
        if(carType == '1' or carType == '2' or carType == '6'):
            result += volume

    return result

def getMonthlyTrafficVolume(year, month, nTrafficVolume):
    monthLastDay = calendar.monthrange(year, month)[1]  #달의 마지막 일자
    for day in range(1, monthLastDay + 1):
    #일별로 반복문 수행
        date = controlDate.getDate(year, month, day)
        #print(date)    #확인용 출력

        nTrafficDataList = getTrafficData(date)['list']  #가져온 데이터
        nTrafficVolume = addDailyTrafficVolume(nTrafficDataList, nTrafficVolume)

    return nTrafficVolume

#{'202210': 154376498, '202211': 43207262}
def main():
    result = dict() #yyyymm 별 전국 교통량 데이터를 저장한 dictionary
    print("<< DATA CRAWLING START >>\n")

    year = 2022
    for month in range(1, 13):
    #월별로 반복문 수행
        if month == datetime.today().month:
            break
        
        nTrafficVolume = 0  #월별 전국 교통량
        nTrafficVolume = getMonthlyTrafficVolume(year, month, nTrafficVolume)

        yyyymm = controlDate.getDate(year, month)
        result[yyyymm] = nTrafficVolume
        print(result)
        
    #csv파일 저장
    temp = list(result.items())
    resultArr = []
    for item in temp:
        resultArr.append(list(item))
        
    ntraffic_table = pd.DataFrame(resultArr, columns=('Date(YYYYMM)', 'Traffic_Volume'))
    ntraffic_table.to_csv('../nationalTrafficVolume.csv', encoding="cp949", mode='w', index=True)

    #데이터 시각화
    TrafficYM = []
    TrafficCount = []
    index = []
    i = 0

    for date, count in result.items():
        index.append(i)
        TrafficYM.append(date)
        TrafficCount.append(count)
        i += 1

    font_location = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
    font_name = font_manager.FontProperties(fname = font_location).get_name()
    matplotlib.rc('font', family = font_name)


    plt.xticks(index, TrafficYM)
    plt.plot(index, TrafficCount, color = "#153462", marker='o', linestyle='--')
    plt.bar(TrafficYM, TrafficCount, color = "#bad1c2")
                
    plt.xlabel('연월 (YYYYMM)')
    plt.xticks(rotation=45)
    plt.ylabel('전국 교통량')
    plt.ticklabel_format(axis='y',useOffset=False, style='plain')
    plt.grid(True)
    plt.title("2022년 전국 월별 교통량")
    plt.show()

if __name__ == '__main__':
    main()
