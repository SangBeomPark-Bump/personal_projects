import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")


N, D = map(int, input().split())
arr = list(map(int, input().split()))

from heapq import heappush, heappop
dp = [-INF for _ in range(N)]

hq = []

maxvalue = -INF
maxindex = -D


for n in range(N):
    case1 = 0
    case2 = maxvalue

    dp[n] = arr[n] + max(case1, case2)

    if dp[n]>= maxvalue:
        maxvalue = dp[n]
        maxindex = n
    else:
        heappush(hq, (-dp[n], n))

    if maxindex + D <= n:
        while maxindex + D <= n:
            maxvalue, maxindex = heappop(hq)
            maxvalue *= -1


print(max(dp))