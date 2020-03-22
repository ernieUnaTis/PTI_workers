from celery import Celery

import requests
import random

app = Celery('tasks', broker='pyamqp://guest@localhost//')

i = 1
while i > 0:
    num = random.randint(9999999, 99999999)
    msisdn = "54" + str(num)
    parametros={"msisdn":msisdn,"carrier":"ar.movistar","operador":"722200"}
    print(requests.get('http://localhost:8080/Productor/Productor', params=parametros).text)
