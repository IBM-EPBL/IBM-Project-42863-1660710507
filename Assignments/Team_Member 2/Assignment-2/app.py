from pickle import TRUE
from flask import Flask,render_template,request
import ibm_db
import ibm_db_dbi as db2
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ylh47723;PWD=x13sSumMMxfN5M1x;",'','')
app = Flask(__name__)
@app.route('/', methods =["GET", "POST"])
def homepage():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pword")
       
        c=f"insert INTO user(email,pwd) values('{email}','{password}')"
        ibm_db.exec_immediate(conn,c)
        return render_template('index.html')
    else:
        return render_template('signup.html')

@app.route('/signin', methods =["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pword")
        sql = "SELECT * FROM user"
        stmt = ibm_db.exec_immediate(conn, sql)
        while ibm_db.fetch_row(stmt) != False:
            if ibm_db.result(stmt, 1)==email and ibm_db.result(stmt, 2)==password:
                print('sucess')
                return render_template('index.html')
            else:
                print('nope')
                
        return render_template('signin.html')
    else:
        return render_template('signin.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
    
if __name__ == '__main__':
	app.run()