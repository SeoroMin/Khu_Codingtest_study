# 숫자 카드 게임

# 입력
# N M
# 1 2 3
# 4 5 6
# 7 8 9

N, M = map(int, input().split())

mins = []

for _ in range(N):  # 행의 개수 N만큼 반복해서 행 입력받기
    row = list(map(int, input().split()))
    mins.append(min(row))

max = max(mins)

print(max)