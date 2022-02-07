import sys
ip = sys.stdin.readline

knight = ip()
x = ord(knight[0]) - ord('a') + 1
y = int(knight[1])


if x == 1 or x == 8 :
    if y == 1 or y == 8 :
        print(2)
    elif y == 2 or y == 7 :
        print(3)
    else :
        print(4)
elif x == 2 or x == 7 :
    if y == 1 or y == 8 :
        print(3)
    elif y == 2 or y == 7 :
        print(4)
    else :
        print(6)
else :
    if y == 1 or y == 8 :
        print(4)
    elif y == 2 or y == 7 :
        print(6)
    else :
        print(8)

