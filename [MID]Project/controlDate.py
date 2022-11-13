from datetime import datetime

def getDate(year, month, day = 0):
    #연월일을 문자열로 변환
    date = str(year)
    if month < 10:
        date += '0' + str(month)
    elif month >= 10:
        date += str(month)
    if day < 10:
        if day == 0:
            return date
        date += '0' + str(day)
    elif day >= 10:
        date += str(day)
        
    return date

def getTime(time):
    #시간을 문자열로 변환
    if time < 10:
        return '0' + str(time)
    return str(time)

def isToday(year, month, day):
    if year == datetime.today().year and month == datetime.today().month and day == datetime.today().day:
        return True
