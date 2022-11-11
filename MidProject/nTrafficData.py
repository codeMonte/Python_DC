import os
import sys
import urllib.request
from datetime import datetime
import calendar
import json

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

def getMonthlyTrafficVolume(year, month, isItToday, nTrafficVolume):
    monthLastDay = calendar.monthrange(year, month)[1]  #달의 마지막 일자
    for day in range(1, monthLastDay + 1):
    #일별로 반복문 수행
        if controlDate.isToday(year, month, day):
        #오늘 날짜 전(통계 없음)까지만 데이터 크롤링 수행
            isItToday[0] = True
            break
        date = controlDate.getDate(year, month, day)
        print(date)

        nTrafficDataList = getTrafficData(date)['list']  #가져온 데이터
        nTrafficVolume = addDailyTrafficVolume(nTrafficDataList, nTrafficVolume)

    return nTrafficVolume

#{'202210': 154376498, '202211': 43207262}
def main():
    result = dict() #yyyymm 별 전국 교통량 데이터를 저장한 dictionary
    print("<< DATA CRAWLING START >>\n")

    isItToday = [False] #참조 호출을 위한 배열 선언

    for year in range(2019, 2023):
    #연도별로 반복문 수행
        for month in range(1, 13):
        #월별로 반복문 수행
            
            nTrafficVolume = 0  #월별 전국 교통량
            nTrafficVolume = getMonthlyTrafficVolume(year, month, isItToday, nTrafficVolume)

            yyyymm = controlDate.getDate(year, month)
            result[yyyymm] = nTrafficVolume
            print(result)
            
            if isItToday[0]:
                break
            

if __name__ == '__main__':
    main()
