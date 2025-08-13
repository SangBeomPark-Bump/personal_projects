import sys
input = sys.stdin.readline
import math


N, ATT = map(int, input().split())
arr = [list(map(int, input().split() ) ) for _ in range(N)]

def fight(hero, enemy):
    h_att, h_hp = hero
    e_att, e_hp = enemy
    e_hp = max(0, e_hp - h_att)
    e_att_turns = math.ceil(e_hp / h_att)
    return [h_att, max(0, h_hp - e_att_turns * e_att)]

def rest(hero,  potion, MAXH):
    h_att, h_hp = hero
    p_att, p_hp = potion

    h_att += p_att
    h_hp = min(MAXH,  h_hp + p_hp)

    return [h_att, h_hp]

def calc(MAXH):
    hero = [ATT, MAXH]

    for t, att, hp in arr:
        # print(hero, (att, hp), "MONSTER" if t - 2 else "POTION")
        if t - 1:
            hero = rest(hero, [att, hp], MAXH)
        else:
            hero = fight(hero, [att, hp])
        if not hero[1]:
            return False
    
    return True

start = 1
end = int(1e18)


result = end
while start <= end:
    mid = (start + end) // 2
    win = calc(mid)
    if win:
        end = mid - 1
        result = mid
    else:
        start = mid +1

print(result)