import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
sys.setrecursionlimit(int(1e7))

N = int(input())

arr = list(map(int, input().split()))


dp = [False for _ in range(int(6e5)+1)]

def recursive(obj, howmany, end):
    global cnt
    if dp[obj + int(3e5)]:
        return True

    if howmany == 0:
        return obj == 0

    if end <= 0:
        return False
    
    if howmany <0:
        return False

    for i in range(howmany + 1):
        dp[obj + int(3e5)] = dp[obj + int(3e5)] or recursive(obj - arr[end-1] * i, howmany - i, end-1)

    return dp[obj + int(3e5)]

ans = 0
for end in range(N):
    temp = recursive(arr[end], 3, end)
    # print(temp)
    ans += int(temp)
print(ans)