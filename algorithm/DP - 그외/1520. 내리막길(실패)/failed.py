import sys
sys.setrecursionlimit(10000)

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)



def solve(y, x):
    # 종료 조건
    if y == M-1 and x == N-1:
        return 1

    # # 메모이제이션
    # if dp[y][x] != -1:
    #     return dp[y][x]

    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not (0 <= ny < M and 0 <= nx < N):
            continue

        if arr[ny][nx] < arr[y][x]:
            dp[y][x] += solve(ny, nx)
    return dp[y][x]

print(solve(0, 0))
