import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

# for i in arr:
#     print(i)