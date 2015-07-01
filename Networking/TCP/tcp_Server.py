import socket

def main():
    s=socket.socket()
    host="127.0.0.1"
    port=5555
    s.bind((host,port))
    
    s.listen(1)
    print "Waiting for a connection..."
    c,addr=s.accept()
    print "Connection Received from: "+str(addr)
    
    while True:
        data=c.recv(1024)
        
        if not data:
            print "Connection ended!!"
            break
            
        print "Data Recieved: "+ str(data)
        ans="Data received correctly"
        
        c.send(ans)
    c.close         # To close the socket
    
if __name__=="__main__": 
        main()