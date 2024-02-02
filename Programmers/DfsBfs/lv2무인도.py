#https://school.programmers.co.kr/learn/courses/30/lessons/154540
import sys 
sys.setrecursionlimit(10000)#<-- 재귀 한도 설정. 안 써줬을 때 테스트 케이스 절반에서 오류 났었는데 써주니까 해결됨.
#dfs,bfs 문제 풀 때 이걸 쓰고 시작하는게 좋다는 글을 봤다. 

global my_sum #합계를 저장할 전역 변수 선언

def dfs(i, j, maps, arr):
    global my_sum
    
    if i < 0 or j < 0 or i >= len(maps) or j >= len(maps[0]) or arr[i][j] == 1 or maps[i][j] == 'X':
        return
    elif arr[i][j] == 0:
        arr[i][j] = 1
        my_sum += int(maps[i][j])  # maps의 값을 정수로 변환하여 더해줌. 
        
        # 상 
        dfs(i - 1, j, maps, arr)
        # 하
        dfs(i + 1, j, maps, arr)
        # 좌
        dfs(i, j - 1, maps, arr)
        # 우
        dfs(i, j + 1, maps, arr)

def solution(maps):
    global my_sum
    sum_arr = []
    a = len(maps)
    b = len(maps[0])
    arr = [[0] * b for _ in range(a)]
    answer = []
    
    for i in range(a):
        for j in range(b):
            my_sum = 0
            
            if maps[i][j] == 'X':
                continue
            else:
                if arr[i][j] == 0:
                    dfs(i, j, maps, arr)
                    if my_sum == 0:
                        continue
                    else: 
                        sum_arr.append(my_sum)
    
    
    if len(sum_arr)==0:
        sum_arr.append(-1)
    else :
        sum_arr.sort()
    return sum_arr
