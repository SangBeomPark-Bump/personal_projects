import sys
input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split())

arr = [list(map(int, input().split() ) ) for _ in range(N)]
sum_arr = [[0 for _ in range(M)] for _ in range(N)]
sum_arr[0][0] = arr[0][0]

for n in range(N):
    for m in range(M):
        temp = 0
        if m>0:
            temp += sum_arr[n][m-1]
        if n>0:
            temp += sum_arr[n-1][m]
        if n>0 and m>0:
            temp -= sum_arr[n-1][m-1]
        sum_arr[n][m] = temp + arr[n][m]

def sum_cal(startn, endn, startm, endm):
    temp = sum_arr[endn][endm]

    if startn>0:
        temp -= sum_arr[startn-1][endm] 
    
    if startm>0:
        temp -= sum_arr[endn][startm-1]
    
    if startn > 0 and startm > 0:
        temp += sum_arr[startn-1][startm-1]
    
    return temp


dp = [[[[INF for _ in range(M)] for _ in range(M)] for _ in range(N)] for _ in range(N)]

for n in range(N):
    for m in range(M):
        dp[n][n][m][m] = 0

for x in range(2, N*M+1): ## (N * M 번)
    cur_arr = [i for i in range(1, x + 1) if x % i == 0]
    for dn in cur_arr: ## 생략 번
        dm = x // dn
        if dn> N or dm > M:
            continue
        for startn in range(N-dn+1):
            for startm in range(M-dm+1):
                endn = startn + dn -1
                endm = startm + dm -1
                base = sum_cal(startn, endn, startm, endm)
                for nextn in range(endn-startn):
                    cur_value = base + dp[startn][startn + nextn][startm][endm] + dp[startn+nextn+1][endn][startm][endm]
                    dp[startn][endn][startm][endm] = min(dp[startn][endn][startm][endm], cur_value)

                for nextm in range(endm-startm):
                    cur_value = base + dp[startn][endn][startm][startm + nextm] + dp[startn][endn][startm + nextm +1][endm]
                    dp[startn][endn][startm][endm] = min(dp[startn][endn][startm][endm], cur_value)

print(dp[0][N-1][0][M-1])