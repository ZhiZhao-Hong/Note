# /user/bin/python3
# -*- coding:utf-8 -*-
# @Time     :2019/2/12 13:08
# @Author   :zhong
# @Software :PyCharm
import pika
import time


credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.19.128', 5672, '/', credentials))
channel = connection.channel()
channel.exchange_declare(exchange='direct_test', exchange_type='direct')

for i in range(0, 60):
    channel.basic_publish(
        exchange='direct_test',
        routing_key='.3oxz',
        body=str(i),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    time.sleep(1)
connection.close()