#!C:/Users/praff/AppData/Local/Programs/Python/Python313/python.exe
print("Content-Type: text/html")
print()

import sys
from urllib.parse import parse_qs
import os
os.environ["USERNAME"] = "praff"
import pymysql

content_length = int(os.environ.get('CONTENT_LENGTH', 0))
post_data = sys.stdin.read(content_length)
form_data = parse_qs(post_data)
no = int(form_data.get('ano', [''])[0])

print(f"<html><body><h1>Hello, {no}!</h1></body></html>")



