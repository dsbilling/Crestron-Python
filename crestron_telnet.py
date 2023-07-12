'''
crestron_telnet.py
Author: Daniel S. Billing (daniel@kilobyte.no)
--------------------------------------------------------------------
Simple Python telnet script for connecting to Crestron and typing commands. This can be expanded to be used as an automation script for getting and setting settings.
'''
import socket, select, string, sys
 
#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage: python crestron_telnet.py hostname port'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # Connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host'
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            # Incoming message from the remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print 'Connection closed'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
             
            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
