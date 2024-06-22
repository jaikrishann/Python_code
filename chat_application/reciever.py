import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address = "172.20.10.4"
port_no =     9999           # 0 - 65536

complete_address = (ip_address,port_no)

s.bind(complete_address)

while True:
    message = s.recvfrom(120)   #(mees,(ip,port))
    
    
    data = message[0]
    data = data.decode('ascii')
    data = data + "\n"
    

    with open(ip_add,'a+') as file:
        file.write(data)
    
