import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())

arr = [list(map(int, input().split() ) ) for _ in range(M)]

# for i in arr:
#     print(i)