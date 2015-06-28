from threading import Thread
import time

def timer(name,delay,repeat):
    print "Timer: "+str(name)+ " Started "
    while repeat>0:
        time.sleep(delay)
        print name+": "+str(time.ctime(time.time()))
        repeat-=1
    print "Timer: "+str(name)+ " Completed"

def main():
    t1=Thread(target=timer,args=("Timer 1",1,5))
    t2=Thread(target=timer,args=("Timer 2",2,6))
    t1.start()
    t2.start()
    print("Main completed")
    
if __name__=="__main__":
    main()
    