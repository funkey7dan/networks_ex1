import socket
import sys

PORT = int(sys.argv[1])
BUFFER = 100

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',PORT))
received_indexes_list = []
while True:
    received_bool = False
    while not received_bool:
        try:
            data,addr = s.recvfrom(BUFFER)
            data_decoded = data.decode('utf8').split('_')
            index = data_decoded[0]
            data = data_decoded[1]
            if index not in received_indexes_list:
                # data_arr = bytearray(data)
                # del data_arr[0]
                print(data,end = '')
                received_indexes_list.append(index)
            received_bool = True
            s.sendto(index.encode(),addr)
        except Exception as e:
            print(str(e)+"ERROR")
            continue
