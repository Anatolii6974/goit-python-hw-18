import pika

from models_rmq import *

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) 

def send_email(str):
    print(f"Send email {str}")

def callback(ch, method, properties, body):
    pk = body.decode()
    task = Task.objects(id=pk, completed=False).first()
    if task:
        task.update(set__completed = True), 
        send_email(task.id)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()