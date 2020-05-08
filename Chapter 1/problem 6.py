
def there():
    
    s=input()
    
    comp="" #string to store the compresed string
    c=0 #for counter purpose
    
    for i in range(0,len(s)):
        if i!=0 and s[i]!=s[i-1]:
            comp+=s[i-1]+str(c)
            c=0
        c+=1
    
   #add the last character of string
   comp+=s[-1]+str(c)
    #return compressed string only if its length is smaller than original string
    if(len(comp)<len(s)):
        return comp;
    return s
    
            
        
        
        
       
       
    
    
    
        
if __name__ == "__main__":
    t=int(input())
    for i in range(0,t):
        s1=there()
        print(s1)

        