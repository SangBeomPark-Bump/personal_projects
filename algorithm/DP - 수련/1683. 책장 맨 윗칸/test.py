import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
S, P = map(int, input().split())
X, *arr = map(int, input().split())

dna = input()
arr = list(map(int, input().split()))

arr = [int(input()) for _ in range(N)]

arr = [list(map(int, list(input().strip('\n')))) for _ in range(N)]
arr = [list(map(int, input().split() ) ) for _ in range(N)]

# for i in arr:
#     print(i)