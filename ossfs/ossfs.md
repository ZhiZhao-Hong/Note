# ossfs使用

## 安装及使用
**1. 进入官网下载对应的数据包**

```https://help.aliyun.com/document_detail/32196.html?spm=a2c4g.11186623.6.1315.7da55d265qMB1B```

**2. 寻找对应的数据包**

![获取下载链接](https://github.com/ZhiZhao-Hong/Note/blob/master/ossfs/img/ossfs%E4%B8%8B%E8%BD%BD.png)

**3. 下载命令 - CentOS7**

```wget http://gosspublic.alicdn.com/ossfs/ossfs_1.80.5_centos7.0_x86_64.rpm```

**4. 安装 ossfs2**

设置bucket name 和 AccessKeyId/Secret信息，将其存放在/etc/passwd-ossfs 文件中。注意这个文件的权限必须正确设置，建议设为640。

```echo my_bucket:faint:123 > /etc/passwd-ossfs```

```chmod 640 /etc/passwd-ossfs```

<br>

将```my_bucket```这个bucket挂载到 ```/tmp/ossfs``` 目录下， AccessKeyIds是```faint```,
AccessKeySecret是```123```

```mkdir /tmp/ossfs```

```ossfs my-bucket /tmp/ossfs -ourl=http://oss-cn-hangzhou.aliyuncs.com```

**5. 卸载bucket**

```fusermount -u /tmp/ossfs ```

---
**如果需要同时挂载两个相同的文件，可以修改/etc/passwd-ossfs**

**重复服务器需要重新挂载ossfs**