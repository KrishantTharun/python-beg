N=int(input())
t=N
temp=0
while t!=0:
    temp=temp*10+t%10
    t=t//10
if N==temp:
    print("yes")
else:
    print("no")
        
