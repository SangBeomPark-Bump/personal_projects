import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
W = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(W)]

def dist( a1, a2):
    return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])

sad0 = [ INF for _ in range(W)]
sad1 = [ INF for _ in range(W)]

sad0[0], sad1[0] = dist((1,1), arr[0]), dist((N, N), arr[0])

for w in range(1, W):
    sad0[w] = sad0[w-1] + dist(arr[w-1], arr[w])
    sad1[w] = sad1[w-1] + dist(arr[w-1], arr[w])


dp = [ [ [INF for _ in range(W)] for _ in range(2)] for _ in range(W)]
for w in range(1, W):
    dp[w][0][w-1] = sad1[w-1] + dist((1,1), arr[w])
    dp[w][1][w-1] = sad0[w-1] + dist((N,N), arr[w])

    for subw in range(w):
        if subw == w - 1:
            for psw in range(subw):
                cur_dist = dist(arr[psw] , arr[w])
                dp[w][0][w-1] = min( dp[w][0][w-1], dp[w-1][1][psw] + cur_dist)
                dp[w][1][w-1] = min( dp[w][1][w-1], dp[w-1][0][psw] + cur_dist)
        else:
            cur_dist = dist(arr[w-1], arr[w])
            dp[w][0][subw] = dp[w-1][0][subw] + cur_dist
            dp[w][1][subw] = dp[w-1][1][subw] + cur_dist

print(min( min(dp[-1][0]), min(dp[-1][1]), sad0[-1], sad1[-1]))