def func_counter(f):  
    def wrapped(y):
        wrapped.counter += 1
        return f
    wrapped.counter = 0
    return wrapped

@func_counter  
def foo(y):
    return y+2**3-34
    
y=int(input()) 
foo(y)
foo(y) 

print(foo.counter) 

