import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())

def golonb(n):
    if n in range(1, 6):
        return [0, 1, 2, 2, 3, 3][n]
    else:
        dp = [1, 2, 4, 6]
        howmany = 3
        number = 4
        value = 6
        while True:
            end = dp[howmany]
            while number < end:
                dp.append(dp[-1] + howmany)
                number +=1
                value += howmany
                if value > n:
                    return number-1
            howmany+=1

print(golonb(N))
