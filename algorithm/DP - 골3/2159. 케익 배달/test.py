import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(N+1)]
next_move = [(0,0), (1, 0), (-1, 0), (0, -1), (0,1)]

INF = float("INF")
dp = [[INF for _ in range(5)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    y, x = arr[i]
    prevy, prevx = arr[i-1]

    for j in range(5):
        dy, dx = next_move[j]
        ny = y + dy
        nx = x + dx

        for prevj in range(5):
            pdy, pdx = next_move[prevj]
            pny = prevy + pdy
            pnx = prevx + pdx

            dp[i][j] = min( dp[i][j], dp[i-1][prevj] + abs(pny - ny) + abs(pnx - nx))
    # print(dp[i])
print(min(dp[-1]))