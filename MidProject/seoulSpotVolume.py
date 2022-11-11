import os
import sys
import urllib.request
from datetime import datetime, timedelta
import calendar
import time
import json
import math
import xmltodict

import seoulSpotNum #서울시 교통량 지점 정보 모듈
import controlDate

#서울시 교통량 이력 정보
#http://data.seoul.go.kr/dataList/OA-13316/A/1/datasetView.do
serviceKey = "44666e45486c696e34334871624d76"

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

def getSpotVolumeData(spotNum, date, time):
#서울시 지점별 교통량 이력 URL 요청
    service_url = "http://openapi.seoul.go.kr:8088/"

    parameters = serviceKey
    parameters += "/xml"
    parameters += "/VolInfo"
    parameters += "/1"
    parameters += "/4" #API에서 제공하는 마지막 행 번호가 4
    parameters += "/" + spotNum
    parameters += "/" + date #20190101~today
    parameters += "/" + time #00~23시
    
    url = service_url + parameters

    retData = getRequestURL(url)

    dictRetData = xmltodict.parse(retData)
    jsonRetData = json.dumps(dictRetData)

    if(retData == None):
        return None
    else:
        return json.loads(jsonRetData)

def getTimeSpotVolume(spotNum, date, time):
#특정 날짜의 특정 시간의 지점별 교통량 반환
    resultByTime = 0;

    #spotNum에 해당하는 지점의 해당 날짜 해당 시간의 교통량을 가져온다
    spotVolumeData = getSpotVolumeData(spotNum, date, time)

    spotVols = spotVolumeData['VolInfo']['row']
    
    for spot in spotVols:
        resultByTime += int(spot['vol'])
        
    #print("TIME: ", date, time, resultByTime)  #확인용 출력
    return resultByTime

def getDailySpotVolume(spotNum, date):
#특정 연월일의 지점별 교통량 합계
    resultByDay = 0
    for hour in range(0, 24):
        
        if(date == "20190101" and hour == 0):
        #해당 날짜를 건너뛰는 이유는 이 날 00시 데이터만 존재하지 않기 때문
            continue
        
        time = controlDate.getTime(hour)  #시간
        resultByDay += getTimeSpotVolume(spotNum, date, time) #하루의 교통량 합계
        
    print("DAILY: ", date, resultByDay)    #확인용 출력
    return resultByDay

def getMonthlySpotVolume(spotNum, year, month, isItToday, result):
#특정 연월의 지점별 교통량 합계
    monthLastDay = calendar.monthrange(year, month)[1]
    for day in range(1, monthLastDay + 1):
        if controlDate.isToday(year, month, day):
            isItToday[0] = True
            break
        date = controlDate.getDate(year, month, day)

        result += getDailySpotVolume(spotNum, date)
        
    print("SPOT: ", spotNum, ", MONTHLY SUM: ", result) #확인용 출력
    return result

def main():
    result = dict()
    print("<< DATA CRAWLING START >>\n")

    spotNums = seoulSpotNum.getAllSpotNum()
    
    isItToday = [False] #참조 호출을 위한 배열 선언
        
    for year in range(2019, 2023):
    #연도별로 반복문 수행
        for month in range(1, 13):
        #월별로 반복문 수행
            
            seoulMonthlyTrafficVolume = 0

            for spotNum in spotNums:
            #서울 전역 월별 교통량 합계
                print(year, "년", month, "월, 지역번호: ",spotNum, " 크롤링 중...")
                seoulMonthlyTrafficVolume = getMonthlySpotVolume(spotNum, year, month, isItToday, seoulMonthlyTrafficVolume)

            yyyymm = controlDate.getDate(year, month)
            result[yyyymm] = seoulMonthlyTrafficVolume
            
            if isItToday[0]:
                break
            
    print("SEOUL 월별: ", result)
        

if __name__ == '__main__':
    main()
