from celery import Celery

import requests

app = Celery('tasks', broker='pyamqp://guest@localhost//')

#@app.task
#def simulador:
xml = "<terraData><fecha>2019-06-11 23:39:06</fecha><idservicio>1934</idservicio><idsusc>1934</idsusc><movil>578112345678</movil><movil_anterior></movil_anterior><operador>co.movistar.fixa</operador><oper_id>732203</oper_id><idtrx>1234567890987654321</idtrx><idnotificacion>xcdhve59vif45kb42e9r</idnotificacion><precio></precio><origen>SMS</origen><evento>EMAIL</evento><plataforma>COLOMBIAFIXA</plataforma><keyword></keyword><tipousuario>3</tipousuario><status>1</status></terraData>"
headers = {'Content-Type':'text/xml'}
print(requests.post('http://127.0.0.1:5000/productor', data=xml, headers=headers).text)
