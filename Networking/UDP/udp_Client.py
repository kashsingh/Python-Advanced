import socket

def main():
    host="127.0.0.1"
    port=5553
    
    server=("127.0.0.1",5555)
    
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    
    message=raw_input("->")
    
    while message!="q":
        s.sendto(message,server)
        data,addr=s.recvfrom(1024)
        print type(addr)
        print "Received from server: "+str(data)
        message = raw_input("->")
        
    s.close
        
if __name__=="__main__":
    main()