import socket

the_target = '127.8.8.1'


# defining the port_scanner function
def port_scanner(port_number):
  try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating socket for the address family ipv4(AF_INET) and is a tcp socket(SOCK_STREAM)
    socket.connect((the_target, port_number))
  
