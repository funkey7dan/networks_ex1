import socket
import sys

PORT = int(sys.argv[1])
BUFFER = 100

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',PORT))
received_indexes_list = []  # list to hold all the indexes we already received

# main script loop
try:
    while True:
        received_bool = False  # flag to know whether the client sent something
        while not received_bool:
            # try to recieve a datagram from the server
            try:
                data,addr = s.recvfrom(BUFFER)
                #split the data using the delimiter to separate the index and the data
                data_decoded = data.decode('utf8').split('_')
                index = data_decoded[0]
                data = data_decoded[1]
                # if we didn't receive this data before, the index is not in our list, we print the data
                if index not in received_indexes_list:
                    print(data,end = '',flush = True)
                    # add the index to the list
                    received_indexes_list.append(index)
                received_bool = True
                # send the index to the client to notify we got the message
                s.sendto(index.encode(),addr)
            # if no data was received, go to the next iteration
            except:
                continue
finally:
    s.close()