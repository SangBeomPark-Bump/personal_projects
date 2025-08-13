import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(N)]

def maxrix_product(a, b):
    if a == b:
        return 0
    return a[0] * a[1] * b[1]


dp = [[ [0] for _ in range(i) ] for i in range(N, 0, -1)]
INF = float('inf')
for factor in range(N):
    for start in range(N-factor):
        end = start + factor
        if factor == 0:
            dp[factor][end] = (maxrix_product(arr[start], arr[end]), arr[start][0], arr[end][1])
        else:
            value = INF
            for front_factor in range(factor):
                behind_factor = factor - front_factor - 1
                start_value, *case1 = dp[front_factor][start]
                end_value, *case2 = dp[behind_factor][end-behind_factor]

                value = min(value, maxrix_product(case1, case2) + start_value + end_value)

            dp[factor][start] = [value, arr[start][0], arr[end][1]]

print(dp[-1][0][0])