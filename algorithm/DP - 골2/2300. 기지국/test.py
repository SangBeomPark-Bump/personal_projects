import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())
arr = [list(map(int, input().split() ) ) for _ in range(N)]
arr.sort(key= lambda x: x[0])

dp = [INF for _ in range(N+1)]
dp[0] = 0
for n in range(1, N+1):
    x, _ = arr[n-1]
    maxy = 0
    maxx = 0
    for k in range(0, n):
        curx, cury = arr[n-k-1]

        maxy = max(maxy, abs(cury) * 2)
        maxx = abs((curx - x))
        # if n == 4:
        #     print(maxx, maxy ,dp[n-k-1], max(maxx, maxy) + dp[n-k-1], k)
        # print(maxx, maxy, x, curx, k)
        dp[n] = min(dp[n], max(maxx, maxy) + dp[n-k-1])
    # print(dp)
    # if n == 4:
    #     break
print(dp[-1])