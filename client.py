from socket import socket,AF_INET,SOCK_DGRAM
import sys

# send the same message until it receives it back with added ac at the end
def send_until_confrm(msg,address):
    confirmed = False
    while not confirmed:
        s.sendto(msg,address)
        try:
            data,addr = s.recvfrom(BUFFER)
            if data == msg + b'ac':
                confirmed = True
                break
        except:
            pass
    return
# check for datagrams until received message back from server
def lstn_loop():
    received_bool = False
    while not received_bool:
        try:
            data,addr = s.recvfrom(BUFFER)
            s.sendto(data + b'ac',addr)
            received_bool = True
        except:
            pass
    print("Missing:" + data.decode())
    return data

BUFFER = 97
IP = sys.argv[1]
PORT = int(sys.argv[2])
RECEIVER = (IP,PORT)
file_name = sys.argv[3]
file = open(file_name,mode = 'rb')
s = socket(AF_INET,SOCK_DGRAM)
s.settimeout(1)
to_send_array = []  #array of chunks to send
i = 0
bytes = file.read(BUFFER)
while bytes:
    # add the current chunk to the array
    to_send_array.append(bytes)
    i += 1
    #read next chunk
    bytes = file.read(BUFFER)

chunks_num = len(to_send_array)  #amount of chunks total
# for every chunk in the array we send it with it's index appended
i = 0
for b in to_send_array:
    # add the index before the chunk
    j = str(i)
    s.sendto(j.encode() + b,RECEIVER)
    i += 1
# notify server we are done sending data
send_until_confrm(b'END_',RECEIVER)
missing = lstn_loop()
send_until_confrm(b'_FIN',RECEIVER)
