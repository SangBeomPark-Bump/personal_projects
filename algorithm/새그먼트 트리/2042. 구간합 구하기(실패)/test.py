import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
import math
sys.setrecursionlimit(int(1e7))

N, M, K = map(int, input().split())
arr_n = [int(input()) for _ in range(N)]
tree_depth =  math.ceil(math.log(N, 2))+1
segment = [ [] for _ in range(tree_depth)]
segment[0] = arr_n

for depth in range(1, tree_depth):
    temp_sum = 0
    for i in range(len(segment[depth-1])):
        temp_sum += segment[depth-1][i]
        if i%2 == 1:
            segment[depth].append(temp_sum)
            temp_sum = 0
    if temp_sum:
        segment[depth].append(temp_sum)

def recursive_sum(start, end, depth, value):
    global tree_depth
    if start == end:
        ans = segment[0][start]
        return ans
    if end-start == 2**(tree_depth-depth)-1:
        ans =  segment[-depth][start // 2**(tree_depth-depth)] 
        return ans
    if start < value and end < value:
        ans = recursive_sum(start, end, depth+1, 2**(tree_depth-2 - depth))
    elif start >= value and end >= value:
        ans = recursive_sum(start, end, depth+1, value + 2**(tree_depth-2 - depth))    
    elif start<value and end>=value:
        ans = recursive_sum(start, value-1, depth+1, 2**(tree_depth-2 - depth)) + recursive_sum(value, end, depth+1, value + 2**(tree_depth-2 - depth))
    return ans

def recursive_change(start, rep_value, depth):
    global tree_depth
    if depth == tree_depth:
        segment[0][start] = rep_value
        return
    segment[-depth-1][start // 2**(tree_depth-depth-1)] += rep_value - segment[0][start]
    recursive_change(start, rep_value, depth+1)


for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        recursive_change(b-1, c, 0)
    if a == 2:
        print(recursive_sum(b-1, c, 0, 2**(tree_depth-1)))


