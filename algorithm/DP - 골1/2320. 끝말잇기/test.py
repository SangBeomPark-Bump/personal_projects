import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())
arr = [input().strip('\n') for _ in range(N)]

dp = [ 0 for _ in range(N)]
visited = [False for _ in range(N)]

def dfs(cur_idx):
    if dp[cur_idx]:
        return dp[cur_idx]
    ans = len(arr[cur_idx])
    for next_idx in range(N):
        if visited[next_idx]:
            continue
        if arr[cur_idx][-1] == arr[next_idx][0]:
            visited[next_idx] = True
            ans = max(ans, len(arr[cur_idx]) + dfs(next_idx) )
            visited[next_idx] = False
    dp[cur_idx] = ans
    return dp[cur_idx]


ans = 0
for n in range(N):
    dp = [ 0 for _ in range(N)]
    visited = [False for _ in range(N)]

    visited[n] = True
    ans = max(ans, dfs(n))
    visited[n] = False

print(ans)