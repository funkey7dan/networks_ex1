from socket import socket,AF_INET,SOCK_DGRAM,inet_aton
import sys

BUFFER = 95
IP = sys.argv[2]
PORT = int(sys.argv[1])
file_name = sys.argv[3]
try:
    file = open(file_name,mode = 'rb')
except Exception as e:
    print("Error opening file!\n")
    print(str(e))
s = socket(AF_INET,SOCK_DGRAM)
try:
    inet_aton(IP)
except Exception as e:
    print("IP error!\n")
    print(str(e))
s.settimeout(5)
bytes = file.read(BUFFER)
index = 0
# while we have chunks left in the file
try:
    while bytes:
        # send the chunk to the server, while appending it's index
        s.sendto(str(index).encode() + b'_' + bytes,(IP,PORT))
        received_bool = False  # flag to know whether the server replies
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
                s.sendto(str(index).encode() + b'_' + bytes,(IP,PORT))
except Exception as e:
    print("Error running client\n")
    print(str(e))
finally:
    file.close()
    #close the socket
    s.close()
    exit()
