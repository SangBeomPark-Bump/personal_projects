import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

str1 = input().strip('\n')
str2 = input().strip('\n')

N = len(str1)
M = len(str2)

dp = [['' for _ in range(M+1)] for _ in range(N+1)]


for index_n in range(1,N+1):
    letter_n = str1[index_n-1]

    for index_m in range(1,M+1):
        letter_m = str2[index_m-1]
        case1 = ''
        if letter_m == letter_n:
            case1 += dp[index_n-1][index_m - 1] +letter_m

        case2 = dp[index_n][index_m-1]
        case3 = dp[index_n-1][index_m]

        dp[index_n][index_m] = max(case1, case2, case3, key= lambda x: len(x))

print(len(dp[-1][-1]))