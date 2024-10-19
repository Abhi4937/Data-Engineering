#!/c/Users/Sudarshan/Desktop/pythonexe/python
import requests
import json
r=requests.get('https://api.github.com/events')
print(r.encoding)
resp=r.content.decode('utf-8',errors='ignore')
response=json.loads(resp)
print(response)

