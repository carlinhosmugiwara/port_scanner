import socket # library to create and manipulate sockets
from queue  import Queue # library to create and manipulate queue data structure
import threading # library to easily create threads and multithreads

the_target = '127.0.0.1' # I used the ip of every local machine here, but you can run it in every ip that you're authorized to do so
open_ports = []
queue = Queue()

# defining the port_scanner function
def port_scanner(port):
  try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating socket for the address family ipv4(AF_INET) and is a tcp socket(SOCK_STREAM)
    socket.connect((the_target, port_number)) # trying to connect to the port
    return True # this means that the connection was successful and that the port is vulnerable
  except:
    return False # this means that the connection was not a success and that the port is closed
  
# defining function to insert ports into the queue  
def put_into_queue(ports):
  for port in ports: # iterating eveyr port in the list
    queue.put(port) # putting it into the queue

# defining the rules to fill the open_ports list    
def target():
  while not queue.empty():
    if(port_scanner(port)):
      print("Port " + str(port) + " is open")
      open_ports.append(port)

# defining the ports that'll be scanned
ports = [ 22, 25, 80, 21, 53, 443] # 22: ssh; 25: smtp; 80: http; 21: ftp; 53: dns; 443: https
put_into_queue(ports) # putting the ports into the queue

threads = []

for thrd in range(45): # number of threads that will occur
  thread = threading.Thread(target=target) # the function that will be the target of the threads
  threads.append(thread)
  
for thread in threads:
  thread.start()
  
for thread in threads:
  thread.join()

# jus something that I did for fun to say the name of the port that's open, not the number  
for i in range(0, len(open_ports)):
  if(open_ports[i] == 22:
    open_ports[i] = "SSH"
  elif(open_ports[i] == 25:
     open_ports[i] = "SMTP"
  elif(open_ports[i] == 80:
     open_ports[i] = "HTTP"
  elif(open_ports[i] == 21:
     open_ports[i] = "FTP"
  elif(open_ports[i] == 53:
     open_ports[i] = "DNS"
  elif(open_ports[i] == 443):
     open_ports[i] == "HTTPS"
         
print("These are the open, ports: ", open_ports)
