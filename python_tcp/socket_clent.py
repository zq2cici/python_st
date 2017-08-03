import socket
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s1.connect(('127.0.0.1', 9998))
# 接收欢迎消息:
print(s1.recv(1024).decode('utf-8'))
for data in [b'Michael1', b'Tracy1', b'Sarah1']:
    # 发送数据:
    s1.send(data)
    print(s1.recv(1024).decode('utf-8'))
s1.send(b'exit')
s1.close()
