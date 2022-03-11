import time

def calculate_time(func):
   def inner1():
    
        begin = time.time()
    
        timer()
        
        end = time.time()
     
        print("Total time ",end - begin)
    return inner1

def timer():
    time.sleep(2)

function_to_be_used = calculate_time(timer)
 
function_to_be_used()
