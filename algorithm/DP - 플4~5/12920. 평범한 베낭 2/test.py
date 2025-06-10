import sys
input = sys.stdin.readline
INF = float("inf")

import math
def decomposer(num):
    arr = []

    factor = math.floor(math.log(num, 2))

    for i in range(factor):
        arr.append( 2 ** i)
    
    arr.append(num - (2 ** factor) +1)
    return arr

N, M = map(int, input().split())
arr = [list(map(int, input().split() ) ) for _ in range(N)]

s_arr = []

for v, c, k in arr:
    cur_arr = decomposer(k)

    for i in cur_arr:
        s_arr.append([v*i, c*i])

adjusted_n = len(s_arr)

dp = [[0 for _ in range(M+1)] for _ in range(adjusted_n+1)]


for i in range(adjusted_n):
    v, c = s_arr[i]
    for m in range(1, M+1):
        case1 = dp[i+1][m-1]
        case2 = 0
        if m >= v:
            case2 = dp[i][m-v] + c
        case3 = dp[i][m]
        dp[i+1][m] = max(case1, case2, case3)

print(dp[-1][-1])