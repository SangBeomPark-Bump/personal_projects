import sys
input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

if N <= M:
    print(N)
    exit()

def calc(x):
    result = 0
    for i in arr:
        result += (x // i) + 1
    return result

start = 1
end = (N // M) * (max(arr) + 1) 

while start <= end:
    mid = (start + end) // 2
    max_kid = calc(mid)
    if max_kid < N:
        start = mid + 1
    elif max_kid >= N:
        end = mid - 1
        ans_time = mid

mod =  N - calc(ans_time - 1)

ans = -1
for index,att in enumerate(arr):
    if ans_time % att == 0:
        mod -= 1
    
    if mod == 0:
        ans = index + 1
        break

print(ans)