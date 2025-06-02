import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())
arr = list(map(int, input().split()))
MOD = int(1e9) + 7


reduced_n = ((N+1)//2) +1
dp = [ [0 for _ in range(reduced_n)] for n in range(N+1)]

dp[1][0] = 1


for n in range(2, N+1):
    for k in range(reduced_n):
        if k < reduced_n:
            dp[n][k] += dp[n-1][k]
        if  k+1 < reduced_n:
            dp[n][k] += dp[n-1][k+1]
        if k >0:
            dp[n][k] += dp[n-1][k-1]
        dp[n][k] %= MOD




if ((arr[0] == 0) or (arr[0] == -1)) and ((arr[-1] == 0) or (arr[-1] == -1)):
    ans = 1 
    arr[0] = 0
    arr[-1] = 0
    start = 0
    length = 1
    end = 0
    while end < N-1:
        end +=1
        length +=1
        if arr[end] == -1:
            continue
        k = abs(arr[start] - arr[end])
        if k >= length or k >= reduced_n:
            ans = 0
            break
        ans *= dp[length][k]
        ans %= MOD
        length = 1
        start = end
else:
    ans = 0

print(ans)
