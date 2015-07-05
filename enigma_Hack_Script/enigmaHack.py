def buildCache(seq, c,s):
    cache = [[0 for j in range(s+c)] for i in range(s+2)]
    for i in range(s):
        cache[0][i] = seq[i]
 
    #build
    for order in range(1, s):
        for idx in range(s-order):
            cache[order][idx] = cache[order-1][idx+1]-cache[order-1][idx]
     
    for idx in range(1,1+c):
        cache[s-1][idx] = cache[s-1][0]
         
    #add next sequences to all levels
    for order in range(s-2,-1,-1):
        for idx in range(s-order, s-order+c):
            cache[order][idx] = cache[order][idx-1]+cache[order+1][idx-1]
    
    for e in cache[0][s:s+c+1]:
        print e ,
    print ''   
         
def solve():
    try:
        print "Enter no. of elements and no of next elements you need seprated by a space: Eg. ""6 4"" "
        s,c = list(map(int, raw_input().split()))
        print "Enter the elements in sequence seprated by space: Eg. ""2 4 5 6 7 8"" "
        seq = list(map(int, raw_input().split()))
        buildCache(seq, c,s)
    except:
        print "Wrong Input... \n Now exiting.."

if __name__== "__main__":        
    solve()