import sys
from collections import deque
ip = sys.stdin.readline

# 좌표문제니까 방향 미리 설정
direction = [[-1,0],[1,0],[0,-1],[0,1]]

# 가로세로 입력
n,m = map(int,ip().split())

# 미로형태 입력
arr = []
for _ in range(n) :
    arr.append(list(map(int,ip().strip('\n'))))

# 방문처리 저장소
visited = [[False for _ in range(m)] for _ in range(n)]


def bfs(arr,visited, y, x):
    
    # BFS 니까 queue 이용
    queue = deque()

    # 초기값 queue에 넣어주기
    queue.append([y,x,1])
    visited[y][x] = True

    while queue :
        ny, nx, cnt = queue.popleft()

        # 종료조건
        if ny == n-1 and nx == m-1 :
           return cnt 
        
        # 죄표에 따른 반복문과 조건문
        for dy, dx in direction :
            if 0 <= ny + dy < n and 0 <= nx + dx < m :
            
                # Queue에 append하는 조건 (탐색 할지말지를 결정)
                if arr[ny+dy][nx+dx] == 1 and not visited[ny+dy][nx+dx] :
                    queue.append([ny+dy,nx+dx,cnt+1])
                    visited[ny+dy][nx+dx] = True


print(bfs(arr,visited,0,0))
