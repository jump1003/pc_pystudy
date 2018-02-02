# server.py
from wsgiref.simple_server import make_server
from hello import application


# 创建一个服务器，IP为空，端口8000，处理函数为application
httpd = make_server('', 8000, application)
print('Starting Server HTTP on port 8000...')
#  监听httpd请求
httpd.serve_forever()
