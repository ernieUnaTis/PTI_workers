from celery import Celery
from kafka import KafkaProducer
import redis
import requests
import random

app = Celery('tasks', broker='pyamqp://guest@localhost//')

i = 1
while i > 0:
    r = redis.Redis()
    val = r.blpop('q_test_mensajeria')
    #print 'Consuming: (%s, %s)' % val
    bootstrap_servers = ['localhost:9092']
    topicName = 'notificacion_mensajeria'
    producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
    producer = KafkaProducer()
    body = val[1]
    ack = producer.send(topicName,  value=body)
    metadata = ack.get()
    print("Inyeccion a Kafka Correcta desde Redis")
