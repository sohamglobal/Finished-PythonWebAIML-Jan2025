#!C:\Users\praff\AppData\Local\Programs\Python\Python312\python
print('content-type:text/html')
print()

import pymysql

con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_tcr4f3ZnICCfhmNruwF',database='sharayudb')
curs=con.cursor()
curs.execute("select * from customers")
data=curs.fetchall()

print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">')
print("<div class='container'><br><br>")
print('<h2 class="display-5">serverside python tested ok...</h2><hr>')

print('<table class="table table-bordered table-hover">')
print("<tr>")
print("<th>Number")
print("<th>Name")
print("<th>City")
print("<th>CarID")
print("<th>PayMode")
print("</tr>")


for rec in data:
    print('<tr>')
    print('<td>',rec[0])
    print('<td>',rec[1])
    print('<td>',rec[2])
    print('<td>',rec[3])
    print('<td>',rec[4])
    print('</tr>')

print('</table>')


con.close()