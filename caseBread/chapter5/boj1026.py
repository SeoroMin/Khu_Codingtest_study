from collections import deque
import sys
ip= sys.stdin.readline

n = int(ip())

first = list(map(int,ip().split()))
second = list(map(int,ip().split()))

first.sort()
second.sort(reverse=True)

result = 0
for i in range(n) :
    result += first[i]*second[i]

print(result)
