import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M, K = map(int, input().split())

arr = [list(input().strip('\n')) for _ in range(N)]

ans = input().strip('\n')

end = len(ans)
temp = []
for dy in range(-K, K+1):
    if dy != 0:
        temp.append((dy, 0))
for dx in range(-K, K+1):
    if dx !=0:
        temp.append((0, dx))


dp = [[ [ 0 for _ in range(M)] for _ in range(N)] for _ in range(end)]

wow = 0
for i in range(end):
    letter = ans[-i-1]
    for y in range(N):
        for x in range(M):
            if arr[y][x] == letter:
                if i == 0:
                    dp[0][y][x] = 1
                else:
                    dp[i][y][x] = 0
                    for dy, dx in temp:
                        ny = y + dy
                        nx = x + dx
                        if ny >= N or ny < 0 or nx >= M or nx<0:
                            continue
                        dp[i][y][x] += dp[i-1][ny][nx]
                    if i == end-1:
                        wow += dp[i][y][x]
print(wow)