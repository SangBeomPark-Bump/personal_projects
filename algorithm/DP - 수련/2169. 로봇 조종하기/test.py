import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())

arr = [list(map(int, input().split() ) ) for _ in range(N)]

INF = float('inf')
dp = [0 for _ in range(M)]
dp_plus = [0 for _ in range(M)]
dp_minus = [0 for _ in range(M)]

temp_sum = 0
for m in range(M):
    temp_sum += arr[0][m]
    dp[m] = temp_sum

for n in range(1, N):
    dp_plus[0] = dp[0] + arr[n][0]
    for m in range(1, M):
        case1 = dp_plus[m-1] + arr[n][m]
        case2 = dp[m] + arr[n][m]
        dp_plus[m] = max(case1, case2)

    dp_minus[-1] = dp[-1] + arr[n][-1]
    for m in range(-2, -M-1, -1):
        case1 = dp_minus[m+1] + arr[n][m]
        case2 = dp[m] + arr[n][m]
        dp_minus[m] = max(case1, case2)
    
    for index, (plus, minus) in enumerate(zip(dp_plus, dp_minus)):
        dp[index] = max(plus, minus)

print(dp[M-1])