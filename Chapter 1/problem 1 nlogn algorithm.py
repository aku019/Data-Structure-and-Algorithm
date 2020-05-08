def there():
    
    s=input()
    s2=sorted(s)
    
    c="No"
    for i in range(1,len(s2)):
        if(s2[i-1]==s2[i]):
            c="Yes"
            break
    
    print(c)
        
if __name__ == "__main__":
    t=int(input())
    for i in range(0,t):
        there()

        