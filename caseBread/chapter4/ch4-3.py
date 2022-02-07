import sys
from collections import deque
ip = sys.stdin.readline

direction = [[0,1],[0,-1],[1,0],[-1,0]]

n,m = map(int,ip().split())
x0, y0, start = map(int,ip().split())

visited = [[False for _ in range(m)] for _ in range(n)]
arr = []


for _ in range(n) :
    arr.append(list(map(int,ip().split())))

cnt = 0
queue = deque()
queue.append([y0,x0])
while queue :
    y,x = queue.popleft()
    visited[y][x] = True
    for dy, dx in direction :
        if arr[y+dy][x+dx] == 0 and not visited[y+dy][x+dx] :
            queue.append([y+dy,x+dx])
            
    cnt += 1

print(cnt)