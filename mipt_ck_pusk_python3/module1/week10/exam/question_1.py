import socket
import random
import datetime
# Params START
server_name_udp = 'time.nist.gov'
server_port_udp = 37
time_diff = 2208988800 # 25567 days between 01.01.1900(Start of XX century) and 01.01.1970(Unix Time)
# Params END
r_byte = random.randbytes(1)
#Make request
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(r_byte, (server_name_udp, server_port_udp))
answer_byte = sock.recv(4)
#Convert from bytes to int
answer_int = int.from_bytes(answer_byte, byteorder="big", signed=False)
answer_now = answer_int - time_diff
#Print UTC time
print(datetime.datetime.utcfromtimestamp(answer_now).strftime('%Y-%m-%d %H:%M:%S'))