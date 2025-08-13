import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")


N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

degrees = [ dict() for _ in range(N)]
for i in range(N):
    for j in range(N-1, i, -1):
        degrees[j][arr[j] - arr[i]] = i

dp = [ [-1 for _ in range(N)] for _ in range(N)]
ans = 1
for start in range(N-1):
    for end in range(start+1, N):
        if arr[end] - arr[start] in degrees[start]:
            prev_start = degrees[start][arr[end] - arr[start]]
            dp[start][end] = dp[prev_start][start] +1
        else:
            dp[start][end] = 2
        ans = max(ans, dp[start][end])

print(ans)