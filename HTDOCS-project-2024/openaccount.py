#!C:\Users\praff\AppData\Local\Programs\Python\Python312\python
print('content-type:text/html')
print()

import cgi
import pymysql

reqobj=cgi.FieldStorage()
no=int(reqobj.getvalue("accountNumber"))
nm=reqobj.getvalue("name")
ty=reqobj.getvalue("accountType")
bl=float(reqobj.getvalue("balance"))

print(f"{no} {nm} {ty} {bl}")

con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_tcr4f3ZnICCfhmNruwF',database='sharayudb')
curs=con.cursor()

try:
    curs.execute("insert into accounts values(%d,'%s','%s',%.2f)" %(no,nm,ty,bl))
    con.commit()
    print('account opened successfully')
except:
    print('eeror in insert')

con.close()
