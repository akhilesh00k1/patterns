n=int(input())
k=0
half=(n+1)//2
for i in range(1,n+1):

    if i<=half:
        k+=1
    else:
        k-=1
             
    for j in range(1,n+1):
        if j >=half+1-k and j<=half-1+k:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
