# 큰 수의 법칙

# 입력
# N M K
# 1 2 3 4 5 ... N

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse = True)  # 내림차순 정렬

large_sum = 0
add = 0
cnt = 0

# 어차피 array에서 0번째, 1번째 인덱스만 사용
max = arr[0]
max2 = arr[1]

# 한 사이클에서 더하기 1회 시행
while True:
    if add >= M:    # M번 다 더했으면 그만 더하자
        break
    # 더하기 수행 근데 더하는 숫자는 경우에 따라 다름
    if max > max2:
        if cnt < K:
            large_sum += max
            cnt += 1
        else:
            large_sum += max2
            cnt = 0
        add += 1
    else:   # 내림차순 정렬이므로 arr[0] == arr[1]
        large_sum += max
        add += 1

print(large_sum)