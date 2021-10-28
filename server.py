import socket
import sys

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
PORT = int(sys.argv[1])
BUFFER = 97
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',PORT))
received_array = []
to_request = []

while True:
    data,addr = s.recvfrom(BUFFER)
    if data == b'END_':
        # return with confirmation
        s.sendto(b'END_' + b'ac',addr)
        i = 0
        # iterate through the received bytes and check what indexes are empty
        for b in received_array:
            if received_array[i]:
                pass
            else:
                # add the index that is empty to the list of those we need to resend
                to_request.append(i)
                i += 1
        # combine the missing indexes
        missing = ",".join(to_request)
        send_until_confrm(missing.encode(),addr)
    elif data == b'_FIN':
        s.sendto(b'_FIN' + b'ac',addr)
        for b in received_array:
            b_arr = bytearray(b)
            del b_arr[0]
            print(b_arr.decode())
    else:
        index = (data[0] - 48) # 48 is 0 in ascii
        received_array.insert(index,data)
