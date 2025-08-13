import sys
input = sys.stdin.readline
verbose = False
verboses = [True for _ in range(10)]

N, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]


dp = [0] + [float('inf') for _ in range(K)] 

for n in range(N):
    for k in range(1, K+1):
        prev = k - arr[n]
        if prev >= 0:
            dp[k] = min( dp[prev] + 1, dp[k])

if dp[-1] == float('inf'):
    print(-1)
else :
    print(dp[-1])