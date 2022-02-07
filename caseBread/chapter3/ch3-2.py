import sys
ip = sys.stdin.readline

#입력부분
n, m, k = map(int,ip().split())
arr = list(map(int,ip().split()))

#값 정렬 (가장큰수와 두번째로큰수 찾기위함)
arr.sort()

res = 0

# m번반복
for i in range(1,m+1) :

    # 한 수를 k번 반복시 두번째로 큰수로 갈아탐
    if (i % k == 0) :
        res += arr[-2]

    # ...
    else :
        res += arr[-1]

print(res)