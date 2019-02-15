N=int(input())
x=list(map(int,input().split()))
y=sorted(x)
for i  in range(1,len(x)):
    print(*y,sep=' ')
    break
