N=int(input())
flag=0
for i in range (2,N-1):
    if N%i==0:
        flag=1
        break
if flag==0:
    print("yes")
else:
    print("no")
        
