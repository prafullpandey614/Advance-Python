import functools

def my_decorators(func):
    @functools.wraps(func) #using functools to keep the identitiy of wrapped function safe
    def wrapper(*args,**kwargs):
        print("Start")
        result = func(*args,**kwargs)
        print("Ends")
        return result
    return wrapper

@my_decorators
def add(x):
    return x+5;

print(add.__name__)
print(add(10))
