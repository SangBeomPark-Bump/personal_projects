import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())
arr = [int(input()) for _ in range(N)]

arr = [0] + arr

import math
P = int(5e5)
rp = math.floor(math.sqrt(P))

is_prime = set( range(2, P+1))

for n in range(2, rp+1):
    if n in is_prime:
        for j in range(n * 2,P+1,n):
            if j in is_prime:
                is_prime.remove(j)

from collections import defaultdict

ndict = defaultdict(int)
for i in arr[1:]:
    ndict[i] +=1
arr2 = [ [key, value] for key, value  in ndict.items()]

X = P
curdp = [0 for _ in range(int(X+1))]
nextdp = [0 for _ in range(int(X+1))]
curdp[0] = 1

for n in range(1, len(arr2)+1):
    number, many = arr2[n-1]
    for prev_number in range(X+1):
        if curdp[prev_number]:
            nextdp[prev_number] += curdp[prev_number]
            for k in range(1, many+1):
                cur_number = number * k
                nextdp[prev_number + cur_number] += curdp[prev_number]
    curdp = nextdp
    nextdp = [0 for _ in range(int(X+1))]

cnt = 0
for n in range(X):
    if curdp[n] and  n in is_prime:
        cnt += curdp[n]
print(cnt)


# for i in arr:
#     print(i)