import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(N)]
arr = [[0, 0]] + arr


dp = [ 0 for _ in range(N+1)]
for n in range(1, N+1):
    dp[n] = max(dp[n], dp[n-1])
    if n + arr[n][0] -1 <N+1:
        dp[n+arr[n][0] -1 ] = max(dp[n+arr[n][0] -1 ], dp[n-1]+ arr[n][1])
    print(dp)

# for i in arr:
#     print(i)