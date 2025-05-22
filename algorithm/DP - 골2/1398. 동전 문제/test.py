import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")



T = int(input())
dp = [INF for _ in range(100)]
dp[0] = 0

for n in range(1, 100):
    case1 = dp[n-1]
    case2 = INF
    case3 = INF
    if n>=10:
        case2 = dp[n-10]
    if n >= 25:
        case3 = dp[n-25]
    
    dp[n] = min(case1, case2, case3) +1

for _ in range(T):
    N = int(input())
    ans = 0
    while N:
        ans += dp[N %100]
        N //= 100
    print(ans)


# for i in arr:
#     print(i)