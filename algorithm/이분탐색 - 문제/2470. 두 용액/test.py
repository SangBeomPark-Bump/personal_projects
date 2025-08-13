import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = [INF, INF, INF]
for n in range(N):
    start = n + 1
    end = N-1
    mynumber = arr[n]
    curnumber = [INF,  INF, INF]

    while start <= end:
        mid = (start + end) // 2
        temp = mynumber + arr[mid]
        curnumber = min([abs(temp), mynumber, arr[mid]], curnumber)
        if temp < 0:
            start = mid + 1
        elif temp > 0:
            end = mid - 1
        else:
            break
    ans = min(curnumber, ans)

print(" ".join( map(str, sorted(ans[1:]))) )

