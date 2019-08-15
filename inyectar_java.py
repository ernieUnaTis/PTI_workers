from celery import Celery

import requests

app = Celery('tasks', broker='pyamqp://guest@localhost//')

parametros={"msisdn":"541234567891","carrier":"ar.movistar","operador":"722200"}
headers = {'Content-Type':'text/html'}
print(requests.get('http://localhost:8080/Productor/Productor', params=parametros, headers=headers).text)
