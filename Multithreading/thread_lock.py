"""Like lock we can also use semaphores but unlike Locks we can specify no of threads that can acquire the lock at a time.
   Ex. If 10 threads running so we can permit 2-3 threads to acquire lock on the piece of data.  """
import threading 
import time

tLock=threading.Lock()

def timer(name,delay,repeat):
    print "Timer: "+str(name)+ " Started "
    tLock.acquire()
    print name+" Lock acquired"
    while repeat>0:
        time.sleep(delay)
        print name+": "+str(time.ctime(time.time()))
        repeat-=1
    tLock.release()
    print name+" lock released"
    print "Timer: "+str(name)+ " Completed"

def main():
    t1=threading.Thread(target=timer,args=("Timer 1",1,5))
    t2=threading.Thread(target=timer,args=("Timer 2",2,6))
    t1.start()
    t2.start()
    print("Main completed")
    
if __name__=="__main__":
    main()
    