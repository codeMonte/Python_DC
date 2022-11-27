from bs4 import BeautifulSoup
html = '<h1 id="title">한빛출판네트워크</h1><div class="top"><ul class="menu"><li><a href="http://www.hanbit.co.kr/member/login.html" class="login">로그인</a></li></ul><ul class="brand"><li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li><li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li></ul></div>'

#BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

#객체에 저장된 html 내용 확인
print("soup.prettify() 출력\n", soup.prettify())
print("\n")

#태그 파싱(parse)하기 - 지정된 한 개의 태그만 파싱
tag_h1 = soup.h1
print("tag_h1 출력\n", tag_h1)
print("\n")

tag_div = soup.div
print("tag_div 출력\n", tag_div)
print("\n")

tag_ul = soup.ul
print("tag_ul 출력\n", tag_ul)
print("\n")

tag_li = soup.li
print("tag_li 출력\n", tag_li)
print("\n")

tag_a = soup.a
print("tag_a 출력\n", tag_a)
print("\n")

tag_ul_all = soup.find_all("ul")
print("tag_ul_all 출력\n", tag_ul_all)
print("\n")

tag_li_all = soup.find_all("li")
print("tag_li_all 출력\n", tag_li_all)
print("\n")

tag_a_all = soup.find_all("a")
print("tag_a_all 출력\n", tag_a_all)
print("\n")

print("tag_a.attrs 출력\n", tag_a.attrs)
print("\n")

print("tag_a.['href'] 출력\n", tag_a['href'])
print("\n")

print("tag_a.['class'] 출력\n", tag_a['class'])
print("\n")

tag_ul_2 = soup.find('ul', attrs={'class':'brand'})
print("tag_ul_2 출력\n", tag_ul_2)
print("\n")

title = soup.find(id="title")
print("title 출력\n", title)
print("\n")

print("title.string 출력\n", title.string)
print("\n")

li_list = soup.select("div>ul.brand>li")
print("li_list 출력\n", li_list)

for li in li_list:
    print("li.string 반복문을 이용해 출력\n", li.string)

print("\n -----End-----")
