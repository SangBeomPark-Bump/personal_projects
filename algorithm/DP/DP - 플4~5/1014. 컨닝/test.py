import sys
input = sys.stdin.readline
INF = float("inf")
T = int(input())

bitrank = [0 for _ in range(1<<10)]
for bit in range(1<<10):
    indexbit = bit
    cnt = 0
    while bit:
        if bit %2:
            cnt +=1
        bit //=2
    bitrank[indexbit] = cnt



for _ in range(T):
    N, M = map(int, input().split())

    arr = [list(input().strip('\n')) for _ in range(N)]

    pos_bit = []
    for bit in range(1<<M):
        cnt = 0
        testbit = bit
        while testbit:
            if testbit %2 == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt == 2:
                break
            testbit //= 2
        if cnt == 2:
            continue
        else:
            pos_bit.append(bit)

    impos_bitarr = [ 0 for _ in range(1<<M)]

    for bit in pos_bit:
        impossible_set = set()
        bitindex = bit

        index = 0
        while bit:
            if bit %2:
                if index + 1 < M:
                    impossible_set.add(index+1)
                if index -1 >=0:
                    impossible_set.add(index-1)
            index +=1
            bit //= 2

        impos_bit = 0
        for impossbile_index in impossible_set:
            impos_bit |= 1<<impossbile_index
        impos_bitarr[bitindex] = impos_bit

    dp = [ [-INF for _ in range(1 << M)] for _ in range(N+1)]
    dp[0][0] = 0

    for n in range(1, N+1):
        xloc = 0
        for m in range(M):
            if arr[n-1][m] == 'x':
                xloc |= (1<<m)
        for cur_bit in pos_bit:
            if dp[n-1][cur_bit] == -INF :
                continue
            impos_bit = impos_bitarr[cur_bit]
            impos_bit |= xloc

            for next_bit in pos_bit:
                if impos_bit & next_bit:
                    continue
                dp[n][next_bit] = max(dp[n][next_bit], dp[n-1][cur_bit] + bitrank[next_bit])
    print(max(dp[-1]))