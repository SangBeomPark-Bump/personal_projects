import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

raw_n, raw_k = input().split()

ARR_N = list(map(int, list(raw_n)[::-1]))
K = int(raw_k)
N = len(ARR_N)
INT_N = int(raw_n)

def swap(n, i, j):
    i_num = (n // (10 ** i)) % 10
    j_num = (n // (10 ** j)) % 10

    return n - i_num * (10**i) - j_num * (10**j) + i_num * (10**j) + j_num * (10**i)



def sad():
    num_set = set([INT_N])
    for _ in range(K):
        myset = set()
        for number in num_set:
            for i in range(N):
                for j in range(i,N):
                    if not ((number // (10 ** i)) % 10 == 0 and j == N-1) and i!= j:
                        myset.add(swap(number, i, j))
        if not myset:
            return -1
        else:
            num_set = myset
    return max(num_set)


print(sad())