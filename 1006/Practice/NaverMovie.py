from bs4 import BeautifulSoup
import urllib.request
html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.naver')
soup = BeautifulSoup(html, 'html.parser')

#전체 html 문서 출력
print("soup.prettify(): \n", soup.prettify())

tags = soup.findAll('div', attrs={'class':'tit3'})
#div 태그의 class=tit3인 태그를 모두 출력
print("tags: \n", tags)

print("tag.a: \n")
for tag in tags:
    #각 tag의 a태그 출력
    print(tag.a)

movieTitle = []
for tag in tags:
    movieTitle.append(tag.a.string)

#랭킹 내에 있는 모든 영화 제목 출력
print("\nmovieTitle: \n", movieTitle)
