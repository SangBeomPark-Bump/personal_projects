import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
arr = [list(map(int, input().split() ) ) for _ in range(N)]

temp = 0

first_high = 0
max_high = -INF
not_first_max_high = -INF

for i in range(1,N):
    cer = arr[i][0]
    value = arr[i-1][1]
    temp += value
    if temp - cer > 0:
        if not first_high:
            first_high = i
        else:
            not_first_max_high = max(not_first_max_high, temp - cer)
        max_high = max(max_high, temp - cer)

ans = first_high == 0
for i in range(first_high):
    if arr[i][1] >= max_high:
        ans = True
        break
if arr[first_high][1] >= not_first_max_high and not ans:
    ans = True

print("Kkeo-eok" if ans else "Zzz")