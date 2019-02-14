# /user/bin/python3
# -*- coding:utf-8 -*-
# @Time     :2019/2/12 13:08
# @Author   :zhong
# @Software :PyCharm
import pika


credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.101.172', 5672, '/', credentials))

channel = connection.channel()
channel.exchange_declare(exchange='direct_test', exchange_type='direct')
channel.queue_declare(queue='task', durable=True)
# 定义管理的路由键值对为.3oxz结尾
channel.queue_bind(exchange='direct_test', queue='task', routing_key='.3oxz')


def callback(ch, method, properties, body):
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 接收消息
channel.basic_consume(
    callback, queue='task', no_ack=False
)


channel.start_consuming()