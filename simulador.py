from celery import Celery

import requests
import random

app = Celery('tasks', broker='pyamqp://guest@localhost//')

#@app.task
#def simulador:
i = 1
while i > 0:
    num = random.randint(9999999, 99999999)
    idServicio = random.randint(1, 99999999)
    msisdn = "57" + str(num)
    xml ="<terraData><fecha>2019-06-1123:39:06</fecha><idservicio>"+str(idServicio)+"</idservicio><idsusc>1934</idsusc><movil>"+msisdn+"</movil><movil_anterior></movil_anterior><operador>co.movistar.fixa</operador><oper_id>732203</oper_id><idtrx>1234567890987654321</idtrx><idnotificacion>xcdhve59vif45kb42e9r</idnotificacion><precio></precio><origen>SMS</origen><evento>EMAIL</evento><plataforma>COLOMBIAFIXA</plataforma><keyword></keyword><tipousuario>3</tipousuario><status>1</status></terraData>"
    headers = {'Content-Type':'text/xml'}
    print(requests.post('http://127.0.0.1:5000/productor', data=xml, headers=headers).text)
