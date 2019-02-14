# centos7 安装

## 1. 查找python的数据包

数据包网址：

```https://www.python.org/ftp/python```

## 2. 下载数据包

```wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz```

## 3. 解压下载的文件包

```tar -xvf Python-3.7.2.tgz```

## 4. 安装Python3.7+版本需要安装新包libffi-devel
```
yum install libffi-devel -y
make install
```

## 4. 进入解压目录, 并配置到指定目录
```
cd Python-3.7.2.tgz
mkdir /usr/local/python3
./configure --prefix==/usr/local/python3
make
make install
```

## 5. 创建软连接
```ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3```
```ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3```