from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import ibm_db
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:32731;PORT= 32731;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA (5).crt;UID=lgp7181;PWD=m0PY1tHmNDQwC0no;",'','')
print(conn)
print('connection succesful')

app = Flask(__name__)
app.secret_key ='itsmysecretkey'
@app.route('/login')
def login():
    return render_template('sign-in.html')

@app.route('/register')
def register():
    return render_template('register.html')

if(__name__=='__main__'):
    app.run(host='0.0.0.0',debug=True)
