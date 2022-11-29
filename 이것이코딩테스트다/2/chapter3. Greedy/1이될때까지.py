n,k = map(int, input().split())
num=0
if(n%k == 0):
  
  while(n != 1):
    n=(n/k)
    num=num+1
    
elif(n%k!=0) :
  while(n != 1):
    
    n=n-1
    num=num+1
print(num)  
