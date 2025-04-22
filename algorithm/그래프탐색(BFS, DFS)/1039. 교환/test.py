import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


raw_n, raw_k = input().split()

ARR_N = list(map(int, list(raw_n)[::-1]))
K = int(raw_k)
N = len(ARR_N)
INT_N = int(raw_n)


def num_maker(arr):
    ans = 0
    for i in range(N):
        ans += arr[i] * (10**i)
    return ans

from copy import deepcopy

def comb():
    for x in range(K):
        opt_num = -1
        swap = (-1, -1)
        for i in range (N):
            for j in range(i, N):
                temp = deepcopy(ARR_N)
                # print(temp)
                if not (ARR_N[i] == 0 and j == N-1) and i!= j:
                    temp[i], temp[j] = temp[j], temp[i]
                    cur_num = num_maker(temp)
                    # print(f'{x}번째 바뀐그거 : {temp2}')
                    if opt_num < cur_num:
                        opt_num = cur_num
                        swap = (i, j)
        if swap == (-1, -1):
            return -1
        else:
            i, j = swap
            ARR_N[i], ARR_N[j] = ARR_N[j], ARR_N[i]
    return opt_num

print(comb())

# for i in arr:
#     print(i)