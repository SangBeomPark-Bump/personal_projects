import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

q = input().strip('\n')
a = input().strip('\n')

N, M = len(q), len(a)
q = ' ' + q
a = ' ' + a

INF = float('inf')
dp = [ [n] + [INF for _ in range(M)] for n in range(N+1)]
dp[0] = [ i for i in range(M+1)]
for n in range(1, N+1):
    letter_q = q[n]
    for m in range(1, M+1):
        letter_a = a[m]
        if letter_a == letter_q:
                dp[n][m] = min(dp[n][m], dp[n-1][m-1])
        
        dp[n][m] = min(dp[n][m], dp[n][m-1] +1, dp[n-1][m] +1, dp[n-1][m-1] +1)
print(dp[-1][-1])