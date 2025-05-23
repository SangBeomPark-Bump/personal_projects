import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())

arr = list(map(int, input().split()))

K = (50 ** 2) +1
def masking(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b * K + c * K * K

def unmasking(x):
    c = x // (K ** 2)
    b = (x // K) % K
    a = (x % K)
    return a, b, c


dpset = [ set() for _ in range(N+1)]
dpset[0] = set([masking(0,0,0)])

for i in range(N):
    cur_number = arr[i]
    for masked_number in dpset[i]:
        a, b, c = unmasking(masked_number)
        dpset[i+1].add(masking(a + cur_number, b, c))
        dpset[i+1].add(masking(a, b + cur_number, c))
        dpset[i+1].add(masking(a, b, c + cur_number))

maxa = 0
for number in dpset[-1]:
    cura = number % K
    maxa = max(cura, maxa)
print(maxa)