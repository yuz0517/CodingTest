#N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
N=input()
A=[]
A = list(map(int,input().split()))

Min = A[0]
Max = A[0]

for i in A:
    if int(Min)>int(i):
        Min = i
        
    if int(Max)<int(i):
        Max = i
        
print(Min,Max)
