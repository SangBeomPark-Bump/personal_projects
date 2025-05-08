import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
arr = [list(map(int, input().split() ) ) for _ in range(N)]


dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for y in range(N):
    for x in range(1, N):
        hor, ver, diag = dp[y][x]

        temp = [False] * 3
        if x+1 < N :
            temp[0] = arr[y][x+1] == 0
            dp[y][x+1][0] += hor + diag if temp[0] else 0


        ### 다음상태 일어서기가 가능하다면
        if y+1 < N :
            temp[1] = arr[y+1][x] ==0
            dp[y+1][x][1] += ver + diag if temp[1] else 0


        ### 다음상태 대각선이 가능한가?
        if temp[0] and temp[1]:
            temp[2] = arr[y+1][x+1] == 0
            dp[y+1][x+1][2] += hor + ver + diag if temp[2] else 0

print(sum(dp[N-1][N-1]))