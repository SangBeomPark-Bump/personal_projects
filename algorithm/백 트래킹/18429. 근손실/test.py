import sys
input = sys.stdin.readline
verbose = False

N, K = map(int, input().split())
arr = list(map(int, input().split()))

from itertools import permutations
orders = list(permutations(arr))  

result = 0
for order in orders:
    muscle = 500
    result +=1
    for program in order:
        muscle += program - K
        if muscle < 500:
            result -=1
            break
print(result)