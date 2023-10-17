N,M = map(int,input().split())
graph = []
for k in range(N):
  graph.append(list(map(int,input())))

def dfs(graph, n,m, visited):
  print("dfs",n,",",m)
  if n>=len(graph) or m>=len(graph[n]):
      print("n>=len(graph) or m>=len(graph[n]) 조건에 해당.종료")
      return
  
  if visited[n][m] == True: 
      print("visited[n][m]==True 조건에 해당. 종료")
      return
  elif n<0 or m<0: 
      print("n<0 or m<0 조건에 해당. 종료")
      return
  elif graph[n][m] == 1 :
      print("graph[n][m]==1 조건에 해당. 종료")
      return
  
  elif graph[n][m]==0 :
    visited[n][m] = True #현재 노드 V를 방문 처리
    print("graph[",n,"][",m,"] 는 0이며 아직 방문하지 않은 노드이기 때문에 이 노드에 대해 상하좌우 탐색한다. ") 
    dfs(graph, n,m-1,visited) #상
    dfs(graph, n,m+1,visited) #하
    dfs(graph, n-1,m,visited) #좌
    dfs(graph, n+1,m,visited) #우



# 이차원 배열을 만들고 False로 채우기
visited = [[False for _ in range(M)] for _ in range(N)]
ice=0
print("len(graph[0])",len(graph[0]))
print("len(graph)",len(graph))
for i in range(N):
  print("for i",i)
  for j in range(M):
    print("for j",j)
    if visited[i][j]==True:
        print("이미 방문된 노드이기 때문에 다음 항목으로 넘어갑니다")
        continue
    elif graph[i][j]== 0 and visited[i][j]==False :
      print("i,j",i,j,graph[i][j], visited[i][j])
      dfs(graph, i,j, visited) 
      ice=ice+1
      print("ice +1 되었습니다. 누적 ice의 개수는: ",ice)
      
    else:
      print("이 노드의 값은 1이기 때문에 다음 항목으로 넘어갑니다. ")
      continue
print("총 얼음 개수 ice: ",ice)


