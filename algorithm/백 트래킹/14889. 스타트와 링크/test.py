import sys
input = sys.stdin.readline
verbose = False
verboses = [True for _ in range(10)]

M = int(input())
S, P = map(int, input().split())
dna = input()
arr = list(map(int, input().split()))