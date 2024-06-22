import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address = "172.20.10.4"
port_no =     9999           # 0 - 65536

target_address = (ip_address,port_no)

message = input("Plz write your message : ")

encrypted_message = message.encode('ascii')
s.sendto(encrypted_message,target_address)