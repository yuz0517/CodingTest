N,M =map(int,input().split())
ilist=[]
result = [0]*N
for k in range(M):
    ilist.append(list(map(int,input().split())))


for i in range(M):

    for j in range(ilist[i][0]-1,ilist[i][1]):

        result[j] = ilist[i][2]


for i in result:
    print(i, end=' ')
