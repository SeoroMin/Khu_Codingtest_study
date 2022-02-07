# 게임 개발

# 입력
# 4 4       # 4 x 4 맵
# 1 1 0     # (1,1)에 북쪽(0)을 바라보고 있음
# 1 1 1 1   # 0: 육지 / 1: 바다
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

N, M = map(int, input().split())
A, B, d = map(int, input().split())

game_map = []
direction = [0, 1, 2, 3]

for _ in range(N):  # 육지/바다 정보를 맵 리스트에 저장
    temp_map = list(map(int, input().split()))
    game_map.extend(temp_map)

visit_map = [None] * len(game_map)
visit_map[A * M + B] = 1    #visit

cnt = 0

while True:
    if d == 0:
        X = A
        Y = B - 1
    elif d == 1:
        X = A - 1
        Y = B
    elif d == 2:
        X = A
        Y = B + 1
    elif d == 3:
        X = A + 1
        Y = B

    # (1)왼쪽 칸이 맵 안에 있는 경우에 대해서 (2)한번 갔던 곳이 아니고 (3)육지라면
    if 0 <= X < N and 0 <= Y < M \
        and visit_map[X * M + Y] == None \
            and game_map[X * M + Y] == 0:   
                d = direction[d - 1]   # 왼쪽칸을 바라보게 회전하고,
                A = X   # 그 위치로 이동하자.
                B = Y
                cnt = 0
                visit_map[A * M + B] = 1    # 방문한 곳은 방문리스트에 기록
    else:   # 왼쪽칸으로 이동하지 못하는 경우
        d = direction[d - 1]   # 왼쪽칸을 바라보게 회전
        cnt += 1    # 네 방향 모두 가지 못하는 곳인지 체크하기 위해서 카운트

    if cnt == 4:
        if d == 0:  
            X = A + 1
            Y = B
        elif d == 1:
            X = A
            Y = B - 1
        elif d == 2:
            X = A - 1
            Y = B
        elif d == 3:
            X = A
            Y = B + 1
        
        # 캐릭터 뒤에 있는 칸(X, Y)이 바다가 아닌 이상 백스텝으로 뒤로 갈 것
        if game_map[X * M + Y] == 0:
            A = X
            B = Y
            cnt = 0
            visit_map[A * M + B] = 1
        else:   # 바다라면
            break

print(visit_map.count(1))


# if 0 <= X <= N & 0 <= Y <= M:   # 왼쪽 칸이 맵 안에 있는 경우에 대해서
#         if visit_map[X * M + Y] != None:    # 한번 갔던 곳이 아니고
#             if game_map[X * M + Y] == 0:    # 육지라면
#                 A = X   # 그 위치로 이동하자.
#                 B = Y
#                 visit_map[A * M + B] = 1    # 방문한 곳은 방문리스트에 기록
#     else:   # 왼쪽칸으로 이동하지 못하는 경우
#         d = direction[d - 1]   # 왼쪽칸을 바라보게 회전
#         cnt += 1    # 네 방향 모두 가지 못하는 곳인지 체크하기 위해서 카운트