Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
a = 123
a = 12.34
a = 1 + 2j
a
(1+2j)
a.real
1.0
a.imag
2.0
a.conjugate()
(1-2j)
abs(a)
2.23606797749979
a = 0o12
a
10
a = 0 * 12A
SyntaxError: invalid decimal literal
a = 0 x 12A
SyntaxError: invalid decimal literal
a=0x12A
a
298
b=True
b
True
a = 3
b = 4
a + b
7
a - b
-1
a * b
12
a / b
0.75
a ** b
81
2 ** 3
8
2 *8 7
SyntaxError: invalid syntax
2 ** 7
128
a % b
3
7 % 3
1
7 //3
2
s1 = "Hello Python"
s1
'Hello Python'
s2 = 'Hello Python'
s2
'Hello Python'
s3 = '''Hello Python'''
s3
'Hello Python'
s4 = """Hello Python"""
s4
'Hello Python'
head = "Python"
tail = " is fun"
head + tail
'Python is fun'
head * 2
'PythonPython'
print("=" * 5)
=====
a = "Now is better than never"
a
'Now is better than never'
a[0]
'N'
a[4]
'i'
a[-2]
'e'
a[-1]
'r'
b=a[0] + a[1] + a[2]
b
'Now'
a[0:3]
'Now'
a
a[4:6]
'is'
a[19:]
'never'
a[:3]
'Now'
a[:]
'Now is better than never'
a[7:-11]
'better'
a = "Python"
a
a.count('p')
0
a.find('y')
1
a.find('p')
-1
a.index('y')
1
a.index('p')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.index('p')
ValueError: substring not found
b=","
c=b.join('Abcd')
c
'A,b,c,d'
a.upper()
'PYTHON'
a.lower()
'python'
d='     py     '
d.lstrip()
'py     '
d.rstrip()
'     py'
d.strip()
'py'
d
'     py     '
a='Pithon'
a[1] = y
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a[1] = y
NameError: name 'y' is not defined
a[1] = 'y'
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a[1] = 'y'
TypeError: 'str' object does not support item assignment
a="Python is difficult."
a.replace("difficult", "funny")
'Python is funny.'
a.split()
['Python', 'is', 'difficult.']
b
','
b="a,b,c,d"
b
'a,b,c,d'
b.split(',')
['a', 'b', 'c', 'd']
a=[1,2,3]
b=['Life', 'is', 'too', 'short']
c=[1,2,'Life','is']
d=[1,2,[3,4],['Life','is']]
d[0]
1
d[2]
[3, 4]
d[3]
['Life', 'is']
d[3][-1]
'is'
d[0:3]
[1, 2, [3, 4]]
a+b
[1, 2, 3, 'Life', 'is', 'too', 'short']
b[0] + "Hey~! *^^*"
'LifeHey~! *^^*'
a[0] + " Hey~? *^^*;"
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a[0] + " Hey~? *^^*;"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
a * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a[2] = 99
a
[1, 2, 99]
a[1:2] = ['a','b','c']
a
[1, 'a', 'b', 'c', 99]
a[-1]=['d','e','f'
       ]
a
[1, 'a', 'b', 'c', ['d', 'e', 'f']]
del a[-1]
a
[1, 'a', 'b', 'c']
a.append(5)
a
[1, 'a', 'b', 'c', 5]
a=[3,4,1,9]
a.reverse()
a
[9, 1, 4, 3]
a.index(9)
0
a.index(1)
1
a.insert(0, 99)
a
[99, 9, 1, 4, 3]
a.remove(99)
a
[9, 1, 4, 3]
b=[1,2,3]
b.pop()
3
b
[1, 2]
b.pop(0)
1b

