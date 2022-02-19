import sys
ip = sys.stdin.readline

# 좌표관련 문제여서 상하좌우 방향 미리 설정
direction = [[-1,0],[1,0],[0,-1],[0,1]]

# 가로세로 길이 입력
n,m = map(int,ip().split())

# 얼음틀 정보 입력
arr = []
for _ in range(n) :
    arr.append(list(map(int,ip().strip('\n'))))

# 방문유무 저장소
visited = [[False for _ in range(m)] for _ in range(n)]


def dfs(arr,visited,y,x):
    # 탐색 시에 방문처리 
    visited[y][x] = True
    
    # 상하좌우 탐색
    for dy, dx in direction :
        if 0 <= y+dy < n and 0 <= x+dx < m :
            # 입력이 0인 경우 + 방문하지 않은 곳일 경우 탐색
            if arr[y+dy][x+dx] == 0 and not visited[y+dy][x+dx] :
                dfs(arr,visited,y+dy,x+dx)

# 아이스크림 개수 count
cnt = 0

# 얼음틀을 전부 조사하여 입력이 0이거나 방문하지 않았으면 dfs 돌리기
for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 0 and not visited[i][j] :
            dfs(arr,visited,i,j)
            cnt += 1

# 출력
print(cnt)
