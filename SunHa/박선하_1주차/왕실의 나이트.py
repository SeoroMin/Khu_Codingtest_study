# 왕실의 나이트

# 입력
# a1

start = input()
m, n = ord(start[0]), int(start[1])

col = [chr(i) for i in range(97,105)]
row = list(range(1, 9))

check = []
move1 = [-2, +2, -2, +2]
move2 = [+1, -1]
direction = ["U", "D", "L", "R"]


# for i in range(4):  # 상하좌우 네 방향으로 두 칸
#     if i < 2:
#         k = n
#         k += move1[i]
#         if 1 <= k <= len(row):
#             check.append(direction[i])
#     else:
#         k = m
#         k += move1[i]
#         if ord("a") <= k <= ord("a") + len(col) - 1:
#             check.append(direction[i])
    

cnt = 0

for i in range(4):  # 상하좌우 네 방향으로 두 칸
    if i < 2:
        tmp1 = n
        tmp1 += move1[i]
        if 1 <= tmp1 <= len(row):  # 상하
            for j in range(2):
                tmp2 = m
                tmp2 += move2[j]
                if ord("a") <= tmp2 <= ord("a") + len(col) - 1:    # 좌우
                    cnt += 1
    else:
        tmp1 = m
        tmp1 += move1[i]
        if ord("a") <= tmp1 <= ord("a") + len(col) - 1:    # 좌우
            for j in range(2):
                tmp2 = n
                tmp2 += move2[j]
                if 1 <= tmp2 <= len(row):  # 상하
                    cnt += 1

print(cnt)