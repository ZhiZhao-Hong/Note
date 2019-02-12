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

a. 查看已打开的端口

```netstat -anp```

b. 查看想开的端口是否已开

```firewall-cmd --query-port=666/tcp```

若提示 FirewallD is not running。 表示为不可知防火墙，需看防火墙是否开启

c. 查看防火墙状态 - running：表示开启，dead表示未开启

```systemctl status firewalld```

d. 开启防火墙

```systemctl start firewalld```

e. 查看想开的端口是否已开

```firewall-cmd --query-port=666/tcp```

f. 开永久端口号

```firewall-cmd --add-port=666/tcp --permanent```

i. 重新载入配置

```firewall-cmd --reload```

j. 移除端口号 - 记得重启

```firewall-cmd --permanent --remove-port=666/tcp```

## Python 操作rabbitmq-server
