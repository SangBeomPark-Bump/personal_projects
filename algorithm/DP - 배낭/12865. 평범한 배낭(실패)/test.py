import sys
input = sys.stdin.readline
verbose = False
verboses = [True for _ in range(10)]


N, K = map(int, input().split())


arr = [list(map(int, input().split() ) ) for _ in range(N)]



dp = [0] * (K + 1)
for i in arr:
    if i[0] < K+1:
        dp[i[0]] = i[1]

for j in range(K+1):
    for weigt, value in arr:
        if j > weigt:
            dp[j] = max(dp[j - weigt] + dp[weigt], dp[j-1], dp[j])
print(dp[-1])