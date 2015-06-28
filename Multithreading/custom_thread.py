import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self,text,out):
        threading.Thread.__init__(self)
        self.text=text
        self.out=out
    
    def run(self):
        f = open(self.out,"a")
        f.write(self.text+'\n')
        f.close()
        time.sleep(2)
        print "Finished writing to the file: "+ self.out


def main():
    message=raw_input("Enter a message to write to the file: ")
    background=AsyncWrite(message,"output.txt")
    background.start()      #Thread started.
    print "Program continues to run while writing to the file"
    background.join()       #This will pause the program until thread is compleated
    
    print "Wait until thread is compleated" 
    
if __name__=="__main__":
    main()
    