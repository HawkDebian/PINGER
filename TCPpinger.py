import socket
import sys
import os
import datetime
import time
import random





os.system('clear || cls')




sys.ps1 = '\033[01;32m '
print(sys.ps1)


print('''

████████╗██╗  ██╗███████╗██████╗ ███████╗██████╗ ██╗ █████╗ ███╗   ██╗
╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗████╗  ██║
   ██║   ███████║█████╗  ██║  ██║█████╗  ██████╔╝██║███████║██╔██╗ ██║
   ██║   ██╔══██║██╔══╝  ██║  ██║██╔══╝  ██╔══██╗██║██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗██████╔╝███████╗██████╔╝██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                      

                                  
                                                                        
''')



target = input("Hostname : ")

port = int(input("TCP Port : "))

i = 0
def ping(port):
    ms = int(round(time.time() * 1000))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
    if s.connect_ex((target, port)):
        print("Request time-out / offline")
        
        s.close()
    else:
        print(f"Reply from {target}: icmp_seq={i} time={ms} ms")
        s.close()
    


while True:
    ping(port)
    i += 1
    l = ['\033[01;32m', '\033[95m', '\033[96m', '\033[94m', '\033[91m']
    l2 = random.choice(l)
    print(l2)
             
