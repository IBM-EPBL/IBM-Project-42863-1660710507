# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

from pickle import TRUE
from flask import Flask,render_template,request
import ibm_db
from prettytable import from_db_cursor
import ibm_db_dbi as db2
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=vpl82476;PWD=k8i1UBTUAkS3ZV2k;",'','')
# print(conn1)
# conn = db2.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=vpl82476;PWD=k8i1UBTUAkS3ZV2k;",'','')
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/', methods =["GET", "POST"])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
       
        c=f"insert INTO users(fname,email,pword) values('{name}','{email}','{password}')"
        ibm_db.exec_immediate(conn,c)
        return render_template('home.html')
    else:
        return render_template('index.html')

@app.route('/signin', methods =["GET", "POST"])
# ‘/’ URL is bound with hello_world() function.
def signin():
    if request.method == "POST":
        # name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        sql = "SELECT * FROM users"
        stmt = ibm_db.exec_immediate(conn, sql)
        while ibm_db.fetch_row(stmt) != False:
            if ibm_db.result(stmt, 1)==email and ibm_db.result(stmt, 2)==password:
                print('sucess')
                return render_template('home.html')
            else:
                print('nope')
                
        return render_template('signin.html')
            
                
            # print( "The Employee number is : ",  ibm_db.result(stmt, 0))
            # print( "The last name is : ", ibm_db.result(stmt, 1) )
            # print( "The last name is : ", ibm_db.result(stmt, 2) )
     
            
            
        
        
    else:
        return render_template('signin.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
    
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
