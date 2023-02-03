#출처: 이것이 코딩테스트다 147페이지 
from collections import deque

#BFS메서드 정의 
def bfs(graph, start, visited):
  #큐 구현을 위해서 deque 라이브러리 사용
  queue = deque([start])
  
  #현재 노드인 start를 방문처리
  visited[start] = True
  
  #queue가 빌 때까지 반복
  while queue :
    # 큐에서 하나의 원소를 뽑아서 출력
    v = queue.popleft()
    print(v, end='')
    # 해당 원소와 연결되어있고 && 아직 방문되지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

#노드 연결 정보를 그래프로  표현(2차원)
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

#노드 방문 정보를 리스트 자료형으로 표현(1차원)
visited = [False] * 9
#정의된 BFS 함수 호출
bfs(graph, 1, visited)