b
[2]
a=[2,1,0,2,3,2,4,2]
a.count(0)
1
a.count(2)
4
t1=(1, )
t2=(1,2,3)
t3=1,2,3
t3
(1, 2, 3)
t4=(1,2,(3,4),('Life','is'))
t4[0]
1
t4[3][-1]
'is'
t4[0:3]
(1, 2, (3, 4))
t1 + t2
(1, 1, 2, 3)
t1 + " Hi"
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    t1 + " Hi"
TypeError: can only concatenate tuple (not "str") to tuple
t2 * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
t2[2] = 99
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    t2[2] = 99
TypeError: 'tuple' object does not support item assignment
dic= {'name':'TaeHwan','phone':'01012345678','birth':'0109'}
dic[1]='a'
dic
{'name': 'TaeHwan', 'phone': '01012345678', 'birth': '0109', 1: 'a'}
dic['pet']='dog'
dic
{'name': 'TaeHwan', 'phone': '01012345678', 'birth': '0109', 1: 'a', 'pet': 'dog'}
del dic[1]
dic
{'name': 'TaeHwan', 'phone': '01012345678', 'birth': '0109', 'pet': 'dog'}
dic['pet']
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    ic['pet']
NameError: name 'ic' is not defined. Did you mean: 'c'?
d
dic['name']
'TaeHwan'
dic['pet']
'dog'
dic.keys()
dict_keys(['name', 'phone', 'birth', 'pet'])
list(dic.keys())
['name', 'phone', 'birth', 'pet']
dic.values()
dict_values(['TaeHwan', '01012345678', '0109', 'dog'])
list(dic.values())
['TaeHwan', '01012345678', '0109', 'dog']
dic.items()
dict_items([('name', 'TaeHwan'), ('phone', '01012345678'), ('birth', '0109'), ('pet', 'dog')])
list(dic.items())
[('name', 'TaeHwan'), ('phone', '01012345678'), ('birth', '0109'), ('pet', 'dog')]
dic.clear()
dic
{}
s1={1,2,'a',5}
s2=set([1,2,3,4,5,6])
s2
{1, 2, 3, 4, 5, 6}
s
s3=set([4,5,6,7,8,9])
s3
3
s3
{4, 5, 6, 7, 8, 9}
s2 & s3
{4, 5, 6}
s2.intersection(s3)
{4, 5, 6}
s2 | s3
{1, 2, 3, 4, 5, 6, 7, 8, 9}
s2.union(s3)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
s2 - s3
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    2 - s3
TypeError: unsupported operand type(s) for -: 'int' and 'set'
s
s2 - s3
{1, 2, 3}
s2.difference(s3)
{1, 2, 3}
s3.difference(s2)
{8, 9, 7}
s2.add(7)
s2
{1, 2, 3, 4, 5, 6, 7}
s2.update([1,2,4,5,6,7,8,9,10])
s2
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2.remove(1,2,7)
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    s2.remove(1,2,7)
sTypeError: set.remove() takes exactly one argument (3 given)
2
s2.remove([1,2,7])
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    s2.remove([1,2,7])
TypeError: unhashable type: 'list'
s2.remove(1)
s2
{2, 3, 4, 5, 6, 7, 8, 9, 10}
dic
{}
dic = {'name':'TaeHwan', 'CS':2017301023}
dic
{'name': 'TaeHwan', 'CS': 2017301023}
dic[0]
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    dic[0]
KeyError: 0
dic['name']
'TaeHwan'
x=3
y=2
x == y
False
x != y
True
x >= y
True
money = 1300
if money >= 1200 and money < 3500:
    print("Can take the bus")

    
Can take the bus
1 in [1,2,3]
True
x in [1,2,3]
True
x not in [1,2,3]
False
'a' in ['a','b','c','d']
True
'i' not in 'python'
True
if money < 10:
    pass
else:
    print("저금하자!")

    
저금하자!
test list = ['one','two','three']
SyntaxError: invalid syntax
test list = ['one','two','three']
SyntaxError: invalid syntax
test_list = ['one','two','three']
for i in test_list:
    x = i + '!'
    print(x)

    
one!
two!
three!
number = 0
for score in [90,25,67,45,93]
SyntaxError: expected ':'
for score in [90,25,67,45,93]:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." %number)
        else:
            
SyntaxError: invalid syntax
for score in [90,25,67,45,93]:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 합격입니다." %number)

        
1번 학생은 합격입니다.
2번 학생은 합격입니다.
3번 학생은 합격입니다.
4번 학생은 합격입니다.
5번 학생은 합격입니다.
number
5
number = 0
for score in [90,25,67,45,93]:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 합격입니다." %number)

        
1번 학생은 합격입니다.
2번 학생은 합격입니다.
3번 학생은 합격입니다.
4번 학생은 합격입니다.
5번 학생은 합격입니다.
number = 0
for score in [90,25,67,45,93]:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)
        
