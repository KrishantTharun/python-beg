x=int(input())
temp=x
ds=0
while x!=0:
    rem=x%10
    ds=ds+rem**3
    x=x//10
if temp==ds:
    print("yes")
else:
    print("no")
    
