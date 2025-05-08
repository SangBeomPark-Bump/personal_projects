import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = list(map(int, input().split()))
arr += [0] * (3-N)


from collections import deque
from itertools import permutations



def hehe():
    dp = [ [ [ -1 for _ in range(arr[2]+1) ] for _ in range(arr[1]+1) ] for _ in range(arr[0]+1)]
    dp[arr[0]][arr[1]][arr[2]] = 0

    que = deque()
    que.append(arr)

    my_list = list(permutations([9, 3, 1], 3))
    while que:
        num1, num2, num3 = que.popleft()
        nextdp = dp[num1][num2][num3] +1

        for d1, d2, d3 in my_list:
            next_num1 = num1 - d1 if num1 > d1 else 0
            next_num2 = num2 - d2 if num2 > d2 else 0
            next_num3 = num3 - d3 if num3 > d3 else 0

            if next_num1 + next_num2 + next_num3 ==0:
                print(nextdp)
                return
            if dp[next_num1][next_num2][next_num3] != -1:
                continue
            dp[next_num1][next_num2][next_num3] = nextdp
            que.append([next_num1, next_num2, next_num3])

hehe()