#! encoding:utf-8
from flask import Flask
from flask import request,jsonify,abort
from db import con_db
from db_test import query
from db_test import insert
import json
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="POST">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign</button></p>
              <form>'''

@app.route('/signin',methods=['POST'])

#def signin():
#    username = request.form['username']
#    password = request.form['password']
#    insert(username,password)
    
#    return '{"code":"000000"}'

def signin():
    da = request.get_json(force=True)
    data = json.loads(da)
    username = data["username"]
    password = data["password"]
                                
    #user = username['username']
    
    '''
    json_to_data = json.loads(data)
    username = json_to_data['username']
    password = json_to_data['password']
    #username = username[0]
    #password = password[1] '''
    try:
        insert(username,password)
        return '{"code":"000000"}'
    except:
        return '{"code":"999999"}'
    '''
    if uname == "" and pawd == "":
        return '<h3>Bad username or password.</h3>'
    else:
        return 00000
    '''
if __name__=='__main__':
    app.run(
     host = '0.0.0.0',
     port = 8888,
     debug = True  
)
