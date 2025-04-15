import sys
input = sys.stdin.readline
verbose = False
verboses = [True for _ in range(10)]

N = int(input())
arr = [int(input()) for _ in range(N)]
arr = [0] + arr


def wine():
    dp = [ [0] * 4 for _ in range(N+1)]
    dp[1] = [0, 0, arr[1], arr[1]]
    for n in range(2, N+1):
        dp[n] = [ max(dp[n-2]), max(dp[n-1]), max(dp[n-2]) +arr[n] , max(dp[n-2][0] , dp[n-2][1]) + arr[n] + arr[n-1]]
    return(max(dp[-1]))

print(wine())
