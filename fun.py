from datetime import datetime
import pytz

search_ex = {"CR_ID":0, 'building':'研揚大樓','roomName':'TR313','capacity':20,
'status':{1:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}}

search_ex2 = {"CR_ID":1, 'building':'研揚大樓','roomName':'TR414','capacity':30,
'status':{5:(1,'開會','Jerry'), 14:(0, '椅子壞掉', 'admin')}}

search_result = [search_ex, search_ex2]

record_ex = {'recordID':'123', 'title':'上課','startDate':'2021-01-30', 'startSection':1, 'endDate':'2021-01-30', 'endSection':10,
'roomName':'TR313', 'building':'研揚大樓(TR)', 'participant':['茶是一種蔬菜湯','茶葉蛋',
'神棍局局長']}

record_ex2 = {'recordID':'456', 'title':'創業', 'startDate':'2021-02-01', 'startSection':1, 'endDate':'2021-01-31', 'endSection':10,
'roomName':'TR411', 'building':'研揚大樓(TR)', 'participant':[]}

records = [record_ex, record_ex2]

user_ex1={"userID":0,"userName":"wacky","nickName":"OwO","password":"hahaha","email":"chenghan0516@gmail.com","identity":0,"banned":False}
user_ex2={"userID":0,"userName":"hello","nickName":"OwO","password":"hahaha","email":"chenghan0516@gmail.com","identity":0,"banned":True}


search_single1 = {1:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}
search_single2 = {3:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}
search_single3 = {3:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}
search_single4 = {3:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}
search_single5 = {3:(1,'電機系上課','咕你媽逼'), 10:(0, '故障', 'admin')}
search_single6 = {9:(1,'電機系上課','你好'), 10:(0, '投影機故障', 'admin')}
search_single7 = {3:(1,'電機系上課','WackilySmiley'), 10:(0, '投影機故障', 'admin')}

search_single_ex = {'CR_ID':1,'building':'研揚大樓','roomName':'TR313','capacity':20, 'status':[search_single1,search_single2,
search_single3,search_single4,search_single5,search_single6,search_single7]}

def get_search_result(data):
    return search_result

def get_single_result(CR_ID, start_date):
    return search_single_ex

def get_current_time():
    taipei = pytz.timezone('Asia/Taipei')
    return datetime.strftime(datetime.now(taipei), "%Y-%m-%d")









def modify_record(data):
    recordID = data['recordID']
    participants = []
    for i in range(int(data['counter'])):
        p = data.get('participant' + str(i))
        if  p != None and p != '':
            participants.append(data['participant' + str(i)])
    print(participants)
    participants = ",".join(participants)
    print(participants)

    return True

def delete_record(data):
    print(data)
    recordID = data['recordID']
    print("delete", recordID)


