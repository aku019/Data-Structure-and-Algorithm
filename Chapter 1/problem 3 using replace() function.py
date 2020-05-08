
def there():
    
    s=input()
    s.strip() #to remove leading and trailing spaces
    s=s.replace(" ","/20")
    
    return(s)
    
    
        
if __name__ == "__main__":
    t=int(input())
    for i in range(0,t):
        print(there())

        