import urllib.request
from datetime import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

import controlDate

#서울시 행정동별 대중교통 총 승차 승객수 정보
#http://data.seoul.go.kr/dataList/OA-21223/S/1/datasetView.do
serviceKey = "58417462646c696e3734485a43676e"

#URL 요청
def getRequestURL(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            #print ("[%s] Url Request Success" % datetime.now())
            retData = response.read().decode('utf-8')
            return retData
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.now(), url))
        return None

def getPassengerCountURL(startPage, endPage):
    service_url = "http://openapi.seoul.go.kr:8088/"

    parameters = serviceKey
    parameters += "/json"
    parameters += "/tpssPassengerCnt"
    parameters += "/" + str(startPage)  #검색 시작 페이지 번호
    parameters += "/" + str(endPage)   #검색 마지막 페이지 번호 ~132288

    url = service_url + parameters

    urlData = getRequestURL(url)

    if(urlData == None):
        return None
    else:
        result = json.loads(urlData)
        return result['tpssPassengerCnt']['row']

def getDailyPassengerCount(psgrData, total, result):
    for data in psgrData:
        total[0] += 1
        if total[0] > 132288:
            break
            
        date = data['CRTR_DT']

        if date in result:
            count = data['PSGR_CNT']
            result[date] += count
        elif not(date in result):
            result[date] = data['PSGR_CNT']

def getMonthlyPassengerCount(yyyymm, count, result):
    if yyyymm in result:
        result[yyyymm] += count
    elif not(yyyymm in result):
        result[yyyymm] = count

def main():
    print("<< DATA CRAWLING START >>\n")

    total = [0]    #참조 호출을 위한 배열 선언
    start = 1
    end =  1000
    
    
    dailyResult = dict()

    while total[0] <= 132288:
        print("현재 크롤링한 페이지 수: ", total[0], ", ", start, "페이지부터 ", end, "페이지까지 크롤링 중...")  #확인용 출력
        tpssPassengerData = getPassengerCountURL(start, end)

        getDailyPassengerCount(tpssPassengerData, total, dailyResult)

        #print("TOTAL: ",total[0])  #확인용 출력
        #print(dailyResult)   #확인용 출력

        if total[0] > 132288:
            print(total[0], " 마지막 데이터 인덱스 초과, 크롤링 종료.")
            break

        #연산이 끝나면 다음 1000페이지 호출
        start += 1000
        end += 1000

    monthlyResult = dict()

    for date, count in dailyResult.items():
    #일별로 정리된 데이터를 월별로 추출
        yyyymm = date[:6]
        
        if yyyymm == '202112':  #2021년 데이터는 12월 31일, 12월 30일만 있으므로 제외.
            break
        
        getMonthlyPassengerCount(yyyymm, count, monthlyResult)
        #print(monthlyResult)

    monthlyResult = dict(sorted(monthlyResult.items()))
    
    year = datetime.today().year
    month = datetime.today().month
    yyyymm = controlDate.getDate(year, month)

    del monthlyResult[yyyymm]
    print("MONHTLY RESULT: ", monthlyResult)
        
    #csv파일 저장
    temp = list(monthlyResult.items())
    resultArr = []
    for item in temp:
        resultArr.append(list(item))
        
    publicTransport_table = pd.DataFrame(resultArr, columns=('Date(YYYYMM)', 'Passenger_Count'))
    publicTransport_table.to_csv('../publicTransportUsage.csv', encoding="cp949", mode='w', index=True)


    #데이터 시각화
    PassengerYM = []
    PassengerCount = []
    index = []
    i = 0

    for date, count in monthlyResult.items():
        index.append(i)
        PassengerYM.append(date)
        PassengerCount.append(count)
        i += 1
    
    font_location = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
    font_name = font_manager.FontProperties(fname = font_location).get_name()
    matplotlib.rc('font', family = font_name)

    plt.xticks(index, PassengerYM)
    plt.plot(index, PassengerCount, color = "#153462", marker='o', linestyle='--')
    plt.bar(PassengerYM, PassengerCount, color = "#bad1c2")
    
    plt.xlabel('연월 (YYYYMM)')
    plt.xticks(rotation = 45)
    plt.ylabel('승차 인원 수')
    plt.ticklabel_format(axis='y',useOffset=False, style='plain')
    plt.grid(True)
    plt.title("2022년 서울시 월별 대중교통 이용자 수")
    plt.show()


if __name__ == '__main__':
    main()
