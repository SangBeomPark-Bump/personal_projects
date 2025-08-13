import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arrup = []
arrdown = []
for i in range(N):
    upnum = arr1[i]
    downnum = arr2[i]
    if upnum:
        arrup.append(upnum)
    if downnum:
        arrdown.append(downnum)

nu = len(arrup)
su = N - nu
nd = len(arrdown)
sd = N - nd

dp = [[ [ - INF for _ in range(sd+1) ]  for _ in range(su+1)] for _ in range(N+1)]

dp[0][0][0] = 0

for n in range(1, N+1):
    for prev_su in range(su+1):
        if prev_su >= n:
            continue
        for prev_sd in range(sd+1):
            if prev_sd >= n :
                continue
            if 0<= n - 1- prev_su < nu and 0 <= n - 1- prev_sd <nd:
                factor1 = arrup[n-1 - prev_su] * arrdown[n - 1- prev_sd]
                dp[n][prev_su][prev_sd] = max(dp[n][prev_su][prev_sd], dp[n-1][prev_su][prev_sd] + factor1)

            if prev_su != su:
                dp[n][prev_su+1][prev_sd] = max(dp[n][prev_su+1][prev_sd], dp[n-1][prev_su][prev_sd])

            if prev_sd != sd:
                dp[n][prev_su][prev_sd+1] = max(dp[n][prev_su][prev_sd+1], dp[n-1][prev_su][prev_sd])

            if prev_su != su and prev_sd != sd:
                dp[n][prev_su+1][prev_sd+1] = max(dp[n][prev_su+1][prev_sd+1], dp[n-1][prev_su][prev_sd])


print(dp[-1][-1][-1])
