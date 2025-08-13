import sys
input = sys.stdin.readline
INF = float("inf")


N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

ans = 0
start = 0
end = arr[-1] - arr[0]

while start <= end:
    
    mid = (start + end) // 2
    
    curhouse = arr[0]

    c = 1
    for n in range(1, N):
        if arr[n] - curhouse >= mid:
            curhouse = arr[n]
            c += 1
    
    if c < C:
        end = mid - 1
    else:
        ans = max(ans, mid)
        start = mid + 1

print(ans)