import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")
MOD = int(1e6)

from collections import Counter

T, A, S ,B =  map(int, input().split())

arr = list(map(int, input().split()))
counter_dict = Counter(arr)

dp = [[0 for _ in range(B+1)] for _ in range(len(counter_dict) +1)]
dp[0][0] = 1

for index, (c, freq) in enumerate(counter_dict.items(), start=1): ## a
    for a in range(B+1): # A번
        for i in range(freq+1): ## a와 같이 T번
            if a+i < B+1:
                dp[index][a+i] += dp[index-1][a]
        dp[index][a] %= MOD

print(sum(dp[-1][S:B+1]) % MOD)
