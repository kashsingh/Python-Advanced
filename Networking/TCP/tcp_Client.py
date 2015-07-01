import socket

def main():
    host="172.20.2.200"
    port=5555
    
    s=socket.socket()
    s.connect((host,port))
    
    message=raw_input("->")
    
    while message!="q":
        s.send(message)
        print "Received from server: "+s.recv(1024)
        message = raw_input("->")
        
if __name__=="__main__":
    main()