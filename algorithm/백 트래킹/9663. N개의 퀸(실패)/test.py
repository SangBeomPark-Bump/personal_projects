import sys
input = sys.stdin.readline
verbose = False

sys.setrecursionlimit(100000)

N = int(input())

def is_possible(r):
    for i in range(r):
        if arr[r] == arr[i]:
            return False
        if r - i == abs(arr[r] - arr[i]):
            return False
    return True

arr = [0] * N

def dfs(depth):

    if depth == N:
        return 1
    
    ans = 0

    for i in range(N):
        arr[depth] = i
        if is_possible(depth):
            ans += dfs(depth + 1)
    return ans

print(dfs(0))