SyntaxError: multiple statements found while compiling a single statement
number = 0;
for score in [90,25,67,45,93]:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

        
1번 학생은 합격입니다.
2번 학생은 불합격입니다.
3번 학생은 합격입니다.
4번 학생은 불합격입니다.
5번 학생은 합격입니다.
def sum1(a,b):
    x = a + b
    return x
def sum2(*args):
    
SyntaxError: invalid syntax
def sum2(*args):
    x = 0
    for i in args:
        x += i
    return x

a=5
b=3
sum1(a,b)
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    sum1(a,b)
NameError: name 'sum1' is not defined. Did you mean: 'sum2'?
s
def sum1(a,b):
    return a+b

sum1(a,b)
8
sum1(3,5)
8
sum2(1,2,3,4,5)
15
sum2(2,3.5,10)
15.5
i = 0
while i < 5:
    i++
    
SyntaxError: invalid syntax
while i < 5:
    i += 1
    print('*' * i)

    
*
**
***
****
*****
abs(-3.5)
3.5
all([1,2,3,4])
True
all([4,-2,0.0,4])
False
all([4,-2,4])
True
any([1,2,3,4])
True
any([4,-2,0.0,4])
True
chr(97)
'a'
chr(48)
'0'
ord('a')
97
ord('0')
48
dir([1,2,3])
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
dir({'1':'a'})
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
dir(1)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
divmod(7,3)
(2, 1)
divmod(1.3,0,2)
Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    divmod(1.3,0,2)
TypeError: divmod expected 2 arguments, got 3
divmod(1.3,0.2)
(6.0, 0.09999999999999998)
oct(8)
'0o10'
oct9234)
SyntaxError: unmatched ')'
hex(16)
'0x10'
hex(234)
'0xea'
oct(234)
'0o352'
a=3
id(a)
4307124528
id(dic)
4355530112
a
3
dic
{'name': 'TaeHwan', 'CS': 2017301023}
id(dic)
4355530112
id(a)
4307124528
int('3')
3
str(3)
'3'
list('python')
['p', 'y', 't', 'h', 'o', 'n']
list((1,2,3))
[1, 2, 3]
tuple('python')
('p', 'y', 't', 'h', 'o', 'n')
tuple([1,2,3])
(1, 2, 3)
type('abc')
<class 'str'>
type(a)
<class 'int'>
sum=lambda a,b: a + b
sum
<function <lambda> at 0x1039f7640>
sum(3,5)
8
max([1,4,2,8,6])
8
max("Python")
'y'
min([1,4,2,8,6])
1
min("Python")
'P'
pow(2,4)
16
c=input()
21
c
'21'
c=input("INPUT INTEGER")
INPUT INTEGER29
c
'29'
range(5)
range(0, 5)
list(range(5))
[0, 1, 2, 3, 4]
list(range(5,10))
[5, 6, 7, 8, 9]
list(range(5,10,2))
[5, 7, 9]
len("Python")
6
sorted([2,0,3,1])
[0, 1, 2, 3]
sorted("Python")
['P', 'h', 'n', 'o', 't', 'y']
Request('http://hanb.co.kr')
Traceback (most recent call last):
  File "<pyshell#308>", line 1, in <module>
    Request('http://hanb.co.kr')
NameError: name 'Request' is not defined
import urllib.request
urllib.request.Request('http://hanb.co.kr')
<urllib.request.Request object at 0x103986320>
pandas.DataFrame()
Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    pandas.DataFrame()
NameError: name 'pandas' is not defined
import pandas
Traceback (most recent call last):
  File "<pyshell#312>", line 1, in <module>
    import pandas
ModuleNotFoundError: No module named 'pandas'
import pandas
Traceback (most recent call last):
  File "<pyshell#313>", line 1, in <module>
    import pandas
ModuleNotFoundError: No module named 'pandas'
import pandas
Traceback (most recent call last):
  File "<pyshell#314>", line 1, in <module>
    import pandas
ModuleNotFoundError: No module named 'pandas'
import panda
Traceback (most recent call last):
  File "<pyshell#315>", line 1, in <module>
    import panda
ModuleNotFoundError: No module named 'panda'
import pandas
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    import pandas
ModuleNotFoundError: No module named 'pandas'
from datetime import datetime
datetime.now()
datetime.datetime(2022, 9, 15, 12, 23, 22, 885544)
import pandas as pd
Traceback (most recent call last):
  File "<pyshell#319>", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
