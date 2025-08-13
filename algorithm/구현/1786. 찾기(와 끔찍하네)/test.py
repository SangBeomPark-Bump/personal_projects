import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
N, M = map(int, input().split())
X, *arr = map(int, input().split())

string = input().rstrip()
arr = list(map(int, input().split()))

arr = [int(input()) for _ in range(N)]

arr = [list(map(int, list(input().strip()))) for _ in range(N)]
arr = [list(map(int, input().split() ) ) for _ in range(N)]

# for i in arr:
#     print(i)