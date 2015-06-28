"""1. Unlike OptParse, if you wish to call a function with an option then 
   you must create a subclass argparse.Action, you must supply a __call__ method.(or simply use if statement)
   2. Argparse also take arguments into list using 'nargs' attribute you can use
      nargs="+" (when no. of arguments are unknown) or nargs=2 (when you no of arguments).  """
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
    args=parser.parse_args()
    result= fib(args.num)
    print "The "+str(args.num)+'th Fibonnaci no. is '+str(result)
if __name__== '__main__':
    main()
    