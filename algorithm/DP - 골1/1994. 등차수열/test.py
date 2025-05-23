import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")
sys.setrecursionlimit(int(1e7))

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()


degrees = [ dict() for _ in range(N)]
for i in range(N):
    for j in range(N-1, i, -1):
        degrees[i][arr[j] - arr[i]] = j

dp = [ [-1 for _ in range(N)] for _ in range(N)]
def recursive_reduced(start, end):
    if dp[start][end] >=0:
        return dp[start][end]
    dp[start][end] = 0
    
    if arr[end] - arr[start] in degrees[end]:
        next_end = degrees[end][arr[end] - arr[start]]
        dp[start][end] = 1 + recursive_reduced(end, next_end)
    return dp[start][end]

max_len = -1
for i in range(N-1):
    for j in range(i+1,N):
        max_len = max(max_len, recursive_reduced(i,j))

print(max_len +2)