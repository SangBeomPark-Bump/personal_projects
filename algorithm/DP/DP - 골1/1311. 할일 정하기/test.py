import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())
arr = [list(map(int, input().split() ) ) for _ in range(N)]

maxmask = (1 << N)
dp = [INF for _ in range( maxmask)]
dp[0] = 0

numbers = [ set() for _ in range(N+1)]
numbers[0].add(0)

for n in range(1, N+1):
    cur_arr = arr[n-1]
    for i in range(N):
        for mask in numbers[n-1]:
            if not (mask & (1<<i)):
                dp[mask | (1<<i)] = min(dp[mask | (1<<i)],  dp[mask] + cur_arr[i])
                numbers[n].add(mask | (1<<i))
print(dp[-1])