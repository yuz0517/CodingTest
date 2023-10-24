ar=list(input())
result=0
if len(ar)==1:
    result=1
else :
    N=int(len(ar)/2)

    for i in range(N):
        p = ar.pop()
        if ar[i]== p:
            result=1
        elif ar[i]!= p:
            result=0
            break
        


print(result)
