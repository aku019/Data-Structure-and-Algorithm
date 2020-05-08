def there():
    
    s=input()
    a={}
    
    c="No"
    for i in s:
        if i in a:
            c="Yes"
            break
        else:
            a[i]=1
    
    print(c)
        
if __name__ == "__main__":
    t=int(input())
    for i in range(0,t):
        there()

        