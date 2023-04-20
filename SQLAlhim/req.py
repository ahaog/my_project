import requests
from bs4 import BeautifulSoup
from datetime import datetime

Id = 'u3819187, u3818294, u3797240, u3947058, u3945228, u3818296, u3802266, u3820637, u3797370, u3980683, u3945730, u3869222'
id = Id.split(', ')
testData = []
for i in id:
    for lang in ['en', 'ru']:
        link = 'https://www.ratatype.com/ru/'+i +'/certification-results/'+lang +'/'
        response = requests.get(link).text

        with open('1.html', 'w', encoding='utf8') as file:
            file.write(response)

        file = open('1.html', encoding="utf8")
        soup = BeautifulSoup(file, 'lxml')

        scr = []

        b = soup.find_all(class_='darkGrey')
        for item in b:
            sp = item.get_text('darkGrey')
            scr.append(sp)

        scr1 = []

        b1 = soup.find_all(class_='accuracyOView')
        for item in b1:
            acc = item.get_text('accuracyOView')
            scr1.append(acc)

        scr2 = []

        div = soup.find_all(class_='dateOView nowrap')
        for item in div:
            date = item.get_text('dateOView nowrap')
            scr2.append(date)

        scr3 =[]

        div1 = soup.find_all(class_='timeOView')
        for item in div1:
            time = item.get_text('timeOView')
            scr3.append(time)

        for a in range(len(scr)):
            testData.append([i, scr[a], scr1[a], scr2[a], scr3[a], lang])
print('[')
for i in testData:
    print(i, ', ')
print(']')






