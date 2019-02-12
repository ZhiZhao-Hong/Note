# /user/bin/python3
# -*- coding:utf-8 -*-
# @Time     :2019/2/12 13:08
# @Author   :zhong
# @Software :PyCharm
import pika


credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.101.172', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='task', durable=True)
channel.basic_publish(
    exchange='',
    routing_key='task',
    body='test',
    properties=pika.BasicProperties(delivery_mode=2)
)
connection.close()