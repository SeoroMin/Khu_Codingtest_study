from collections import deque
import sys
ip= sys.stdin.readline

direction = [[-1,0],[1,0],[0,-1],[0,1]]
m,n = map(int,ip().split())
tomato=[[0 for _ in range(m)] for _ in range(n)]
queue = deque()

for i in range(n) :
    x = list(map(int,ip().split()))
    tomato[i]= x
    for j in range(m) :
        if tomato[i][j] == 1 :
            queue.append([i,j,0])



while queue :
    y,x,cnt = queue.popleft()
    for dy, dx in direction :
        if 0 <= y+dy < n and 0 <= x+dx < m :
            if tomato[y+dy][x+dx] == 0 :
                tomato[y+dy][x+dx] = 1
                queue.append([y+dy,x+dx,cnt+1])




ok = True
for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 0 :
            ok = False

if ok :
    print(cnt)
else :
    print(-1)
