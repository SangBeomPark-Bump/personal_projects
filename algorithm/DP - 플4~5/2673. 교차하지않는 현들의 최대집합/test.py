import sys
input = sys.stdin.readline
INF = float("inf")
from collections import deque

N = int(input())
arr = [list(map(int, input().split() ) ) for _ in range(N)]
arr = [[start -1, end-1] for start, end in arr]
X = 100
e_arr = arr + [ i[::-1] for i in arr]
s_arr = sorted(e_arr, key= lambda x: x[1] - x[0] if x[1] > x[0] else x[1] - x[0] + X)


dp = [0 for _ in range(N*2)]
que = deque(s_arr)
snapshot = []

ans = 0
for i in range(N * 2): ## 100개
    start, end = que.popleft()

    if start > end:
        end += X

    snapshot.append([start, end, i])

    inner_dp = [0 for _ in range(end - start + 1)]
    for j in range(start+1, end +1): ### 100 개
        case1 = inner_dp[j-1 - start]
        case2 = 0
        for cs, ce, index in snapshot: ## 평균 50개
            if j == ce and start < cs :
                case2 = inner_dp[cs - start] + dp[index]
            if j - X == ce and start - X < cs:
                case2 = inner_dp[ cs - start + X ] + dp[index]
        inner_dp[j - start] = max(case1, case2)
    # print(inner_dp, start, end, end-start +1)
    

    dp[i] = inner_dp[-1] + 1

print(max(dp))