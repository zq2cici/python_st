import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael1', b'Tracy1', b'Sarah1']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9977))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
