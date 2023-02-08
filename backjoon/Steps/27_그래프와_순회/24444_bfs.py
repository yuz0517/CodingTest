import sys
from collections import deque

 #### bfs 함수
def bfs(graph, start, visited,n):
  
  
  queue = deque([start])
  visited[start] = True
  count = [0] * (len(visited))
  
  #방문 순서 정보가 담겨있는 변수
  ordernum = 0; 
  while queue :
    #queue 의 맨 왼쪽을 POP 하고 
    v = queue.popleft()
    #방문 순서를 1 증가시킨 후 
    ordernum = ordernum+1
    #count 배열에 방문 순서를 기록한다. 
    count[v] = ordernum

    for i in graph[v]:
       #v 에서 연결되어있는 정점들을 체크한다.
       #만약에 정점 i들이 아직 visited 된 상태가 아니라면 
      if not visited[i]:
        #queue 에 i 를 추가시키고
        queue.append(i)
        #i 는 visited 됨.
        visited[i] = True
  #1부터 끝까지의 정점이 몇 번째로 방문되었는지 기록된 배열 원소들을 모두 출력.
  for i in range(1,n+1):
    print(count[i])
    
    
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
    #오름차순 정렬 해 주었다. (연결되어 있는 정점들 중 제일 작은 정점부터 방문하기위해)
    graph[i].sort()
  
visited = [False] * (int(n)+1)


bfs(graph, r, visited, n)
