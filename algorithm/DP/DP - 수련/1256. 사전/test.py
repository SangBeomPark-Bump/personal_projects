import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N, M, K = map(int, input().split())
K -=1


# import math

# nmCn = math.comb((N+M), N)

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for n in range(N+1):
    for m in range(M+1):
        if n== 0 or m == 0:
            dp[n][m] = 1
        else:
            dp[n][m] = dp[n-1][m] + dp[n][m-1]

def recursive(N, M, K):
    global ans
    if N  == 0:
        ans += 'z' * M
        print(ans)
        return
    if M == 0:
        ans += 'a' * N
        print(ans)
        return
    picked_n = dp[N-1][M]
    picked_m = dp[N][M-1]

    if 0 <= K < picked_n:
        ans += 'a'
        recursive(N-1, M, K)
    elif picked_n <= K < picked_n + picked_m:
        ans += 'z'
        recursive(N, M-1, K- picked_n)
    else:
        # print(picked_n, K, comb, sep='\n')
        print(-1)
        return
ans = ''

recursive(N, M, K)