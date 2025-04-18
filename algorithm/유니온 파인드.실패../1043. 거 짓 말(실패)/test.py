import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N, M = map(int, input().split())

T, *t_arr = map(int, input().split())

p_arr = [list(map(int, input().split() ) ) for _ in range(M)]

party_union = [num for num in range(N+1)]

def find(x):
    if party_union[x] == x:
        return x
    return party_union[x]

def uninon(a, b):
    fa = find(a)
    fb = find(b)

    if fa < fb:
        party_union[fb] = fa
    else :
        party_union[fa] = fb

for party_num, *party_members in p_arr:
    for i in range(party_num - 1):
        uninon(party_members[i], party_members[i+1])

know_true_party = list(set([find(t)for t in t_arr] ))

cnt = 0
for party in p_arr:
    if find(min(party[1:])) not in know_true_party:
        cnt +=1

print(cnt)