install pandas
SyntaxError: invalid syntax
conda
Traceback (most recent call last):
  File "<pyshell#321>", line 1, in <module>
    conda
NameError: name 'conda' is not defined
conda install pandas
SyntaxError: invalid syntax
f = open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", mode='w')
f
<_io.TextIOWrapper name='/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt' mode='w' encoding='UTF-8'>
f.close()
f
<_io.TextIOWrapper name='/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt' mode='w' encoding='UTF-8'>
for i in range(1,6):
    data="%d번째 줄입니다.\n"%i
    f.write(data)

    
Traceback (most recent call last):
  File "<pyshell#330>", line 3, in <module>
    f.write(data)
ValueError: I/O operation on closed file.
f = open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", mode='w')
for i in range(1,6):
    data="%d번째 줄입니다.\n"%i
    f.write(data)

    
10
10
10
10
10
i
5
for j in range(1,6):
    data="%d번째 줄입니다. \n"%j
    f.write(data)

    
11
11
11
11
11
data
'5번째 줄입니다. \n'
j
5
f
<_io.TextIOWrapper name='/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt' mode='w' encoding='UTF-8'>
f.close()
f = open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", mode='w')
for j in range(6,11):
    data="%d번째 줄입니다. \n"%j
    f.write(data)

    
11
11
11
11
12
f.close()
f = open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", mode='w')
for i in range(1,6):
    data="%d번째 줄입니다.\n"%i
    f.write(data)

    
10
10
10
10
10
f.close()
f = open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", 'a')
for i in range(6,11):
    data="%d번째 줄입니다.\n"%i
    
    f.write(data)

    
10
10
10
10
11
f.close()
f = open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", 'a')
f.close()
f = open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", 'r')
line = f.readline()
print(line)
1번째 줄입니다.

while True:
    line = f.readline()
    if not line: break
    print(line)

    
2번째 줄입니다.

3번째 줄입니다.

4번째 줄입니다.

5번째 줄입니다.

6번째 줄입니다.

7번째 줄입니다.

8번째 줄입니다.

9번째 줄입니다.

10번째 줄입니다.

f.close()
f = open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", 'r')
lines=f.readlines()
print(lines)
['1번째 줄입니다.\n', '2번째 줄입니다.\n', '3번째 줄입니다.\n', '4번째 줄입니다.\n', '5번째 줄입니다.\n', '6번째 줄입니다.\n', '7번째 줄입니다.\n', '8번째 줄입니다.\n', '9번째 줄입니다.\n', '10번째 줄입니다.\n']
for line in lines:
    print(line)

    
1번째 줄입니다.

2번째 줄입니다.

3번째 줄입니다.

4번째 줄입니다.

5번째 줄입니다.

6번째 줄입니다.

7번째 줄입니다.

8번째 줄입니다.

9번째 줄입니다.

10번째 줄입니다.

f = open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", 'r')
data=f.read()
data
'1번째 줄입니다.\n2번째 줄입니다.\n3번째 줄입니다.\n4번째 줄입니다.\n5번째 줄입니다.\n6번째 줄입니다.\n7번째 줄입니다.\n8번째 줄입니다.\n9번째 줄입니다.\n10번째 줄입니다.\n'
f.close()
with.open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", 'w') as f:
    
SyntaxError: invalid syntax
with open("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/newText.txt", 'w') as f:
    f.write("Now is better than never.")

    
25
data=f.read()
Traceback (most recent call last):
  File "<pyshell#378>", line 1, in <module>
    data=f.read()
ValueError: I/O operation on closed file.
pip install numpy
SyntaxError: invalid syntax
python3 --version
Traceback (most recent call last):
  File "<pyshell#380>", line 1, in <module>
    python3 --version
NameError: name 'python3' is not defined
import numpy as np
np__versoin
Traceback (most recent call last):
  File "<pyshell#382>", line 1, in <module>
    np__versoin
NameError: name 'np__versoin' is not defined
np__version__
Traceback (most recent call last):
  File "<pyshell#383>", line 1, in <module>
    np__version__
NameError: name 'np__version__' is not defined
np --version
Traceback (most recent call last):
  File "<pyshell#384>", line 1, in <module>
    np --version
