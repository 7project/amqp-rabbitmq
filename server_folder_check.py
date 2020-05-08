import time
import pika
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='folder')


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        channel.basic_publish(exchange='', routing_key='folder', body=str(event))

    def on_deleted(self, event):
        print(event)
        channel.basic_publish(exchange='', routing_key='folder', body=str(event))

    def on_moved(self, event):
        print(event)
        channel.basic_publish(exchange='', routing_key='folder', body=str(event))

    def on_modified(self, event):
        print(event)
        channel.basic_publish(exchange='', routing_key='folder', body=str(event))


observer = Observer()
observer.schedule(Handler(), path='foolder/', recursive=True)
observer.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

connection.close()
