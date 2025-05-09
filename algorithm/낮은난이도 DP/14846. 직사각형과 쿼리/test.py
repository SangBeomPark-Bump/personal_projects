import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = [[0 for _ in range(N+1)]] + [ [0] + list(map(int, input().split() ) ) for _ in range(N)]

dp = [ [ [0 for _ in range(10)] for _ in range(N+1)] for _ in range(N+1)]
for y in range(1, N+1):
    for x in range(1, N+1):
        cur_num = arr[y][x]-1
        for i in range(10):
            dp[y][x][i] = dp[y-1][x][i] + dp[y][x-1][i] - dp[y-1][x-1][i]
        dp[y][x][cur_num] +=1

def ans(y1, x1, y2, x2):
    temp = 0
    for i in range(10):
        if (dp[y2][x2][i] - dp[y1-1][x2][i] - dp[y2][x1-1][i] + dp[y1-1][x1-1][i]) > 0:
            temp+=1
    return temp

M = int(input())

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(ans(y1, x1, y2, x2))