import sys
input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split())

P = int(input())
L = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(L)]
arr.sort(key = lambda x: x[1])


miny = -1
for y, x in arr:
    miny = max(miny, y)
# print(miny)


def calc(size):
    
    result = 0
    covered_x = 0

    for _, x in arr:
        if covered_x < x:
            covered_x = x + size - 1
            result +=1

    return result

start = miny
end = max(N, M)

ans = miny
while start <= end:
    mid = (start + end) // 2
    value = calc(mid)
    if value <= P:
        ans = mid
        end = mid - 1
    
    else:
        start = mid + 1

print(ans)