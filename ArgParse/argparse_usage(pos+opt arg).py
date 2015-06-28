import argparse

def fib(num):
    a,b=0,1
    for i in range(num):
        a,b=b,a+b
    return a


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("num",help="The Fibonacci number"+\
                              "you wish to calculate",type=int)
    parser.add_argument("-o","--option",help="Output the result"+\
                        "to the file.",action="store_true")     # action tells us that the argument is provided or not.
    args=parser.parse_args()
    result= fib(args.num)
    print "The "+str(args.num)+'th Fibonnaci no. is '+str(result)
    
    if args.option:
        f=open('fibonnaci.txt',"a")
        f.write(str(result)+'\n')
        
        
if __name__== '__main__':
    main()