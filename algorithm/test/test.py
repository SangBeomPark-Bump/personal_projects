import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())

arr = [input().strip('\n') for _ in range(N)]

dp = [ [-1 for _ in range(M)] for _ in range(N)]

dx = 1
dy = [-1, 0, 1]

max_carrot = -1

for x in range(M):
    for y in range(N):

        if arr[y][x] == 'R':
            dp[y][x] =0

        if arr[y][x] == 'O':
            max_carrot = max(max_carrot, dp[y][x])

        cur_carrot = dp[y][x]
        if cur_carrot >=0:
            nx = x + dx
            for i in range(3):
                ny = y + dy[i]
                if nx < M and 0 <= ny < N:
                    if arr[ny][nx] == '#':
                        continue
                    is_carrot = arr[ny][nx] == 'C'
                    dp[ny][nx] = max(dp[ny][nx], cur_carrot + (1 if is_carrot else 0))



print(max_carrot)