#!C:\Users\praff\AppData\Local\Programs\Python\Python312\python
print('content-type:text/html')
print()

import cgi
import pymysql

reqobj=cgi.FieldStorage()
no=int(reqobj.getvalue("ano"))

print('<h3>Search Result</h3><hr>')

con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_tcr4f3ZnICCfhmNruwF',database='sharayudb')
curs=con.cursor()
curs.execute("select * from accounts where accno=%d" %no)
data=curs.fetchone()
if data:
    print(data)
else:
    print('not found')

con.close()
