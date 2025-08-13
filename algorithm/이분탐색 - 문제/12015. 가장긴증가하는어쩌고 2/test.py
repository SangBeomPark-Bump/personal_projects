import sys
input = sys.stdin.readline
INF = float("inf")
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

lis = []

for num in arr:
    idx = bisect_left(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(len(lis))