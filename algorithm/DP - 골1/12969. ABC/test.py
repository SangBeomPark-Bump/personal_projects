import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N, K = map(int, input().split())

from itertools import combinations_with_replacement
from collections import Counter

def solve():
    for n in range(1,N+1):
        cur_cs = list(combinations_with_replacement([0,1,2], n))
        for cur_c in cur_cs:
            cur_dict = Counter(cur_c)
            for i in range(3):
                if i not in  cur_dict.keys():
                    cur_dict[i] = 0
            cur_value = cur_dict[1] * cur_dict[0] + cur_dict[2] * (cur_dict[1] + cur_dict[0])
            if cur_value == K:
                value = 'A'*cur_dict[0] + "B" * cur_dict[1] + 'C' * cur_dict[2]
                if N - len(value) >= 2 and cur_dict[1] == 0 and cur_dict[2] == 0:
                    value = 'B' + value
                if N - len(value) >= 1:
                    value = 'C' *(N - len(value)) + value
                if 'C' in value and 'B' in value and 'A' in value:
                    return value
    return -1
print(solve())

# for i in arr:
#     print(i)