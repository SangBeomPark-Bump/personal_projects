import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
arr = [int(input()) for _ in range(N)]

dp = [ [-INF for _ in range(N)] for _ in range(N)]

for n in range(N):
    dp[n][n] = arr[n]

if N > 1:
    for n in range(N):
        dp[n][ (n+1) % N] = max(arr[n] , arr[(n+1) % N])

for factor in range(3 - N%2, N-2, 2):
    for start in range(N):
        end = (start + factor) % N

        case1_prev = dp[ (start+1) % N][ (end-1) %N] if arr[start] > arr[(end-1) %N ] else dp[start][(end-2) %N ]
        case2_prev = dp[ (start+1) % N][ (end-1) %N] if arr[end] > arr[(start+1) % N] else dp[(start+2) % N][end]

        case1 = arr[end] + case1_prev
        case2 = arr[start] + case2_prev
        dp[start][end] = max(case1, case2)

if N <= 2:
    print(max(arr))
else:
    ans = -INF
    for start in range(N):
        n1 = (start+1)%N
        n2 = (start-1)%N

        if arr[n1] > arr[n2]:
            temp = dp[ (n1+1) %N][n2] + arr[start]
        else:
            temp = dp[n1][(n2 -1) % N] + arr[start]
        ans = max(ans, temp)
    print(ans)
    
# for i in arr:
#     print(i)