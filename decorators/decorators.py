def decorator(func):
    
    def wrapper(a,b): #args and kwargs helps us to use all the arguments of func
        if(a<b):
            a,b = b,a 
        
        return func(a,b)
        
    return wrapper
def divide(a,b):
    print(a/b)

instance_one =  decorator(divide)
instance_one(80,40)