NameError: name 'version' is not defined
import pandas
pands
pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []
np.__version__
'1.23.3'
ar1=np.array([1,2,3,4,5])
ar1
array([1, 2, 3, 4, 5])
type(ar1)
<class 'numpy.ndarray'>
ar2=np.array([[10,20,30],[40,50,60]])
ar2
array([[10, 20, 30],
       [40, 50, 60]])
ar3=np.array(1,11,2)
Traceback (most recent call last):
  File "<pyshell#393>", line 1, in <module>
    ar3=np.array(1,11,2)
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
ar3=np.array(1,11,2)
Traceback (most recent call last):
  File "<pyshell#394>", line 1, in <module>
    ar3=np.array(1,11,2)
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
ar3 = np.arange(1,11,2)
ar3
array([1, 3, 5, 7, 9])
ar4 = np.array([1,2,3,4,5,6]).reshape((3,2))
ar4
array([[1, 2],
       [3, 4],
       [5, 6]])
ar6 = ar2[0:2, 0:2]
ar6
array([[10, 20],
       [40, 50]])
ar7 = ar2[0,:]
ar7
array([10, 20, 30])
ar8=ar1+10
ar8
array([11, 12, 13, 14, 15])
ar1+ar8
array([12, 14, 16, 18, 20])
ar8-ar1
array([10, 10, 10, 10, 10])
ar*2
Traceback (most recent call last):
  File "<pyshell#407>", line 1, in <module>
    ar*2
NameError: name 'ar' is not defined. Did you mean: 'a'?
ar1*2
array([ 2,  4,  6,  8, 10])
ar1/2
array([0.5, 1. , 1.5, 2. , 2.5])
ar9=np.dot(ar2,ar4)
ar9
array([[220, 280],
       [490, 640]])
pd.__version__
Traceback (most recent call last):
  File "<pyshell#412>", line 1, in <module>
    pd.__version__
NameError: name 'pd' is not defined. Did you mean: 'd'?
import pandas as pd
pd.__version__
'1.4.4'
data1=[10,20,30,40,50]
data1
[10, 20, 30, 40, 50]
data2=['1반','2반','3반','4반','5반']
data2
['1반', '2반', '3반', '4반', '5반']
sr1=pd.Series(data1)
sr1
0    10
1    20
2    30
3    40
4    50
dtype: int64
sr2=pd.Series(data2)
dsr2
0    1반
1    2반
2    3반
3    4반
4    5반
dtype: object
sr2
0    1반
1    2반
2    3반
3    4반
4    5반
dtype: object
sr3=pd.Series([101,102,103,104,105])
sr3
0    101
1    102
2    103
3    104
4    105
dtype: int64
sr4=pd.Series(['mon','tue','wed','thu','fri'])
sr4
0    mon
1    tue
2    wed
3    thu
4    fri
dtype: object
sr5=pd.Series(data1, index=[1000,1001,1002,1003,1004])
sr5
1000    10
1001    20
1002    30
1003    40
1004    50
dtype: int64
sr6=pd.Series(data,index=data2)
sr6
1반    1번째 줄입니다.\n2번째 줄입니다.\n3번째 줄입니다.\n4번째 줄입니다.\n5번...
2반    1번째 줄입니다.\n2번째 줄입니다.\n3번째 줄입니다.\n4번째 줄입니다.\n5번...
3반    1번째 줄입니다.\n2번째 줄입니다.\n3번째 줄입니다.\n4번째 줄입니다.\n5번...
4반    1번째 줄입니다.\n2번째 줄입니다.\n3번째 줄입니다.\n4번째 줄입니다.\n5번...
5반    1번째 줄입니다.\n2번째 줄입니다.\n3번째 줄입니다.\n4번째 줄입니다.\n5번...
dtype: object
data2
['1반', '2반', '3반', '4반', '5반']
sr6=pd.Series(data1,index=data2)
sr6
1반    10
2반    20
3반    30
4반    40
5반    50
dtype: int64
sr8
Traceback (most recent call last):
  File "<pyshell#435>", line 1, in <module>
    sr8
NameError: name 'sr8' is not defined. Did you mean: 'ar8'?
sr8[2]
Traceback (most recent call last):
  File "<pyshell#436>", line 1, in <module>
    sr8[2]
