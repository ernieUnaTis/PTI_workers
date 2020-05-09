from inyectar_java import send_javaProducer
from simulador import simulador
import time



i = 1

while(i>0):
    send_javaProducer()
    simulador()
    time.sleep(5)
