
def there():
    
    s=input()
    m={} #a dictionary to store the character and it's count
    n=len(s)
    for i in s:
        if i in m:
            m[i]+=1
        else:
            m[i]=1
    
    c=0 #to keep count of characters who occur once
    
    for i in m.values():
        if(i%2!=0):
            c+=1
        if(c>1):
            return False #in any case(odd or even) the count of odd charcters can't exceed 1
    if(n%2==0 and c==0): #if the string is even length then no character should occur odd times for palindrome
        return True
    if(n%2!=0 and c==1): #if string's length is odd then one character can occur for odd number of times
        return True
    
    return False
    
    
    
        
if __name__ == "__main__":
    t=int(input())
    for i in range(0,t):
        print(there())

        