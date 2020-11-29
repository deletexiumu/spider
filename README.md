# Python3、DataX以及web2py安装步骤
## DataX安装
1. 将datax.zip文件夹上传到服务器的/data/realinsight目录下，执行命令:`unzip datax.zip`
2. 更改文件夹权限:`chown -R realinsight:realinsight datax`

## Python3安装
1. 将python3.6文件夹上传到/usr/local目录下
2. 创建软连接，执行命令```
ln -s /usr/local/python3.6/bin/python3 /usr/bin/python3
ln -s /usr/local/python3.6/bin/uwsgi /usr/bin/uwsgi
```

## web2py安装
1. 将web2py文件夹上传至nginx的html目录下
2. 更改文件夹权限`chown -R realinsight:realinsight web2py`
3. 安装oracle-client，切换到web2py目录下，执行命令:`rpm -ivh oracle-instantclient18.3-basic-18.3.0.0.0-3.x86_64.rpm`
4. 安装postgresql依赖库，将pgsql-10.zip上传到/usr/local目录下，执行命令`unzip pgsql-10.zip`
5. 添加oracle动态库连接，添加文件`/etc/ld.so.conf.d/oracle.conf`，添加内容:`/usr/lib/oracle/18.3/client64/lib`
6. 添加pg动态库连接，添加文件`/etc/ld.so.conf.d/pgsql.conf`，添加内容:`/usr/local/pgsql-10/lib`
7. 使动态库连接生效，执行命令:`ldconfig`
8. 添加uwsgi配置文件，在/data/realinsight/nginx/tengine/conf目录下创建文件web2py.ini，添加内容```
[uwsgi]
socket = 127.0.0.1:9090
pythonpath = /data/realinsight/nginx/tengine/html/web2py/
mount = /=wsgihandler:application
processes = 4
master = true
harakiri = 60
reload-mercy = 8
cpu-affinity = 1
stats = /tmp/%n.stats.socket
max-requests = 5000
limit-as = 1024
reload-on-as = 256
reload-on-rss = 192
cron = 0 0 -1 -1 -1 /usr/local/python3.6/bin/python3 /data/realinsight/nginx/tengine/html/web2py/web2py.py -Q -S welcome -M -R scripts/sessions2trash.py -A -o
no-orphans = true
chmod-socket = 666```
1. 启动uwsgi，执行命令：`uwsgi -d --ini /data/realinsight/nginx/tengine/conf/web2py.ini`,执行命令`ps aux|grep uwsgi`查看进程是否存在，如果存在则表示启动成功。
2. 测试访问web2py是否部署成功，浏览器访问地址查看页面打开是否正常:`http://ip:port/task_monitor/`
