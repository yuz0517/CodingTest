import sys

N,M,K = map(int,(input().split()))
listN=list(map(int,(input().split())))
listM=list(map(int,(input().split())))
NSum=[]
MSum=[]

for i in range(N):
    for j in range(i+1,N+1): 
        NSum.append(tuple(listN[i:j]))
        #print("print",i,j,listN[i:j])
for i in range(M):
    for j in range(i+1,M+1): 
        MSum.append(tuple(listM[i:j]))

common = set((NSum))&set((MSum))
maxlength=0
if len(common)==0:
    print(0)
else :
    for i in common:
        if maxlength <len(i):
            maxlength=len(i)
    print(maxlength)
#파이썬은 length가 아닌 len!!! list.length()가 아니라 len(list)   
#set(tuple)&set(tuple) => 튜플 형태로 결과가 나오며 겹치는 값들을 하나로  묶어줌 
#  미리 튜플로 만들어주고 쓸 것 !!!
#
