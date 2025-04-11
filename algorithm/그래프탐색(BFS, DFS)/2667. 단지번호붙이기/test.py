import sys
input = sys.stdin.readline
verbose = False

N, M = map(int, input().split())
arr =  [list(map(int,list(input().strip('\n')))) for _ in range(N) ]