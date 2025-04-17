import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
sys.setrecursionlimit(10000)

C, N = map(int, input().split())

arr = [tuple(map(int, input().split() ) ) for _ in range(N)]
arr = [0] + arr

dp = [[0] for _ in range(N+1)]

for n in range(1, N+1):
    c = 1
    while True:
        pay, benefit = arr[n]
        prev = c - pay
        case1 = 0
        if prev >= 0:
            case1 = dp[n][prev] + benefit
        try:
            case2 = dp[n-1][c]
        except IndexError:
            case2 = 0
        dp[n].append(max(case1, case2))
        c +=1
        if dp[n][-1] >= C:
            break

print(len(dp[-1])-1)