import socket

def main():
    host="127.0.0.1"
    port=5555
    
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)       #DGRAM is for UDP (User Datagram Protocol)
    s.bind((host,port))
    
    
    print "Waiting for a connection..."
      
    while True:
        data,addr=s.recvfrom(1024)
        print type(addr)
        print "message from: "+str(addr)
        print "from connected user: "+ str(data)
        data=str(data).upper
        s.sendto(data,addr)
    s.close         # To close the socket
    
if __name__=="__main__": 
        main()