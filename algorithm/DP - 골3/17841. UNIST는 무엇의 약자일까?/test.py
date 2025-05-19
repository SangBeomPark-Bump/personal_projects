import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())
arr = [input().strip('\n') for _ in range(N)]
UNIST = list("UNIST")

for i in arr:
    print(i)