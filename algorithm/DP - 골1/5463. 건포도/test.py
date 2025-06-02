import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")
sys.setrecursionlimit(int(1e7))

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
    
    if startn > 0 and endm > 0:
        temp += sum_arr[startn-1][startm-1]
    
    return temp



dp = [[[[INF for _ in range(M)] for _ in range(M)] for _ in range(N)] for _ in range(N)]



def recursive( startn, endn, startm, endm ):
    if dp[startn][endn][startm][endm] != INF:
        return dp[startn][endn][startm][endm]
    if (startm == endm) and (startn == endn):
        dp[startn][endn][startm][endm] = 0
        return 0
    
    base = sum_cal(startn, endn, startm, endm)
    
    for nextn in range(endn-startn):
        cur_value = base + recursive(startn, startn + nextn, startm, endm) + recursive(startn+nextn+1, endn, startm, endm)
        dp[startn][endn][startm][endm] = min(dp[startn][endn][startm][endm], cur_value)
        
    for nextm in range(endm-startm):
        cur_value = base + recursive(startn, endn, startm, startm + nextm) + recursive(startn, endn, startm + nextm +1, endm)
        dp[startn][endn][startm][endm] = min(dp[startn][endn][startm][endm], cur_value)

    return dp[startn][endn][startm][endm]

print(recursive(0, N-1, 0, M-1))