import sys
ip = sys.stdin.readline

# 가로세로 입력
n,m = map(int,ip().split())

maxx = 0

for _ in range(n) :
    # 각 행의 최솟값중 최댓값 n번갱신
    maxx = max(maxx, sorted(list(map(int,ip().split())))[0])


print(maxx)