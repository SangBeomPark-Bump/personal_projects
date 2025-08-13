import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N, D = map(int, input().split())

arr = [list(map(int, input().split() ) ) for _ in range(N)]

dp = [i for i in range(D+1)]

for d in range(1, D+1):
    case1 = d
    for start, end, distance in arr:
        if d == end:
            case1 = min(case1, dp[start] + distance)
    case2 = dp[d-1] +1
    dp[d] = min(case1, case2)
# print(start, end, distance)

print(dp[-1])