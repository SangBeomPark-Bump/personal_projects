import sys
input = sys.stdin.readline
INF = float("inf")


N, M = map(int, input().split())
arr = [list(map(int, input().split() ) ) for _ in range(N)]

initial_blocks = [
    ((0, 0), (0, 1), (1, 0), (1, 1)), 
    
    ((0, 0), (0, 1), (0, 2), (0, 3)), 
    ((0, 0), (1, 0), (1, 1), (2, 1)),
    ((0, 1), (1, 0), (1, 1), (2, 0)),

    ((0, 0), (1, 0), (2, 0), (2, 1)),
    ((0, 0), (0, 1), (1, 1), (0, 2)),
    ((0, 1), (1, 1), (2, 1), (2, 0)),
]





def rotatek(block, k):
    new_block = []
    for loc in block:
        y, x = loc
        if k == 0:
            new_loc =  loc
        elif k == 1:
            new_loc = (-x, y)
        elif k == 2:
            new_loc = (-y, -x)
        else:
            new_loc =  (x, -y)
        new_block.append(new_loc)
    return tuple(new_block)

blocks = []
for b in range(len(initial_blocks)):
    block = initial_blocks[b]
    if b == 0:
        x = 1
    elif b <= 3:
        x = 2
    else:
        x = 4
    for k in range(0, x):
        blocks.append(rotatek(block, k))


def blocksum(block):
    result = 0
    for y in range(N):
        for x in range(M):
            cur_result = 0
            for dy, dx in block:
                ny = y + dy
                nx = x + dx

                if not(0 <= ny < N and 0 <= nx < M):
                    cur_result = -1
                    break
                cur_result += arr[ny][nx]
            result = max(result, cur_result)
    return result


ans = -1
for block in blocks:
    ans = max(ans, blocksum(block))
print(ans)