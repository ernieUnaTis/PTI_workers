from celery import Celery

from kafka import KafkaProducer

import pika


# RabbitMQ Consumir la Informacion
app = Celery('tasks', broker='amqp://guest@localhost//', backend='amqp')
#print "Ernesto"



connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='notificacion_terceros')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # Kafka Enviar Informacion
    bootstrap_servers = ['localhost:9092']
    topicName = 'notificacion_terceros'
    producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
    producer = KafkaProducer()
    ack = producer.send(topicName,  value=body)
    metadata = ack.get()
    print("Inyeccion a Kafka Correcta")
    #print(metadata.partition)


channel.basic_consume(queue='notificacion_terceros', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
