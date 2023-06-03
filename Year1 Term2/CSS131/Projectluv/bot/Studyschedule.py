from parinya import LINE
import requests
import cv2
import time
import datetime


LINE_NOTIFY_API_URL = "https://notify-api.line.me/api/notify"
line = LINE('hoqVc61wZRZcPAHUyI7Bxjbr2rKo8Rwr0mEXag70Uz0')
baseURLWork = requests.get('http://localhost:3000/homewrk')
baseURLWork = baseURLWork.json()
baseURLClass = requests.get('http://localhost:3000/classschedule')
baseURLClass = baseURLClass.json()
example = requests.get('https://jsonplaceholder.typicode.com/users')
daatenow = datetime.datetime.now()
datevalue = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def sendtextClassOnsite():
    for i in baseURLClass :
        if i['classsite'] == 'Online' :
            continue
        massage ='\n'+ 'วันพรุ่งนี้คุณเรียน'+i['classsite']+ '\n' +'วิชา' + i['namesubject'] +'\n' +' ในเวลา ' + str(i['time']) + ':' + str(i['mintime']) + ' น.ครับ'
        line.sendtext(massage)

def sendtextClassOnline() :
    for i in baseURLClass :
        if i['classsite'] == 'Onsite' :
            continue
        massage ='\n'+ 'วันนี้คุณเรียน'+i['classsite']+ '\n' +'วิชา' + i['namesubject'] +'\n' +' ในเวลา ' + str(i['time']) + ':' + str(i['mintime']) + ' นาฬิกาครับ'
        line.sendtext(massage)   


# for i in baseURLClass :
#     if i['day'] == None :
#         continue
#     result = (datevalue.index(i['day']))
#     # print("datevalue",((daatenow.weekday()+1)%7))
#     # print("result",result)
#     if result == ((daatenow.weekday()+1)%7) and i['classsite'] == 'Onsite' :

#         sendtextClassOnsite()
#     elif  i['day'] == daatenow.strftime('%A') and i['classsite'] == 'Online' :
#         line.sendsticker('11537','52002734')
#         sendtextClassOnline()


# for i in baseURLWork.json() :
#     if i['day'] == daatenow.day+1 :
#         massage = '\n' + 'วันพรุ่งนี้คุณมีการบ้านวิชา'+i['namework'] + 'ที่ต้องส่ง' + '\n' + 'เวลา' + str(i['hour']) + ':' + str(i['minute']) + 'นาฬิกานะคะ'
#         line.sendtext(massage)



# line.sendtext(daatenow.datetime.now().strftime('%H'))

while  True :
    if "07" == daatenow.now().strftime('%H') :
        for i in baseURLClass :
            if i['day'] == None :
                continue
            result = (datevalue.index(i['day']))
        # print("datevalue",((daatenow.weekday()+1)%7))
        # print("result",result)
            if result == ((daatenow.weekday()+1)%7) and i['classsite'] == 'Onsite' :
                sendtextClassOnsite()
                sleep(3600)
            elif  i['day'] == daatenow.strftime('%A') and i['classsite'] == 'Online' :
                line.sendsticker('11537','52002734')
                sendtextClassOnline()
                sleep(3600)
    elif "11" == daatenow.now().strftime('%H') :
        for i in baseURLWork :
            if i['day'] == daatenow.day+1 :
                massage = '\n' + 'วันพรุ่งนี้คุณมีการบ้านวิชา'+i['namework'] + 'ที่ต้องส่ง' + '\n' + 'เวลา' + str(i['hour']) + ':' + str(i['minute']) + 'นาฬิกานะคะ'
                line.sendtext(massage)
                sleep(3600)
