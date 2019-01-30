# redis的笔记 - linux版本

## redis的部署
先找到linux的redis包，百度redis进入到官网，截取链接。

![获取下载链接](https://github.com/ZhiZhao-Hong/Note/blob/master/redis/img/1.png)

下载并解压数据包
```
# cd /
# cd etc
# wget http://download.redis.io/releases/redis-5.0.3.tar.gz
# tar zxvf redis-5.0.3.tar.gz
```

编译
```
# cd redis-5.0.3
# make
```

redis/src目录下有四个可以执行的文件
1. redis-server : 启动服务
2. redis-bencmark
3. redis-cli ： 
4. redis.conf

启动服务，然后插入队列
```
# cd src
# ./redis-server
# ./redis-cli
```