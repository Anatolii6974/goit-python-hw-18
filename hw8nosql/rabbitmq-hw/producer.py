from faker import Faker
from datetime import datetime
import pika
from models_rmq import *
from mongoengine import *

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_mock', queue='task_queue')
fake = Faker()

def main():

    for i in range(5):
        task = Task(fullname=fake.name(), email=fake.email())
        task.save()
        print(task)
        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=str(task.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
    connection.close()
    
    
if __name__ == '__main__':
    main()