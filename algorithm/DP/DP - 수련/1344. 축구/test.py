import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

A = int(input()) / 100
B = int(input()) / 100

def non_prime(test):
    a = (test[2] + test[3] + test[5] + test[7] + test[11] + test[13] + test[17])
    return 1-a


dp_A = [ [0 for _ in range(19) ] for _ in range(19)]
dp_B = [ [0 for _ in range(19) ] for _ in range(19)]
dp_A[0][0] = 1
dp_B[0][0] = 1

for n in range(1, 19):
    for goal in range(19):
        prob_A = dp_A[n-1][goal]
        prob_B = dp_B[n-1][goal]
        if goal != 18:
            dp_A[n][goal+1] = dp_A[n][goal+1] + prob_A * A
            dp_B[n][goal+1] = dp_B[n][goal+1] + prob_B * B
        dp_A[n][goal] = dp_A[n][goal] + prob_A * (1-A)
        dp_B[n][goal] = dp_B[n][goal] + prob_B * (1-B)


print(1 - non_prime(dp_A[-1]) * non_prime(dp_B[-1]))