NameError: name 'sr8' is not defined. Did you mean: 'ar8'?
sr6[2]
30
sr8['wed']
Traceback (most recent call last):
  File "<pyshell#438>", line 1, in <module>
    sr8['wed']
NameError: name 'sr8' is not defined. Did you mean: 'ar8'?
sr6[-1]
50
sr6['3반']
30
sr6[0:4]
1반    10
2반    20
3반    30
4반    40
dtype: int64
sr6.index
Index(['1반', '2반', '3반', '4반', '5반'], dtype='object')
sr6.values
array([10, 20, 30, 40, 50])
sr1+sr3
0    111
1    122
2    133
3    144
4    155
dtype: int64
sr4+sr2
0    mon1반
1    tue2반
2    wed3반
3    thu4반
4    fri5반
dtype: object
data_dic{
    
SyntaxError: '{' was never closed
data_dic={
    'year':[2018,2019,2020],
    'sales':[350,480,1099],
    }
data_dic
{'year': [2018, 2019, 2020], 'sales': [350, 480, 1099]}
df1=pd.DataFrame(data_dic)
df1
   year  sales
0  2018    350
1  2019    480
2  2020   1099
df2=pd.DataFrame([[89.2,92.5,90.8],[92.8,89.9,95.2]],index=['중간고사', '기말고사'],columns=data[0:3])
Traceback (most recent call last):
  File "<pyshell#454>", line 1, in <module>
    df2=pd.DataFrame([[89.2,92.5,90.8],[92.8,89.9,95.2]],index=['중간고사', '기말고사'],columns=data[0:3])
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pandas/core/frame.py", line 720, in __init__
    columns = ensure_index(columns)  # type: ignore[arg-type]
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pandas/core/indexes/base.py", line 7060, in ensure_index
    return Index._with_infer(index_like, copy=copy)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pandas/core/indexes/base.py", line 680, in _with_infer
    result = cls(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pandas/core/indexes/base.py", line 508, in __new__
    raise cls._scalar_data_error(data)
TypeError: Index(...) must be called with a collection of some kind, '1번째' was passed
df2=pd.DataFrame([[89.2,92.5,90.8],[92.8,89.9,95.2]],index=['중간고사', '기말고사'],columns=data2[0:3])
df2
        1반    2반    3반
중간고사  89.2  92.5  90.8
기말고사  92.8  89.9  95.2
data_df=[['2017301023','TaeHwan','90','95'],['2017301024','TaeHwan2','93','94'],['2017301025','TaeHwan3','87','97']]
df3=pd.DataFrame(data_df)
df3
            0         1   2   3
0  2017301023   TaeHwan  90  95
1  2017301024  TaeHwan2  93  94
2  2017301025  TaeHwan3  87  97
df3.columns=['학번','이름','중간고사','기말고사']
df3
           학번        이름 중간고사 기말고사
0  2017301023   TaeHwan   90   95
1  2017301024  TaeHwan2   93   94
2  2017301025  TaeHwan3   87   97
df3.head(2)
           학번        이름 중간고사 기말고사
0  2017301023   TaeHwan   90   95
1  2017301024  TaeHwan2   93   94
d
df3.tail(2)
           학번        이름 중간고사 기말고사
1  2017301024  TaeHwan2   93   94
2  2017301025  TaeHwan3   87   97
df3.tail(1)
           학번        이름 중간고사 기말고사
2  2017301025  TaeHwan3   87   97
df3('이름')
Traceback (most recent call last):
  File "<pyshell#465>", line 1, in <module>
    df3('이름')
TypeError: 'DataFrame' object is not callable
df3['이름']
0     TaeHwan
1    TaeHwan2
2    TaeHwan3
Name: 이름, dtype: object
df3.to_csv("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/score.csv",header='False')
df4=pd.read_csv("/Users/taehwankim/Desktop/무제 폴더/4학년 2학기/DataCrawling/score.csv",encoding='utf-8',index_col=0,engine='python')
df4
           학번        이름  중간고사  기말고사
0  2017301023   TaeHwan    90    95
1  2017301024  TaeHwan2    93    94
2  2017301025  TaeHwan3    87    97
import matplotlib as plt
plt.__version__
'3.5.3'
import matplotlib.pyplot as plt
x=[2016,2017,2018,2019,2020]
y=[350,410,520,695,543]
plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x160c19360>]
p
plt.title('Annual sales')
Text(0.5, 1.0, 'Annual sales')
plt.xlabel('years')
Text(0.5, 0, 'years')
plt.ylabel('sales')
Text(0, 0.5, 'sales')
plt.show()
plt.close()
return 0;
close
y1=[350,410,520,695]
y2=[200,250,385,350]
x = range(len(y1))
plt.bar(x,y1,width=0.7,color='blue')
<BarContainer object of 4 artists>
plt.bar(x,y2,width=0.7,color='red')
<BarContainer object of 4 artists>
plt.title('Quarterly sales')
Text(0.5, 1.0, 'Quarterly sales')
plt.xlabel('Quarters')
Text(0.5, 0, 'Quarters')
plt.ylabel('sales')
Text(0, 0.5, 'sales')
plt.show()
plt.show()
plt.show()
plt.close()
xlabel=['first','second','third','fourth']
plt.xticks(x,xLabel,fontsize=10)
Traceback (most recent call last):
  File "<pyshell#493>", line 1, in <module>
    plt.xticks(x,xLabel,fontsize=10)
NameError: name 'xLabel' is not defined. Did you mean: 'xlabel'?
plt.xticks(x,xlabel,fontsize=10)
([<matplotlib.axis.XTick object at 0x163548460>, <matplotlib.axis.XTick object at 0x163548430>, <matplotlib.axis.XTick object at 0x163525270>, <matplotlib.axis.XTick object at 0x16356cc40>], [Text(0, 0, 'first'), Text(1, 0, 'second'), Text(2, 0, 'third'), Text(3, 0, 'fourth')])
plt.legend(['chairs','desks'])
<matplotlib.legend.Legend object at 0x16356d810>
plt.show()

======================================== RESTART: Shell =======================================
>>> plt.show()
Traceback (most recent call last):
  File "<pyshell#497>", line 1, in <module>
    plt.show()
NameError: name 'plt' is not defined
>>> y1=[350,410,520,695]
... y2=[200,250,385,350]
SyntaxError: multiple statements found while compiling a single statement
>>> y1=[350,410,520,695]
>>> y2=[200,250,385,350]
>>> x = range(len(y1))
>>> plt.bar(x,y1,width=0.7,color='blue')
Traceback (most recent call last):
  File "<pyshell#502>", line 1, in <module>
    plt.bar(x,y1,width=0.7,color='blue')
NameError: name 'plt' is not defined
>>> import metplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#503>", line 1, in <module>
    import metplotlib.pyplot as plt
ModuleNotFoundError: No module named 'metplotlib'
>>> import matplotlib.pyplot as plt
>>> plt.show()
>>> import matplotlib.pyplot as plt
>>> y1=[350,410,520,695];
... y2=[200,250,385,350];
... x = range(len(y1));
... plt.bar(x,y1,width=0.7,color='blue');
SyntaxError: multiple statements found while compiling a single statement
>>> y1=[350,410,520,695]
>>> y2=[200,250,385,350]
>>> x = range(len(y1))
>>> plt.bar(x,y1,width=0.7,color='blue')
<BarContainer object of 4 artists>
>>> plt.bar(x,y2,width=0.7,color='red')
<BarContainer object of 4 artists>
>>> plt.title('Quarterly sales')
Text(0.5, 1.0, 'Quarterly sales')
>>> plt.xlabel('Quarters')
Text(0.5, 0, 'Quarters')
>>> plt.ylabel('sales')
Text(0, 0.5, 'sales')
>>> xlabel=['first','second','third','fourth']
>>> plt.xticks(x,xlabel,fontsize=10)
([<matplotlib.axis.XTick object at 0x1221f3c10>, <matplotlib.axis.XTick object at 0x1221f3be0>, <matplotlib.axis.XTick object at 0x1221f2890>, <matplotlib.axis.XTick object at 0x122271450>], [Text(0, 0, 'first'), Text(1, 0, 'second'), Text(2, 0, 'third'), Text(3, 0, 'fourth')])
>>> plt.legend(['chairs','desks'])
<matplotlib.legend.Legend object at 0x122271e70>
>>> plt.show()
>>> print("Today is 2022.09.15 Thursday")
Today is 2022.09.15 Thursday
