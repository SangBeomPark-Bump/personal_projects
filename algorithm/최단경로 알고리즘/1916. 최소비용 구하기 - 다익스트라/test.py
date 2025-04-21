import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
M = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(M)]



A, B = map(int, input().split())

print(N, M, A, B)

for i in arr:
    print(i)
