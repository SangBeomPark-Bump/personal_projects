import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())
arr = [list(map(int, input().split() ) ) for _ in range(M)]


ps = [[number, [], 0] for number in range(N+1)]


for start, end in arr:
    ps[start][1].append(end)
    ps[end][2] +=1

from collections import deque

que = deque()

for i in ps[1:]:
    if i[2] == 0:
        que.append(i)

que

result = []
while que:
    cur_num, ends, _ =  que.popleft()
    result.append(cur_num)
    for end_num in ends:
        ps[end_num][2] -=1
        if ps[end_num][2] == 0:
            que.append(ps[end_num])
print(' '.join(map(str, result)))

# for i in arr:
#     print(i)