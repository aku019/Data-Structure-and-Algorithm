
def there():
    
    s=input()
    s1=input()
    n=len(s)
    m=len(s1)
    if(abs(n-m)>1):
        return False  #if difference of length b/w them is more than 1 then return false
   
    c=0#this is a flag to check if strings are equi length or not,c=0 for equal and c=1 for different lenght
    
    #this section is to determine the longer of the 2 strings , it's not necessary to do 
    #I did it to remove the overhead of writing more statments in loop
    if(n>m):
        c=1
        l=s
        sm=s1
    elif(n<m):
        
        c=1
        l=s1
        sm=s
    else:
        l=s1
        sm=s
    
    
    cn=0 #counter to count the distance b/w 2 strings
    i=0
    j=0
    while i<len(l) and j<len(sm):
        
        
        if(l[i]!=sm[j]):#if the characters are not same
            cn+=1 #update distance
            if(cn>1): #if distance more than 1(i.e. actually 2) then return false
                #print(1)
                return False
            if(c==0):#this says that both string are equal lenght so move ahead on both strings
                i+=1
                j+=1
            else: #if length is different move ahead in the shorter string
                i+=1
        else:
            i+=1
            j+=1
    
    if(cn>1):
        
        return False
        
    return True
    
    
            
        
        
        
       
       
    
    
    
        
if __name__ == "__main__":
    t=int(input())
    for i in range(0,t):
        print(there())

        