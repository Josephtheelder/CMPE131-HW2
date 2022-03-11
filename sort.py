
def sort_list(num_list):
    
    n=len(num_list)
    
    i=0
   
    while(i<n):
        j=0
        
        while(j<n-i-1):
            
            if(num_list[j]>num_list[j+1]):
                temp=num_list[j]
                num_list[j]=num_list[j+1]
                num_list[j+1]=temp
              
            j=j+1
         
        i=i+1
     
    return num_list
    
num_list=[1,9,2,4,3,5]

ans=sort_list(num_list)

for i in ans:
    print(i,end=" ")
