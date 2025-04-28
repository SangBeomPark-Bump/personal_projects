import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    sum_arr = [0]
    for i in range(N):
        sum_arr.append( sum_arr[-1] + arr[i])


    def size(a, b):
        return sum_arr[b+1] - sum_arr[a]

    dp = [ [0 for _ in range(N)] for _ in range(N)]



    for factor in range(1,N):
        for start in range(N-factor):
            end = start + factor
            tempmin = float('inf')
            filesize = size(start, end)
            for startfactor in range(factor):
                endfactor = factor - startfactor -1
                startend = start + startfactor 
                endstart = end - endfactor
                tempmin = min(tempmin, dp[start][startend] + dp[endstart][end]+filesize)
            dp[start][end] = tempmin

    print(dp[0][-1])
