import socket
import threading

def updlink():
     while True:
        # 接收数据:
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        s.sendto(b'Hello, %s!' % data, addr)
     s.close()


def updlink1():
    while True:
        # 接收数据:
        data, addr = s1.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        s1.sendto(b'Hello, %s!' % data, addr)
    s1.close()



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')

t = threading.Thread(target=updlink)
t.start()




s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s1.bind(('127.0.0.1', 9977))
print('Bind UDP on 9977...')

t1 = threading.Thread(target=updlink1)
t1.start()

t.join()
t1.join()

'''
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
'''   
