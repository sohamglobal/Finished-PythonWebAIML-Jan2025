#!C:\Users\praff\AppData\Local\Programs\Python\Python312\python
print('content-type:text/html')
print()

import cgi
import pymysql

reqobj=cgi.FieldStorage()
no=int(reqobj.getvalue("eno"))
nm=reqobj.getvalue("enm")
dp=reqobj.getvalue("dep")
po=reqobj.getvalue("pos")
lo=reqobj.getvalue("loc")
sl=float(reqobj.getvalue("sal"))

#print(f"{no} {nm} {dp} {po} {lo} {sl}")
con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_tcr4f3ZnICCfhmNruwF',database='sharayudb')
curs=con.cursor()
try:
    curs.execute("insert into employees values(%d,'%s','%s','%s','%s',%.2f)" %(no,nm,dp,po,lo,sl))
    con.commit()
    print('new employee inserted successfully')
except:
    print('insert failed')
con.close()

