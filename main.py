from flask import Flask , render_template
from flask import request, url_for, flash, redirect, make_response

from fun import *

app = Flask(__name__)

buildings=['研揚大樓(TR)','第四教學大樓(T4)','綜合研究大樓(RB)','國際大樓(IB)','電資館(EE)']

record_ex = {'recordID':'123', 'title':'上課','startDate':'2021-01-30', 'startSection':1, 'endDate':'2021-01-30', 'endSection':10,
'roomName':'TR313', 'building':'研揚大樓(TR)', 'participant':['茶是一種蔬菜湯','茶葉蛋',
'神棍局局長']}

record_ex2 = {'recordID':'456', 'title':'創業', 'startDate':'2021-02-01', 'startSection':1, 'endDate':'2021-01-31', 'endSection':10,
'roomName':'TR411', 'building':'研揚大樓(TR)', 'participant':['勞工',
'CEO','CTO','PM']}

records = [record_ex, record_ex2]

search_ex = {'building':'研揚大樓','roomName':'TR313','capacity':20,
'status':{1:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}}

search_ex2 = {'building':'研揚大樓','roomName':'TR414','capacity':30,
'status':{5:(1,'開會','Jerry'), 14:(0, '椅子壞掉', 'admin')}}

search_result = [search_ex, search_ex2]

user_ex1={"userID":0,"userName":"wacky","nickName":"OwO","password":"hahaha","email":"chenghan0516@gmail.com","identity":0,"banned":0}


classroom_ex ={"CR_ID":0,"building":buildings[0],"roomname":"TR-313","capacity":20}

search_single_ex1 = {'building':'研揚大樓','roomName':'TR313','capacity':20,
'status':{1:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}}
search_single_ex2 = {'building':'研揚大樓','roomName':'TR313','capacity':20,
'status':{3:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}}
search_single_ex3 = {'building':'研揚大樓','roomName':'TR313','capacity':20,
'status':{14:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}}
search_single_ex4 = {'building':'研揚大樓','roomName':'TR313','capacity':20,
'status':{1:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}}
search_single_ex5 = {'building':'研揚大樓','roomName':'TR313','capacity':20,
'status':{2:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}}
search_single_ex6 = {'building':'研揚大樓','roomName':'TR313','capacity':20,
'status':{8:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}}
search_single_ex7 = {'building':'研揚大樓','roomName':'TR313','capacity':20,
'status':{11:(1,'電機系上課','咕你媽逼'), 10:(0, '投影機故障', 'admin')}}
search_single_exs = [search_single_ex1,search_single_ex2,search_single_ex3,search_single_ex4,search_single_ex5,search_single_ex6,search_single_ex7]

def cookie_check():
    """
    check cookie's correctness
    """
    email = request.cookies.get("email")
    password = request.cookies.get('password')
    return authentication(email, password)

@app.route('/logout')
def logout():
    res = make_response(redirect(url_for("login_page")))
    res.set_cookie(key='email', value='', expires=0)
    res.set_cookie(key='password', value='', expires=0)
    return res

@app.route('/register',methods=['POST','GET'])
def register_page():
    if cookie_check()[0]:
        return redirect(url_for('main_page'))

    if request.method == 'POST':
        if register(request.form):
            #註冊成功
            return redirect(url_for('login_page'))
        else:
            #註冊失敗
            return render_template("register.html")
    return render_template("register.html")

@app.route('/login',methods=['POST','GET'])
def login_page(): 
    if cookie_check()[0]:
        return redirect(url_for('main_page'))
    return render_template("login.html")

@app.route('/search',methods=['POST','GET'])
def search_page():
    check = cookie_check()
    if not check[0]:
        return redirect(url_for('login_page'))
    if request.method =='POST':
        return render_template("search.html", buildings=buildings, date=request.form['date'], result=search_result, admin = check[1])
    return render_template("search.html", buildings=buildings, date=get_current_time(), result=None, admin = check[1])
    
@app.route('/borrow',methods=['POST','GET'])
def borrow_page():
    check = cookie_check()
    if not check[0]:
        return redirect(url_for('login_page'))
    return render_template("borrow.html", buildings=buildings, admin=check[1])

@app.route('/record',methods=['POST','GET'])
def record_page():
    check = cookie_check()
    if not check[0]:
        return redirect(url_for('login_page'))
    
    return render_template("record.html", records=records, admin = check[1])

@app.route('/single_record',methods=['POST'])
def single_record_page():
    check = cookie_check()
    if not check[0]:
        return redirect(url_for('login_page'))
    if request.method =='POST':
        if request.form['postType'] == 'get':
            print('get')
            return render_template("single_record.html",record=get_record(request.form['id']), admin = check[1])
        elif request.form['postType'] == 'modify':
            modify_record(request.form)
            return redirect(url_for('record_page'))
        elif request.form['postType'] == 'delete':
            delete_record(request.form)
            return redirect(url_for('record_page'))
    return redirect(url_for('main_page'))

@app.route('/', methods=['POST', 'GET'])
def main_page():
    check = cookie_check()
    #if cookie exists and user information is correct, then enter main page 
    if check[0]:
        return render_template("main.html", user_name = request.cookies.get('email'), admin=check[1])
    if request.method =='POST':
        #TODO encryption
        check = authentication(request.form['email'], request.form['password'])
        if check[0]:
            resp = make_response(render_template("main.html", admin=check[1]))
            #set cookie
            resp.set_cookie('email', request.form['email']) #TODO set age
            resp.set_cookie('password', request.form['password']) #TODO set age
            
            return resp
        #login fail
        else:
            return redirect(url_for('login_page'))
    
    return redirect(url_for('login_page'))

@app.route('/account_management', methods=['POST', 'GET'])
def account_management_page():
    #if cookie exists and user information is correct, then enter main page 
    check = cookie_check()
    if check[0] and check[1] == "admin":
        return render_template("account_management.html", user = user_ex1, admin=check[1])
    else:
        return redirect(url_for('login_page'))
      
@app.route('/search_single',methods=['POST','GET'])
def search_single_page():
    check = cookie_check()
    if not check[0]:
        return redirect(url_for('login_page'))
    if request.method =='POST':
        return render_template("search_single.html",classroom = classroom_ex,records = search_single_exs, start_search_date = datetime(2020, 5, 17), admin = check[1])
    return render_template("search_single.html",classroom=classroom_ex,records = search_single_exs, start_search_date = datetime(2020, 5, 17), admin = check[1])

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "test Key"
    app.run()