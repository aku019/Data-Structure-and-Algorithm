from collections import Counter 
#(From GFG)Once initialized, counters are accessed just like dictionaries. 
#Also, it does not raise the KeyValue error (if key is not present) instead the value’s count is shown as 0.

def there():
    
    s=input()
    s1=input()
    s_dict=Counter(s)
    print(s_dict) #you can see it here how counter works
    s1_dict=Counter(s1)
    print(s1_dict)
    
    return s_dict==s1_dict
    
    
        
if __name__ == "__main__":
    t=int(input())
    for i in range(0,t):
        print(there())

        