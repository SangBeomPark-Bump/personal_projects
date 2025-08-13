import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M, K = map(int, input().split())


arr_c = list(map(int, input().split()))
arr_f = [list(map(int, input().split() ) ) for _ in range(M)]

p = [ n for n in range(N+1)]

def find(a):
    if a != p[a]:
        p[a] = find(p[a])
    return p[a]

def union(a, b):
    if a == b:
        return
    pa = find(a)
    pb = find(b)
    if a> b:
        p[pa] = pb
    else:
        p[pb] = pa

for i in range(M):
    a, b = arr_f[i]
    union(a, b)


for n in range(1,N+1):
    p[n] = find(p[n])

group_dict = dict()
for n in range(1, N+1):
    where = p[n]
    if where not in group_dict.keys():
        group_dict[where] = [arr_c[n-1],1]
    else:
        group_dict[where] = [group_dict[where][0] + arr_c[n-1], group_dict[where][1] +1]

dp = [ [ 0 for _ in range(K)] for _ in range(len(group_dict)+1)]

for n, key in enumerate(group_dict.keys(), start = 1):
    for k in range(K):
        prev_k = k - group_dict[key][1]
        case1 = 0
        if 0 <= prev_k:
            case1 = dp[n-1][prev_k] + group_dict[key][0]

        case2 = dp[n-1][k]
        dp[n][k] = max(case1, case2)
    # print(dp[n])

print(dp[-1][-1])
