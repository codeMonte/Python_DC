import urllib.request
from datetime import datetime
import calendar
import json
import xmltodict
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

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
    
    if len(spotVolumeData['VolInfo']) == 1:
    #데이터가 존재하지 않는 경우 예외처리
        return resultByTime

    spotVols = spotVolumeData['VolInfo']['row']
    
    for spot in spotVols:
        if len(spot) != 6:
            continue
        #if spotNum == 'A-06':
         #   print(len(spot))
          #  print(spot['vol'])
           # print(type(spot['vol']))
        resultByTime += int(spot['vol'])
        
    #print("getTimeSpotVolume(",spotNum, ", ", date, ", ", time, ") 호출 결과: ", resultByTime)  #확인용 출력
    return resultByTime

def getDailySpotVolume(spotNum, date):
#특정 연월일의 지점별 교통량 합계
    resultByDay = 0
    for hour in range(0, 24):
        
        if(date == "20221025"):
        #해당 날짜를 건너뛰는 이유는 이 날 데이터가 존재하지 않기 때문
            return 0
        
        time = controlDate.getTime(hour)  #시간
        resultByDay += getTimeSpotVolume(spotNum, date, time) #하루의 교통량 합계
        
    print("지점: ", spotNum, ", 일별 합계: ", date, resultByDay)    #확인용 출력
    return resultByDay

def getMonthlySpotVolume(spotNum, year, month, isItToday, result):
#특정 연월의 지점별 교통량 합계
    monthLastDay = calendar.monthrange(year, month)[1]
    for day in range(1, monthLastDay):
        if controlDate.isToday(year, month, day):
            isItToday[0] = True
            break
        date = controlDate.getDate(year, month, day)

        result += getDailySpotVolume(spotNum, date)
        
    print("지점: ", spotNum, ", 월별 합계: ", result) #확인용 출력
    return result

def main():
    result = dict()
    print("<< DATA CRAWLING START >>\n")

    spotNums = ['F-02', 'F-03', 'F-05']
    #모든 지점을 크롤링하는 것은 시간이 매우 오래 걸려
    #서울의 교통이 많이 지나가는 강변북로, 내부순환로, 동부간선도로를 추출하여 표본 집단으로 조사
    
    isItToday = [False] #참조 호출을 위한 배열 선언
        
    year = 2022
    for month in range(1, 13):
    #월별로 반복문 수행
        seoulMonthlyTrafficVolume = 0

        for spotNum in spotNums:
        #서울 전역 월별 교통량 합계
            print(year, "년", month, "월, 지역번호: ",spotNum, " 크롤링 중...")
            seoulMonthlyTrafficVolume = getMonthlySpotVolume(spotNum, year, month, isItToday, seoulMonthlyTrafficVolume)
                
        yyyymm = controlDate.getDate(year, month)
        result[yyyymm] = seoulMonthlyTrafficVolume

        print(result)
        
        if isItToday[0]:
            break

    
    year = datetime.today().year
    month = datetime.today().month
    yyyymm = controlDate.getDate(year, month)

    del result[yyyymm]
    print("서울 전역 월별: ", result)
        
    #csv파일 저장
    temp = list(result.items())
    resultArr = []
    for item in temp:
        resultArr.append(list(item))
        
    spotVol_table = pd.DataFrame(resultArr, columns=('Date(YYYYMM)', 'Spot_Volume'))
    spotVol_table.to_csv('../seoulSpotVolume.csv', encoding="cp949", mode='w', index=True)

    #데이터 시각화
    SpotVolumeYM = []
    SpotVolume = []
    index = []
    i = 0

    for date, volume in result.items():
        index.append(i)
        SpotVolumeYM.append(date)
        SpotVolume.append(volume)
        i += 1
        
    font_location = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
    font_name = font_manager.FontProperties(fname = font_location).get_name()
    matplotlib.rc('font', family = font_name)

    plt.xticks(index, SpotVolumeYM)
    plt.plot(index, SpotVolume, color = "#153462", marker='o', linestyle='--')
    plt.bar(SpotVolumeYM, SpotVolume, color = "#bad1c2")
    
    plt.xlabel('연월 (YYYYMM)')
    plt.xticks(rotation = 45)
    plt.ylabel('서울시 교통량')
    plt.ticklabel_format(axis='y',useOffset=False, style='plain')
    plt.grid(True)
    plt.title("2022년 서울시 월별 교통량 수")
    plt.show()

if __name__ == '__main__':
    main()
