from celery import Celery
from kafka import KafkaProducer
import time
import sys
import stomp

app = Celery('tasks', broker='pyamqp://guest@localhost//')

i = 1

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        bootstrap_servers = ['localhost:9092']
        topicName = 'notificacion_eventos_internos'
        producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
        producer = KafkaProducer()
        ack = producer.send(topicName,  value=message.encode())
        metadata = ack.get()
        print("Inyeccion a Kafka Correcta desde AMQ" )


print("AQUI")
read_messages = []
conn = stomp.Connection()
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True)
conn.subscribe(destination='ar.movistar.reciclaje', id=1, ack='auto')
for message in read_messages:
    bootstrap_servers = ['localhost:9092']
    topicName = 'notificacion_eventos_internos'
    producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
    producer = KafkaProducer()
    ack = producer.send(topicName,  value=message.encode())
    metadata = ack.get()
    print("Inyeccion a Kafka Correcta 2")
#conn.send(body='Test from Python', destination='/queue/SAMPLEQUEUE')
time.sleep(2)
conn.disconnect()
