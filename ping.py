import os

import sys


sys.ps1 = '\033[01;32m '
print(sys.ps1)

sys.ps2 = '\033[95m'

sys.ps3 = '\033[94m'

sys.ps4 = '\033[96m'

print('''

 ####### ######   #####   #####  
    #    #     # #     # #     # 
    #    #     #       #       # 
    #    ######   #####   #####  
    #    #   #         #       # 
    #    #    #  #     # #     # 
    #    #     #  #####   #####  
                                 


''')

s1 = input("Enter IP : ")

packet = input("Enter packet size : ")

os.system("ping "+s1+" -s "+packet)
