1. 新建一个 django project
django-admin.py startproject project-name
特别是在 windows 上，如果报错，尝试用 django-admin 代替 django-admin.py 试试

2. 新建 app
python manage.py startapp app-name

3. 同步数据库
python manage.py syncdb 
注意：Django 1.7.1及以上的版本需要用以下命令
python manage.py makemigrations
python manage.py migrate

4. 使用开发服务器
python manage.py runserver 
# 当提示端口被占用的时候，可以用其它端口：
python manage.py runserver 8001
python manage.py runserver 9999
（当然也可以kill掉占用端口的进程）
# 监听所有可用 ip （电脑可能有一个或多个内网ip，一个或多个外网ip，即有多个ip地址）
python manage.py runserver 0.0.0.0:8000
# 如果是外网或者局域网电脑上可以用其它电脑查看开发服务器
# 访问对应的 ip加端口，比如 http://172.16.20.2:8000

6. 创建超级管理员
python manage.py createsuperuser 
# 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填
# 修改 用户密码可以用：
python manage.py changepassword username
