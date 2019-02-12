# /user/bin/python3
# -*- coding:utf-8 -*-
# @Time     :2019/2/12 10:57
# @Author   :zhong
# @Software :PyCharm
import pika

# 创建凭证
credentials = pika.PlainCredentials('admin', 'admin')
# 链接服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.101.172', 5672, '/', credentials))
# 创建频道
channel = connection.channel()

# 在频道内声明消息队列, 队列名为hello, durable=True 表示队列持久化
# durable设置只是重启之后，队列依旧存在。但是队列的内容不存在了。
channel.queue_declare(queue='hello', durable=True)

# 向名为hello的消息队列中插入Hello World!字段
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello World!',
    properties=pika.BasicProperties(delivery_mode=2)
)
# properties=pika.BasicProperties(delivery_mode=2)
# 如果仅仅是设置了队列的持久化，仅队列本身可以在rabbit-server宕机后保留，队列中的信息依然会丢失，如果想让队列中的信息或者任务保留，
# 还需要做以上设置。
# ----------------------------------------------------------------------------------------------------------------------
#消息队列持久化包括3个部分：
#    　　（1）exchange持久化，在声明时指定durable => 1
#    　　（2）queue持久化，在声明时指定durable => 1
#    　　（3）消息持久化，在投递时指定delivery_mode=> 2（1是非持久化）

# 如果exchange和queue都是持久化的，那么它们之间的binding也是持久化的。
# 如果exchange和queue两者之间有一个持久化，一个非持久化，就不允许建立绑定。

connection.close()