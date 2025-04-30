import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
ns = list(map(int, input().split()))
M = int(input())
ms = list(map(int, input().split()))

available = [False for _ in range(40001)]

dp = [ [set() for _ in range(N)] for _ in range(N)]

for n in range(N):
    dp[n][n].add(ns[n])
    available[ns[n]] = True


def setmaker(list1, list2):
    global available
    myset = set()
    for i in list1:
        for j in list2:
            if i < j:
                myset.add(j - i)
                available[j-i] = True
            elif i> j :
                myset.add(i - j)
                available[i - j] = True
            myset.add(i + j)
            available[i+j] = True
    return myset

for factor in range(1, N+1):
    for start in range(N-factor):
        end = start  + factor
        
        for startfactor in range(factor):
            endfactor = factor - startfactor - 1
            dp[start][end] = dp[start][end].union(setmaker(dp[start][start+ startfactor], dp[end - endfactor][end]))

print(' '.join(['Y' if available[m] else "N" for m in ms]))