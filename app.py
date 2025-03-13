from flask import Flask
from flask import render_template
from flask import request
import requests
import json
import pandas as pd
import time
# import mysql.connector
# from flask_cors import CORS
# mysql = mysql.connector.connect(user='web', password='webPass',
#   host='127.0.0.1',
#   database='student')

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
app = Flask(__name__)
# CORS(app)
# My SQL Instance configurations
# Change the HOST IP and Password to match your instance configurations

@app.route("/test")#URL leading to method
def test(): # Name of the method
 return("Hello World!<BR/>THIS IS ANOTHER TEST!") #indent this line

@app.route("/yest")#URL leading to method
def yest(): # Name of the method
 return("Hello World!<BR/>THIS IS YET ANOTHER TEST!") #indent this line


@app.route("/fetch/<symbol>")
def fetchPrices():

  url=f'https://query2.finance.yahoo.com/v8/finance/chart/{symbol}?period1=1739494200&period2={int(time.time())}&interval=5m&includePrePost=true&events=div%7Csplit%7Cearn&&lang=en-US&region=US'

headers={'accept': '*/*',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'no-cache',
'cookie': f'GUCS=ASTF5w0L; GUC=AQABCAFnuaRn6UIdogSV&s=AQAAAFGXNzqT&g=Z7hfuA; A1=d=AQABBK5fuGcCEIgFWNQR6ZF7ISuvyCWpcCoFEgABCAGkuWfpZ-Ijb2UBAiAAAAcIqF-4Z9txERE&S=AQAAAkwUiSG1FZkE-D2bD3shBhM; EuConsent=CQNLZQAQNLZQAAOACKENBdFgAAAAAAAAACiQAAAAAAAA; A1S=d=AQABBK5fuGcCEIgFWNQR6ZF7ISuvyCWpcCoFEgABCAGkuWfpZ-Ijb2UBAiAAAAcIqF-4Z9txERE&S=AQAAAkwUiSG1FZkE-D2bD3shBhM; A3=d=AQABBK5fuGcCEIgFWNQR6ZF7ISuvyCWpcCoFEgABCAGkuWfpZ-Ijb2UBAiAAAAcIqF-4Z9txERE&S=AQAAAkwUiSG1FZkE-D2bD3shBhM; cmp=t={int(time.time())}&j=1&u=1---&v=67; PRF=t%3DNVDA',
'origin': 'https://finance.yahoo.com',
'pragma': 'no-cache',
'priority': 'u=1, i',
'referer': f'https://finance.yahoo.com/quote/{symbol}/',
'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}


resp=requests.get(url, headers=headers)

j=json.loads(resp.content)

df=pd.DataFrame(j['chart']['result'][0]['indicators']['quote'][0],index=j['chart']['result'][0]['timestamp'])

df.to_csv(f'{symbol}.csv')


# @app.route("/add", methods=['GET', 'POST']) #Add Student
# def add():
#   if request.method == 'POST':
#     name = request.form['name']
#     email = request.form['email']
#     print(name,email)
#     cur = mysql.cursor() #create a connection to the SQL instance
#     s='''INSERT INTO students(studentName, email) VALUES('{}','{}');'''.format(name,email)
#     app.logger.info(s)
#     cur.execute(s)
#     mysql.commit()
#   else:
#     return render_template('add.html')

#   return '{"Result":"Success"}'
# @app.route("/") #Default - Show Data
# def hello(): # Name of the method
#   cur = mysql.cursor() #create a connection to the SQL instance
#   cur.execute('''SELECT * FROM students''') # execute an SQL statment
#   rv = cur.fetchall() #Retreive all rows returend by the SQL statment
#   Results=[]
#   for row in rv: #Format the Output Results and add to return string
#     Result={}
#     Result['Name']=row[0].replace('\n',' ')
#     Result['Email']=row[1]
#     Result['ID']=row[2]
#     Results.append(Result)
#   response={'Results':Results, 'count':len(Results)}
#   ret=app.response_class(
#     response=json.dumps(response),
#     status=200,
#     mimetype='application/json'
#   )
#   return ret #Return the data in a string format
if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080
  #app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080