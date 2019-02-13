N,M=map(int,input().split( ))
for i in range(N+1,M):
    if i%2==0:
        print(i,end=" ")
        i+=1
