import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")
from collections import defaultdict

N, S = map(int, input().split())

hv_dict = defaultdict(int)

for _ in range(N):
    height, value = map(int, input().split())
    hv_dict[height] = max(hv_dict[height], value)

heights = sorted(hv_dict.keys(), reverse=True)

X = int(2e7)
# X = 30
dp = [0 for _ in range( X+1)]

cur_height = heights.pop()

for h in range(1, X+1):
    case1 = 0
    if h == cur_height:
        case1 = dp[cur_height - S] + hv_dict[cur_height]
        if heights:
            cur_height = heights.pop()
    case2 = dp[h-1]
    dp[h] = max(case1, case2)

print(dp[-1])