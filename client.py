from socket import socket,AF_INET,SOCK_DGRAM
import sys

BUFFER = 100
IP = sys.argv[1]
PORT = int(sys.argv[2])
file_name = sys.argv[3]
file = open(file_name,mode = 'rb')
s = socket(AF_INET,SOCK_DGRAM)
s.settimeout(10)

bytes = file.read(BUFFER)

while bytes:
    s.sendto(bytes,(IP,PORT))
    print("sent\n" + bytes.decode())
    received_bool = False
    while not received_bool:
        try:
            data,addr = s.recvfrom(BUFFER)
            if data:
                received_bool = True
                bytes = file.read(BUFFER)
        except:
            s.sendto(bytes,(IP,PORT))
            print("sent\n" + bytes.decode())

    # while received < sent:
    #     try:
    #         data,addr = s.recvfrom(BUFFER)
    #         received += 1
    #         #print(data)
    #         bytes = file.read(BUFFER)
    #         break
    #     except:
    #         print("No data")
    #         #s.sendto(bytes,(IP,PORT))
    #         #print("sent\n" + bytes.decode())  #print(data)
file.close()
# data,addr = s.recvfrom(BUFFER)
# print(data)
s.close()
exit(0)
