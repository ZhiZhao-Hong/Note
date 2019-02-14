# rabbitmq 使用教程

## linux 下部署rabbitmq服务器

### 1. 下载rabbitmq-3.7.11

```wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.7.11/rabbitmq-server-3.7.11-1.el7.noarch.rpm```

### 2. 安装依赖 erlang包

```
cd /etc/yum.repos.d
vim rabbitmq_erlang.repo
```

将下面的内容复制到rabbitmq_erlang.repo文件里面

```
[rabbitmq_erlang]
name=rabbitmq_erlang
baseurl=https://packagecloud.io/rabbitmq/erlang/el/7/$basearch
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://packagecloud.io/rabbitmq/erlang/gpgkey
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300

[rabbitmq_erlang-source]
name=rabbitmq_erlang-source
baseurl=https://packagecloud.io/rabbitmq/erlang/el/7/SRPMS
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://packagecloud.io/rabbitmq/erlang/gpgkey
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
```

### 3. 成功添加rabbitmq_erlang.repo之后，直接用yum安装

```yum install erlang```

### 4. 安装依赖包 socat

```yum install socat```

### 5. 安装rabbitmq

```rpm -ivh rabbitmq-server-3.7.11-1.el7.noarch.rpm```

### 6. 生成mq配置文件

```cp /usr/share/doc/rabbitmq-server-3.7.11/rabbitmq.config.example /etc/rabbitmq/rabbitmq.config```

### 7. 启动web插件

```rabbitmq-plugins enable rabbitmq_management```

启动插件之后，可以在网页输入 http://localhost:15672 打开控制台。账号密码默认为guest

### 8. 启动rabbitmq服务

```rabbitmq-server start```

### 9. 停止服务
```rabbitmqctl stop```





### 10. 对外开放防火墙

#### a. 查看已打开的端口

```netstat -anp```

#### b. 查看想开的端口是否已开

```firewall-cmd --query-port=666/tcp```

若提示 FirewallD is not running。 表示为不可知防火墙，需看防火墙是否开启

#### c. 查看防火墙状态 - running：表示开启，dead表示未开启

```systemctl status firewalld```

#### d. 开启防火墙

```systemctl start firewalld```

#### e. 查看想开的端口是否已开

```firewall-cmd --query-port=666/tcp```

#### f. 开永久端口号

```firewall-cmd --add-port=666/tcp --permanent```

#### i. 重新载入配置

```firewall-cmd --reload```

#### j. 移除端口号 - 记得重启

```firewall-cmd --permanent --remove-port=666/tcp```

## Python 操作rabbitmq-server
