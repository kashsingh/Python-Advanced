from string import Template

class MyTemplate(Template):
    delimiter="#"   #Here default delimiter '$' is changed. Thus our new delimiter is "#" as we override the Template class variable.

def main():
    cart=[]
    cart.append(dict(item="Coke",price=8,qty=3))
    cart.append(dict(item="Fish",price=32,qty=1))
    cart.append(dict(item="Cake",price=12,qty=2))
    
    t= MyTemplate("#qty * #item = #price")
    print "Cart:"
    total=0
    for data in cart:
        print t.substitute(data)        
        total+=data['price']
    print "Total: "+str(total)  
    
    
if __name__=='__main__':
    main()