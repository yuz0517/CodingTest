import sys
n = sys.stdin.readline()
n = int(n)
arr  = []

for i in range(n):
  a,b = sys.stdin.readline().split()
  
  a = int(a)
  b = int(b)
  arr.append(a+b)

for i in range(n):
  print(arr[i])
