
def there():
    
    s=input()
    s1=input()
    if(len(s)!=len(s1)):
        return "No";
        
    
    
    j=ord(s[0])^ord(s1[0])
    
    for i in range(1,len(s)):
        k=ord(s[i])
        k1=ord(s1[i])
        j=j^k^k1
    
    
    if(j==0):
        return "Yes"
    return "No"
    
    
        
if __name__ == "__main__":
    t=int(input())
    for i in range(0,t):
        print(there())

        