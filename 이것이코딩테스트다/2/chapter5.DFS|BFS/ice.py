N,M = map(int,input().split())
graph = []
for k in range(N):
  graph.append(list(map(int,input())))

def dfs(graph, n,m, visited):  
  if n>=len(graph) or m>=len(graph[n]):
      return
    
  if visited[n][m] == True: 
      return
  elif n<0 or m<0: 
      return
  elif graph[n][m] == 1 :
      return
  elif graph[n][m]==0 :
    visited[n][m] = True 
    dfs(graph, n,m-1,visited) 
    dfs(graph, n,m+1,visited) 
    dfs(graph, n-1,m,visited) 
    dfs(graph, n+1,m,visited) 


visited = [[False for _ in range(M)] for _ in range(N)]
ice=0

for i in range(N):
  for j in range(M):
    if visited[i][j]==True:
        continue
    elif graph[i][j]== 0 and visited[i][j]==False :
      dfs(graph, i,j, visited) 
      ice=ice+1
    else:
      continue
print(ice)

