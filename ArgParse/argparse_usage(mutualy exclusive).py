"""Mutually exclusive arguments are those where you can select one option or other but not both.
   A group is needed to implement this. If both are tried to used an output is generated saying they cann't be used together."""
import argparse

def fib(num):
    a,b=0,1
    for i in range(num):
        a,b=b,a+b
    return a


def main():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group()
    
    group.add_argument("-v","--verbose",action="store_true")
    group.add_argument("-q","--quiet",action="store_true")
    
    parser.add_argument("num",help="The Fibonacci number"+\
                              "you wish to calculate",type=int)
                              
    parser.add_argument("-o","--option",help="Output the result"+\
                        "to the file.",action="store_true")     # action tells us that the argument is provided or not.
    args=parser.parse_args()
    result= fib(args.num)
    
    if args.verbose:
        print "The "+str(args.num)+'th Fibonnaci no. is '+str(result)
    elif args.quiet:
        print result
    else:
        print "Fib("+str(args.num)+') = '+str(result)
    
    if args.option:
        f=open('fibonnaci.txt',"a")
        f.write(str(result)+'\n')
        
        
if __name__== '__main__':
    main()