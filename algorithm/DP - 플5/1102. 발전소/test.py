import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())
arr = [list(map(int, input().split() ) ) for _ in range(N)]
string = input().strip('\n')
P = int(input())


ybit = 0
yarr = []

temp = 1
for i in range(N):
    if string[i] == 'Y':
        ybit += temp
        yarr.append(i)
    temp *= 2

def rankcalc(bit):
    value = 0
    while bit > 0:
        if bit %2 == 1:
            value +=1
        bit //= 2
    return value

if rankcalc(ybit) >= P:
    print(0)
    exit()

if ybit == 0:
    print(-1)
    exit()


bitrank = [ [] for _ in range(N+1)]

for bit in range(1<<N):
    bitrank[rankcalc(bit)].append(bit)



dp = [ [INF for _ in range(N)] for _ in range(1<<N)]


for i in yarr:
    for j in range(N):
        dp[ybit][j] = min(arr[i][j], dp[ybit][j])

import math
ans = INF
for rank in range(rankcalc(ybit)+1, N+1):
    for bit in bitrank[rank]:
        if bit & ybit != ybit:
            continue

        num = 0
        value = INF
        curarr = []

        valuebit = bit

        while valuebit>0:
            if valuebit%2 == 1:
                value = min(dp[bit - (1<<num)][num], value)
                curarr.append(num)
            valuebit //= 2
            num +=1

        if rank >= P:
            ans = min(ans, value)
            continue

        for i in curarr:
            for j in range(N):
                if (1<<j) & bit:
                    dp[bit][j] = 0
                    continue
                dp[bit][j] = min(value + arr[i][j], dp[bit][j])

print(ans)