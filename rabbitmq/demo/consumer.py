# /user/bin/python3
# -*- coding:utf-8 -*-
# @Time     :2019/2/12 11:12
# @Author   :zhong
# @Software :PyCharm
import pika


credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.101.172', 5672, '/', credentials))
channel = connection.channel()

# 处理函数
def callback(ch, method, properties, body):
    print(body)
    # 确认消费成功之后，才发送回调。base_consume需要将no_ack设置为false
    ch.basic_ack(delivery_tag=method.delivery_tag)

# no_ack=true 表示回调函数不需要发送确认标识
# no_ack=False 表示消费函数需要发送确认消费完成表示符
channel.basic_consume(
    callback,
    queue='hello',
    no_ack=False
)

channel.start_consuming()