import sys
input = sys.stdin.readline
INF = float("inf")

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))


    dp = [ [ False for _ in range(n+1)] for n in range(N+1)]
    dp[0][0] = True
    for n in range(N+1):
        for score in range(n+1):
            if not dp[n][score]:
                continue
            for m in range(M):
                new_score = score + arr[m]
                if new_score + n > N:
                    continue
                dp[new_score + n][new_score] = True

    ans = -1
    for n in range(N+1):
        if dp[-1][n]:
            ans = max(ans, n)
    print(ans)