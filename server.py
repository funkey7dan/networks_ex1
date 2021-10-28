import socket
import sys
IP = "10.0.2.4"
PORT = int(sys.argv[1])
BUFFER = 100

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',PORT))

while True:
    received_bool = False
    while not received_bool:
        try:
            data,addr = s.recvfrom(BUFFER)
            if data:
                print(str(data.decode('utf8')),end = '')
                #print("Sent yes")
                # while not s.sendto(data,addr):
                #     print("in while")
                #     s.sendto(data,addr)
                received_bool = True
        except:
            continue
   # data,addr = s.recvfrom(BUFFER)
    #if data:
     #   print(str(data.decode('utf8')),end = '')
        #print("Sent yes")
      #  s.sendto(data,addr)
        #s.sendto(b'yes',addr)
    # else:
    #     print(str(data.decode('utf8')),end = '')
    #s.sendto(data,addr)
