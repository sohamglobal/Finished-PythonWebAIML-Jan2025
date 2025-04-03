#!C:\Users\praff\AppData\Local\Programs\Python\Python313\python
print('content-type:text/html')
print()

import cgi
import pymysql

reqobj=cgi.FieldStorage()
nm=reqobj.getvalue("unm")

print('<h3>Welcome %s to serverside python</h3><hr>' %nm)
con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_tcr4f3ZnICCfhmNruwF',database='sharayudb')
curs=con.cursor()
#curs.execute("select * from accounts where accnm='%s'" %nm)
curs.execute("select * from accounts where accnm like '%%%s%%'" %nm)
data=curs.fetchall()
if data:
    print(data)
else:
    print('not found')
con.close()



