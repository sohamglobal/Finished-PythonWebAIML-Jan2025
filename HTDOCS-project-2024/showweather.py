#!C:\Users\praff\AppData\Local\Programs\Python\Python312\python
print('content-type:text/html')
print()

import cgi
from urllib import request
import json

reqobj=cgi.FieldStorage()
ct=reqobj.getvalue("city")

print("<h2>Weather of City : %s</h2><hr>" %ct)

response=request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ct+"&appid=5ea9269ece0f0c287803a5b69fca4d80")
data=response.read()
info=json.loads(data)
#print(info)
desc=info['weather'][0]['description']
print('description : ',desc)

flike=info['main']['feels_like']
cel=flike-272.15
print('<br>Feels Like %.2f' %cel)


