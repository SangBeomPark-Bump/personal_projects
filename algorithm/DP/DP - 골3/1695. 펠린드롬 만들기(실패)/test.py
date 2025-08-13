import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
sys.setrecursionlimit(int(1e7))

N = int(input())

arr = list(map(int, input().split()))


INF = float("inf")
dp = [ [0 for _ in range(N)] for _ in range(N)]

def recursive(start, end):
    if start>=N or start > end:
        return 0

    if end == start:
        dp[start][end] = 1
        return 1
    
    if dp[start][end]:
        return dp[start][end]

    start_number = arr[start]
    ans = recursive(start+1, end)

    for temp_end in range(end, start, -1):
        if start_number == arr[temp_end]:
            ans = max(recursive(start+1, temp_end-1) +2, ans)
            dp[start][end] = ans
            return ans
    dp[start][end] = ans
    return ans

print(N - recursive(0, N-1))
