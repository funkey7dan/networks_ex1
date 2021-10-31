from socket import socket,AF_INET,SOCK_DGRAM
import sys

BUFFER = 95
IP = sys.argv[1]
PORT = int(sys.argv[2])
file_name = sys.argv[3]
file = open(file_name,mode = 'rb')
s = socket(AF_INET,SOCK_DGRAM)
s.settimeout(5)

bytes = file.read(BUFFER)
index = 0
# while we have chunks left in the file
try:
    while bytes:
        # send the chunk to the server, while appending it's index
        s.sendto(str(index).encode()+b'_'+bytes,(IP,PORT))
        received_bool = False # flag to know whether the server replies
        # while we have no answer from the server
        while not received_bool:
            # try to recieve a datagram from the server
            try:
                data,addr = s.recvfrom(BUFFER)
                # if we received a datagram, check if it's the index of the chunk we send, as an ACK from server
                if data.decode() == str(index):
                    received_bool = True
                    # increment index count and read next chunk
                    index += 1
                    bytes = file.read(BUFFER)
            # if we didn't receive data from the server, send it again
            except:
                s.sendto(str(index).encode()+b'_'+bytes,(IP,PORT))
finally:
    file.close()
    #close the socket
    s.close()
    exit(0)
