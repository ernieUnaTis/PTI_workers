from celery import Celery
from kafka import KafkaProducer
import time
import sys
import stomp

app = Celery('tasks', broker='pyamqp://guest@localhost//')

i = 1

class MyListener(stomp.ConnectionListener):
    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        for x in range(10):
            print(x)
            time.sleep(1)
        print('processed message')

while i > 0:
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
        body = val[1].encode()
        ack = producer.send(topicName,  value=message)
        metadata = ack.get()
        print( message['msisdn'])
    #conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')
    time.sleep(2)
    conn.disconnect()
