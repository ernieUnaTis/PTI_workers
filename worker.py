from celery import Celery
import pika

# RabbitMQ Consumir la Informacion
app = Celery('tasks', broker='amqp://guest@localhost//', backend='amqp')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='notificacion_terceros')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='notificacion_terceros', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
