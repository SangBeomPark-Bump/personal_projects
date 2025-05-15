import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
N, M = map(int, input().split())
X, *arr = map(int, input().split())

string = input().strip('\n')
arr = list(map(int, input().split()))

arr = [int(input()) for _ in range(N)]

arr = [list(map(int, list(input().strip('\n')))) for _ in range(N)]
arr = [list(map(int, input().split() ) ) for _ in range(N)]

# for i in arr:
#     print(i)