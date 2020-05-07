import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='folder')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume('folder', callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('Stop server in hand!')
