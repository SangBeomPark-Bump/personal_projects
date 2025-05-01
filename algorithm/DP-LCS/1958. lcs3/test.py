import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


str1 = input().strip('\n')
str2 = input().strip('\n')
str3 = input().strip('\n')

N = len(str1)
M = len(str2)
L = len(str3)

dp = [ [ [0 for _ in range(L+1)] for _ in range(M+1) ] for _ in range(N+1) ]

for n in range(1,N+1):
    letn = str1[n-1]
    for m in range(1,M+1):
        letm = str2[m-1]
        for l in range(1,L+1):
            letl = str3[l-1]
            if letl == letm and letn == letm:
                dp[n][m][l] = dp[n-1][m-1][l-1] + 1
            else:
                dp[n][m][l] = max(dp[n-1][m][l], dp[n][m-1][l], dp[n][m][l-1])

print(dp[-1][-1][-1])