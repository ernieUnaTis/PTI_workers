from celery import Celery

import requests
import random

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def send_javaProducer():
    num = random.randint(1111111, 99999999)
    msisdn = "54" + str(num)
    parametros={"msisdn":msisdn,"carrier":"ar.movistar","operador":"722200"}
    print(requests.get('http://localhost:8080/Productor/Productor', params=parametros).text)
