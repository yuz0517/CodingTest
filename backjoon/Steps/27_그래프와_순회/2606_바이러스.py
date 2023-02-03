from collections import deque


def bfs(graph, start, visited):

  
  queue = deque([start])
  visited[start] = True
  j = 0
 
  while queue :

    v = queue.popleft()

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        j = j+1

  print(j)

computer = int(input()) 
pair = int(input())


graph = [[0]*0 for i in range(computer+1)]

for i in range(pair) :
  a,b = input().split()
  
  a = int(a)
  b = int(b)
 
  graph[a].append(b)
  graph[b].append(a)


visited = [False] * (int(computer)+1)

bfs(graph, 1, visited)
