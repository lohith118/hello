n=int(input("enter the value"))
b=0
while(n>0):
    d=n%10
    b=b*10+d
    n=n//10
print(b)    
