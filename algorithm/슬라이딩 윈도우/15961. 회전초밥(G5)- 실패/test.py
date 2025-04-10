import sys
input = sys.stdin.readline
verbose = False

import sys
input = sys.stdin.readline
verbose = False

N, d, k , c = map(int, input().split())
sushi_list = [int(input()) for _ in range(N)]
sushi_list =  sushi_list + sushi_list[:k-1]