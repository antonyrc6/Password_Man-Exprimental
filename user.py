import sqlite3
from flask import Flask
from flask import render_template
from CreateAccount import registration
import requests

app = Flask(__name__)
app.secret_key="__privatekey__"

@app.route('/')
def defaultHome():
    return render_template('LogIn.html')

def __init__(self):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("CREATE TABLE user1(name text, password text")

    conn.commit()
    conn.close()

@app.route('/registration',methods=['POST','GET'])
def registrationform():
    registrations = registration()
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    if requests.method=='POST':
        if(requests.form["name"]!="" and requests.form["password"]!=""):
            name=requests.form["name"]
            password=requests.form["password"]
            statement = f"SELECT * from user WHERE name='{name}' AND password='{password}';"
            c.execute(statement)
            data=c.fetchone()
            if data:



    elif requests.method=='GET':
        return render_template('CreateAccount.html',form=registrations)
    '
