import sys
input = sys.stdin.readline
INF = float("inf")


W, N = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()


dp = [ set() for _ in range(N)]

dp[2].add(sum(arr[:2]))
for n in range(3, N-1):
    flag = True
    dp[n] = dp[n-1].copy()
    for i in range(n-1):
        if arr[i] + arr[n-1] + arr[n] + arr[n+1] > W:
            break
        dp[n].add(arr[i]+ arr[n-1])
        flag = False
    if flag:
        break

window = sum(arr[:3])
min_window = window

test = False
for n in range(3, N):
    window += arr[n]
    min_window += arr[n]

    if min_window > W:
        break

    if window >= W:
        for n2 in range(n-1, 1, -1):
            cur_number = W - arr[n] - arr[n2]
            if cur_number in dp[n2]:
                test = True
                break

    if test:
        break

    window -= arr[n-3]
    min_window -= arr[n]

print( "YES" if test else "NO")