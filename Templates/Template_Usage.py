'''Here are some points about templates:
   1. We can escape the delimiter by using it twice i.e. Template('I have $$0.') will output: "I have $0."   
   2. To attach a string at end of a placeholder you need to specify placeholder in {} i.e
        Eg. Template("This is our ${place}yard.") will output: "This is our shipyard."    '''

from string import Template

def main():
    cart=[]
    cart.append(dict(item="Coke",price=8,qty=3))
    cart.append(dict(item="Fish",price=32,qty=1))
    cart.append(dict(item="Cake",price=12,qty=2))
    
    t= Template("$qty * $item = $price")
    print "Cart:"
    total=0
    for data in cart:
        print t.substitute(data)        
        #in place of substitue() we could use safe_substitute() to handle any exceptions or error raised when the mentioned placeholder is missing.
        #Ex: Template($name has $money) can give output "Tim has $money" as 'money' placehoder was missing.
        total+=data['price']
    print "Total: "+str(total)  
    
    
if __name__=='__main__':
    main()