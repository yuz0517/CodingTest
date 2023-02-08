import sys
from collections import deque

global ordernum  
ordernum = 0
def dfs(graph, start, visited,n,count):
  
  global ordernum
  queue = deque([start])

  queue.append(start)

  
      
  while(queue):
   
    i = queue.pop()


    if not visited[i]:

      visited[i] = True

      ordernum += 1
      count[i] = ordernum
      graph[i].sort(reverse=True)
      queue.extend(graph[i])
   
  #print(queue)
 
#n: 정점 , m: 간선, r: 시작정점

    
n,m,r = sys.stdin.readline().split()
n = int(n)
m = int(m)
r = int(r)

#빈 이차원 배열 선언
graph = [[0]*0 for i in range(n+1)]

for i in range(m) :
  a,b = sys.stdin.readline().split()
  
  a = int(a)
  b = int(b)
 
  graph[a].append(b)
  graph[b].append(a)


visited = [False] * (int(n)+1)
count = [0] * (len(visited))

dfs(graph, r, visited, n,count)

for i in range(1,n+1):
  print(count[i])
