import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

## 후기 메커니즘. 계산량이 많은걸 없앰
dp_prev = []

default = [0] * 1024
dp_prev.append(default)
for i in range(1, 10):
    temp = default.copy()
    temp[1<<i] = 1
    dp_prev.append(temp)

cnt_sums = []
for _ in range(1, N):
    dp_cur = [[0] * 1024 for _ in range(10) ]
    # cnt_sum = 0
    for i in range(10): ### 저번꺼를 이동시킬거임. 이동시킬 번호는 i
        for bitmask, cnt in enumerate(dp_prev[i]): # 저번꺼의 bitmask 번호
            if i != 0:
                input_minus = bitmask | 1 <<(i-1) ### 예를들어, 1이랑 2면 3
                # if input_minus == 1023:
                #     cnt_sum += cnt %(10**9)
                dp_cur[i-1][input_minus] += cnt%(10**9)
            if i != 9:
                input_plus = bitmask | 1 <<(i+1)
                # if input_plus == 1023:
                #     cnt_sum += cnt
                dp_cur[i+1][input_plus] += cnt%(10**9)
    dp_prev = dp_cur
    # cnt_sums.append(cnt_sum)

s = 0
for i in dp_prev:
    s += i[1023] 
print((s%(10**9)))