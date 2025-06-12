import sys
input = sys.stdin.readline
INF = float("inf")
MOD = int(1e9) + 7

def matmul(A1, A2):
    ans = [ [0, 0], [0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] += A1[i][k] * A2[k][j]
            ans[i][j] %= MOD
    return ans

def recursive(n):
    if n == 1:
        return [[4, -1], [1, 0]]
    if n == 0:
        return [[1, 0], [0, 0]]
    
    matrix = recursive(n//2)
    result = matmul(matrix, matrix)

    if n % 2:
        result = matmul(result, recursive(1))

    return result

N = int(input())

if N % 2:
    print(0)
else:
    N //=2
    print(sum(recursive(N)[0]) % MOD)

# for i in arr:
#     print(i)