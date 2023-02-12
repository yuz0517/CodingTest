import sys
n = sys.stdin.readline()
 
arr  = []

for i in range(n+1):
  a,b = sys.stdin.readline().split()
  
  a = int(a)
  b = int(b)
  arr.append(a+b)

for i in range(n+1):
  print(arr)
