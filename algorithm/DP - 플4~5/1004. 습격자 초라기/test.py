import sys
input = sys.stdin.readline
INF = float("inf")


T = int(input())

for _ in range(T):
    N, W = map(int, input().split())

        
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    arr1.append(arr1[0])
    arr2.append(arr2[0])

    mode = [[0,0], [-1, -1], [0, -1], [-1, 0]]
    ans = INF
    for a, b in mode:
        arx = arr1[::]
        ary = arr2[::]
        arx[a] = W
        ary[b] = W

        dp = [[INF for _ in range(4)] for _ in range(N+2)]
        dp[0][3] = 0
        dp[1][0] = 2
        dp[1][3] = 1 if arx[0] + ary[0] <= W else INF

        for n in range(2, N+2):
            dp[n][0] = min(dp[n-1]) + 2

            if ary[n-2] + ary[n-1] <= W:
                dp[n][1] = min(dp[n-1][0], dp[n-1][2]) + 1
            
            if arx[n-2] + arx[n-1] <=W:
                dp[n][2] = min(dp[n-1][0], dp[n-1][1]) + 1
            
            if ary[n-2] + ary[n-1] <= W and arx[n-2] + arx[n-1] <=W :
                dp[n][3] = min(dp[n][3], min(dp[n-2]) + 2)
            
            if arx[n-1] + ary[n-1] <= W:
                dp[n][3] = min(dp[n][3], min(dp[n-1]) + 1)

        ans = min(ans, min(dp[-1]))

    print(ans - 2)

