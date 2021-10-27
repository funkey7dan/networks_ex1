from socket import socket,AF_INET,SOCK_DGRAM
import sys

BUFFER = 100
IP = sys.argv[1]
PORT = int(sys.argv[2])
file_name = sys.argv[3]
file = open(file_name,mode = 'rb')
s = socket(AF_INET,SOCK_DGRAM)
s.settimeout(1)

bytes = file.read(BUFFER)
sent = 0
received = 0
while bytes:
    s.sendto(bytes,(IP,PORT))
    print("sent\n" + bytes.decode())
    sent += 1
    received_bool = False
    while not received_bool:
        try:
            data,addr = s.recvfrom(BUFFER)
            if data.decode() == 'yes':
                received_bool = True
        except:
            s.sendto(b'received',(IP,PORT))

    while received < sent:
        try:
            data,addr = s.recvfrom(BUFFER)
            received += 1
            #print(data)
            bytes = file.read(BUFFER)
            break
        except:
            print("No data")
            #s.sendto(bytes,(IP,PORT))
            #print("sent\n" + bytes.decode())  #print(data)
file.close()
# data,addr = s.recvfrom(BUFFER)
# print(data)
if sent == received:
    print("data matches")
s.close()
exit(0)
