import os
import sys
import urllib.request
from datetime import datetime, timedelta
import calendar
import time
import json
import math

#일자별 전국 교통량 //그 중에서도 1종(소형차), 2종(중형차), 6종(경차)
#https://www.data.go.kr/data/15062049/openapi.do
trafficKey = "2841870463"

#서울시 교통량 지점 정보
#http://data.seoul.go.kr/dataList/OA-13314/A/1/datasetView.do
spotKey = "6b6c6a6d6d6c696e353951484d5947"

#서울시 교통량 이력 정보
#http://data.seoul.go.kr/dataList/OA-13316/A/1/datasetView.do
seoulTrafficKey = "44666e45486c696e34334871624d76"

#서울시 행정동별 대중교통 총 승차 승객수 정보
#http://data.seoul.go.kr/dataList/OA-21223/S/1/datasetView.do
publicTransportKey = "79505379526c696e37344762416961"

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

def getTraffic(yyyymmdd):
    service_url = "http://data.ex.co.kr/openapi/trafficapi/nationalTrafficVolumn"

    parameters = "?key=" + trafficKey
    parameters += "&type=json"
    parameters += "&sumDate=" + yyyymmdd

    url = service_url + parameters

    retData = getRequestURL(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

def getDate(year, month, day):
    #연월일을 문자열로 변환
    date = str(year)
    if month < 10:
        date += '0' + str(month)
    elif month >= 10:
        date += str(month)
    if day < 10:
        date += '0' + str(day)
    elif day >= 10:
        date += str(day)
        
    return date

#def getMonthlyTrafficVolume(month)

def main():
    result = dict() #yyyymm 별 전국 교통량 데이터를 저장한 dictionary
    print("<< DATA CRAWLING START >>\n")

    isToday = False

    #연도별로 반복문 수행
    for year in range(2019, 2023):
        
        #월별로 반복문 수행
        for month in range(1, 13):
            
            nTrafficVolume = 0  #월별 전국 교통량
        
            monthLastDay = calendar.monthrange(year, month)[1]  #달의 마지막 일자
            
            #일별로 반복문 수행
            for day in range(1, monthLastDay + 1):

                date = getDate(year, month, day)
                print(date)

                nTrafficDataList= getTraffic(date)['list']  #가져온 데이터
                nTrafficDataLength = getTraffic(date)['count']  #총 데이터 개수

                for trafficData in nTrafficDataList:
                    if(trafficData['carType'] == '1' or trafficData['carType'] == '2' or trafficData['carType'] == '6'):
                        #가져온 데이터 중 차종 1/2/6종에 대해서만 교통량 조사
                        nTrafficVolume += int(trafficData['trafficVolumn'])

                #오늘 날짜 전(통계 없음)까지만 데이터 크롤링 수행
                if year == datetime.today().year and month == datetime.today().month and day == datetime.today().day - 1:
                    isToday = True
                    break

            result[date[:6]] = nTrafficVolume
            print(result)
            
            if isToday:
                break

if __name__ == '__main__':
    main()
