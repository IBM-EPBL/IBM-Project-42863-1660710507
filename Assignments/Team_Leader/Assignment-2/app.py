from pickle import TRUE
from flask import Flask,render_template,request
import ibm_db
import ibm_db_dbi as db2
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=31249;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=qgz17067;PWD=IDxrQyZ1Jed6CmrX;",'','')
app = Flask(__name__)
@app.route('/', methods =["GET", "POST"])
def hello_world():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pword")
       
        c=f"insert INTO users(email,pword) values('{email}','{password}')"
        ibm_db.exec_immediate(conn,c)
        return render_template('home page.html')
    else:
        return render_template('signup.html')

@app.route('/signin', methods =["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        sql = "SELECT * FROM users"
        stmt = ibm_db.exec_immediate(conn, sql)
        while ibm_db.fetch_row(stmt) != False:
            if ibm_db.result(stmt, 1)==email and ibm_db.result(stmt, 2)==password:
                print('sucess')
                return render_template('home page.html')
            else:
                print('nope')
                
        return render_template('home page.html')
    else:
        return render_template('signin.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home page.html')
    
if __name__ == '__main__':
	app.run()