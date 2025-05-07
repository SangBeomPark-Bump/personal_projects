import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N, M = map(int, input().split())

arr = [list(map(int, list(input().strip('\n')))) for _ in range(N)]
dp = [[ [0, 0] for _ in range(M)] for _ in range(N) ]

def left(y, x):
    if y > N-1 or x<0:
        return 0
    
    if arr[y][x] == 0:
        return 0 

    if dp[y][x][0]:
        return dp[y][x][0]
    

    dp[y][x][0] = left(y+1, x-1) + 1
    return dp[y][x][0]

def right(y, x):
    if y > N-1 or x>M-1:
        return 0
    
    if arr[y][x] == 0:
        return 0 

    if dp[y][x][1]:
        return dp[y][x][1]
    

    dp[y][x][1] = right(y+1, x+1) + 1
    return dp[y][x][1]

for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            left(y, x)
            right(y, x)

value = 0
for n in range(N):
    for m in range(M):
        factor = min(dp[n][m][0], dp[n][m][1])
        for small_factor in range(factor-1, -1, -1):
            if small_factor < value-1:
                break
            if n + small_factor < N and m - small_factor>=0 and m + small_factor <M:
                case1 = dp[n+small_factor][m-small_factor][1]
                case2 = dp[n+small_factor][m+small_factor][0]
                if min(case1, case2) >= small_factor+1:
                    value = max(small_factor+1, value)
print(value)