import sys
input = sys.stdin.readline
INF = float("inf")
MAX = 1000
dp = [ INF for _ in range(MAX+1)]

def plus(n1, n2):
    return int(str(n1) + str(n2))

def mul(n1, n2):
    return int(str(n1)[0] + str(n2) + str(n1)[1])
multiplier = [(2, 12), (3, 34), (5, 56)]



dp[1] = 12
dp[2] = 34
dp[3] = 56

for n in range(4, MAX+1):
    ans = INF
    for subn in range(1, n):
        ans = min(ans, plus(dp[subn] , dp[n-subn]))
    
    for k, l in multiplier:
        if n % k ==0:
            ans = min(ans, mul(l, dp[n//k]))
    dp[n] = ans

mapping_dict = { str(index +1) : value  for index, value in enumerate(list("(){}[]"))}

def mapper(n1):
    return mapping_dict[n1]

def resolver(n):
    return ''.join(list(map(mapper, list(str(n)))))





T = int(input())
for _ in range(T):
    n = int(input())
    print(resolver(dp[n]))


# for i in arr:
#     print(i)