import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())
arr = [list(map(int, list(input().strip('\n')))) for _ in range(N)]

ans = 0
for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            continue
        if y == 0 or x == 0:
            value = 0
        else: 
            value = min(arr[y-1][x], arr[y][x-1], arr[y-1][x-1])
        arr[y][x] = value +1
        ans = max(value +1, ans)

print(ans **2 )


