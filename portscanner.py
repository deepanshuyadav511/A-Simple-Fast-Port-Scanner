import socket
import sys
import threading
import pyfiglet    #For fonts
from datetime import datetime
             
art = pyfiglet.figlet_format("PORT SCANNER")
print(art)
print( " "*45 + " - BY DEEPANSHU YADAV" + "\n")

print( "NOTE: For multiple targets, seperate them with ','" + "\n")
##################
#FUNCTIONS
################## 
#Getting service names from the port number using getsercbyport() of python's socket module

def service_on_port(port_number, protocol):
    service_name = socket.getservbyport(port_number, protocol)
    return service_name

#Function scanning one ip address and one port only
def scan_port(ip_address,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_address,port))
        service = service_on_port(port,"tcp")     #service running on the port
        print(f"[+] Port Opened {port}: {service}")
        sock.close()
    except:
        print(f"[-] Port Closed {port}")
        
#Function that scans multiple ports by looping over the function scan_port()
def scan(target,start_port,end_port):
    print("-"*50)
    print("Scanning Target: {}".format(target))
    print("Scanning started at: {}".format(start_time))
    print("-"*50)
    print("\n*****OPEN PORTS*****" + "\n") #open port message
    for x in range(start_port,end_port + 1):
        thread = threading.Thread(target = scan_port, args = (target,x,))
        thread.start()
 
usage = "SYNTAX: python file_name TARGETS START_PORT END_PORT"

#check what time the scan started
start_time = datetime.now()

if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

#Terminal arguments
targets = sys.argv[1] 
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

#check if there are multiple targets specified by the user
if ',' in targets:
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), start_port,end_port)
else:
    scan(targets,start_port,end_port)

#Checking the time again
end_time = datetime.now()

#Calculates the difference of time to see how long it took to run the script
print("Time elapsed",end_time - start_time,2,"s") #prints time eclapsed

print("\n*****CLOSED PORTS*****\n") #closed port message
