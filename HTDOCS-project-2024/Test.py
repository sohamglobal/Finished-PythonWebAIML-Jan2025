#!C:\Users\praff\AppData\Local\Programs\Python\Python313\python

print('content-type:text/html')
print()

#--------
print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">')
print("<div class='container'><br><br>")
print('<h2 class="display-5">serverside python tested ok...</h2><hr>')

lst=['Java','Python','C#','JavaScript','SQL']

for nm in lst:
    print('<li>')
    print(nm)

print('<hr>')

import pymysql
con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_tcr4f3ZnICCfhmNruwF',database='sharayudb')
curs=con.cursor()
curs.execute("select * from employees")
data=curs.fetchall()
print(data)
con.close()

print("<br><a href='index.html'>Home</a>")
print('</div>')
