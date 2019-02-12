# rabbitmq 使用教程

## linux 下部署rabbitmq服务器

### 1. 安装epel依赖包

```rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm```

### 2. 安装erlang依赖包
```yum install erlang```

### 3. 下载rabbitmq-server
```wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.7.11/rabbitmq-server-3.7.11-1.el7.noarch.rpm```

### 4. 安装rabbitmq-server
```rpm -ivh rabbitmq-server-3.7.11-1.el7.noarch.rpm```

### 5. 生成配置文件
```cp /usr/share/doc/rabbitmq-server-3.6.1/rabbitmq.config.example /etc/rabbitmq/rabbitmq.config```

### 6. 启动rabbitmq
```rabbitmq-server start```

### 7. 对外开放防火墙

## Python 操作rabbitmq-server
