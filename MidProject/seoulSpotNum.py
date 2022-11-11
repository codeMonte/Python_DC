import os
import sys
import urllib.request
from datetime import datetime, timedelta
import calendar
import time
import json
import math
import xmltodict


#서울시 교통량 지점 정보
#http://data.seoul.go.kr/dataList/OA-13314/A/1/datasetView.do
spotKey = "6b6c6a6d6d6c696e353951484d5947"

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

def getAllSpotData():
    service_url = "http://openapi.seoul.go.kr:8088/"

    parameters = spotKey
    parameters += "/xml"
    parameters += "/SpotInfo"
    parameters += "/1/139"  #첫 페이지부터 마지막(139) 페이지까지 크롤링

    url = service_url + parameters

    retData = getRequestURL(url)

    dictRetData = xmltodict.parse(retData)
    jsonRetData = json.dumps(dictRetData)

    if(retData == None):
        return None
    else:
        return json.loads(jsonRetData)

def getAllSpotNum():
    spotNums = []
    spotData = getAllSpotData()['SpotInfo']['row']
    for spot in spotData:
        spotNums.append(spot['spot_num'])
    return spotNums

def main():
    result = []
    print("<< DATA CRAWLING START >>\n")

    spotNums = getAllSpotNum()    

if __name__ == '__main__':
    main()
