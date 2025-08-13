import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

dp = [ [-INF for _ in range(N+1)] for _ in range(N+1)]
dp[0][0] = 0
for n in range(1, N * 2+1):
    for b in range( max(0, n-N) ,min(n, N) + 1):
        a = n - b
        case1 = -INF
        case2 = -INF
        case3 = -INF
        if a>0:
            case1 = dp[a-1][b]
        if b>0:
            case2 = dp[a][b-1]
        if a>0 and b>0:
            if A[a-1] > B[b-1]:
                case3 = dp[a-1][b-1] + 2
            elif A[a-1] == B[b-1]:
                case3 = dp[a-1][b-1] + 1
        dp[a][b] = max(case1, case2, case3)
print(dp[-1][-1])



# for i in arr:
#     print(i)