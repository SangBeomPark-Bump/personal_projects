import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


S, A, B, C = map(int, input().split())
dp = [[ [ [-1 for _ in range(C+1)] for _ in range(B+1)] for _ in range(A+1)] for _ in range(S+1)]
da = [-1, 0, 0, -1, -1, 0, -1]
db = [0, -1, 0, -1, 0, -1, -1]
dc = [0, 0, -1, 0, -1, -1, -1]

def dfs(a, b, c, s):
    if dp[s][a][b][c] != -1:
        return dp[s][a][b][c]
    temp = a+b+c

    if temp == 0:
        return 1
    
    if s == 0:
        return 0

    value = 0
    for i in range(7):
        na = a+ da[i]
        nb = b+ db[i]
        nc = c+ dc[i]
        ns = s-1
        if na<0 or nb < 0 or nc< 0 or ns < 0:
            continue

        value += dfs(na, nb, nc, ns)
    dp[s][a][b][c] = value
    return value

print(dfs(A, B, C, S))
