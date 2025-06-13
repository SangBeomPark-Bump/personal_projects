import sys
input = sys.stdin.readline
INF = float("inf")


N, L = map(int, input().split())

arr = [list(map(int, input().split() ) ) for _ in range(N)]

dydx = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if i == j == 0:
            continue
        dydx.append((i, j))

dp = [ [ [ [[0 for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(L+1)]
for i in range(N):
    for j in range(N):
        dp[1][i][j][i][j] = 1

        if L >= 2:
            for dy, dx in dydx:
                ey = i + dy
                ex = j + dx

                if ey<0 or ex < 0 or ey >=N or ex >=N:
                    continue
                if arr[i][j] == arr[ey][ex]:
                    dp[2][i][j][ey][ex] += 1

# starty, startx = 0, 1
for l in range(L%2+2, L+1, 2): # L//2번

    for starty in range(N): ## N번
        for startx in range(N): ## N번
            for dy, dx in dydx: ## 8번
                msy = starty + dy
                msx = startx + dx

                if msy < 0 or msy>= N or msx<0 or msx >=N:
                    continue

                for mey in range(N): ## N번
                    for mex in range(N): ## N번
                        if not dp[l-2][mey][mex]:
                            continue


                        for edy, edx in dydx: ## 8번
                            ey = edy + mey
                            ex = edx + mex

                            if ey < 0 or ey >= N or ex<0 or ex >=N:
                                continue
                
                            if arr[starty][startx] == arr[ey][ex]:
                                dp[l][starty][startx][ey][ex] += dp[l-2][msy][msx][mey][mex]


ans = 0

for sy in range(N):
    for sx in range(N):
        for ey in range(N):
            for ex in range(N):
                ans += dp[-1][sy][sx][ey][ex]
print(ans)