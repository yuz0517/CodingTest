#dfs를 recursion으로 구현 -> boj 에서 런타임 에러 남. 재귀를 쓰지 않고 구현해야함
import sys
from collections import deque

global ordernum  
ordernum = 0
def dfs(graph, start, visited,n,count):
  
  global ordernum
  queue = deque([start])
  visited[start] = True
  queue.append(start)

  ordernum += 1
  count[start] = ordernum
      
 
    if not visited[i]:
   
      visited[i] = True
      
   
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

for i in range(n+1):
    graph[i].sort()
visited = [False] * (int(n)+1)
count = [0] * (len(visited))

dfs(graph, r, visited, n,count)

for i in range(1,n+1):
  print(count[i])
