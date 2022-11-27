import urllib.request
service_url = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
serviceKey = "KHOzLUHCJiwWHGvWP0HpN8wDENhC9bFA3XzTtAIaTyMFTe13jay%2FoQY2cveaXeY62p8%2BUCQIpwgKpvcZnEaHrA%3D%3D"

#parameters 생성하기
parameters = "?_type=json&serviceKey=" + serviceKey
parameters += "&YM=" + "201703"
parameters += "&SIDO=" + urllib.parse.quote("서울특별시")
parameters += "&GUNGU=" + urllib.parse.quote("종로구")
#성북구로 할 시에 경복궁이 성북구에 위치하지 않으므로 totalCount = 0으로 결과가 나온다.
parameters += "&RES_NM=" + urllib.parse.quote("경복궁")
parameters += "&pageNo=" + "1"
parameters += "&numOfRows=" + "100"

url = service_url + parameters
req = urllib.request.Request(url)

#url open 요청 보내기 & 응답 받기
response = urllib.request.urlopen(req)
decodeData = response.read().decode('utf-8')

#응답 받은 데이터 확인하기
import json
jsonData = json.loads(decodeData)
print("jsonData 출력\n", jsonData)
print("\n")

print("jsonData.keys() 출력\n", jsonData.keys())
print("\n")

print("jsonData['response'].keys() 출력\n", jsonData['response'].keys())
print("\n")

print("jsonData['response']['body'].keys() 출력\n", jsonData['response']['body'].keys())

print("\n-----End-----")
