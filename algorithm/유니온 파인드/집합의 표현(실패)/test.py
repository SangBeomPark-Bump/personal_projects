import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())

numbers = [0 for _ in range(N+1)]
sets = [set()]

temp = 0
# for com, num1, num2 in arr:
for _ in range(M):
    com, num1, num2 = map(int, input().split())
    num1_set = numbers[num1]
    num2_set = numbers[num2]
    if com == 0:
        if num1 != num2:
            if num1_set == 0 and num2_set ==0:
                temp +=1
                sets.append(set((num1, num2)))
                numbers[num1] = temp
                numbers[num2] = temp

            elif num1_set != 0 and num2_set == 0:
                sets[num1_set].add(num2)
                numbers[num2] =  num1_set

            elif num2_set != 0 and num1_set == 0:
                sets[num2_set].add(num1)
                numbers[num1] =  num2_set
            else:
                sets[num1_set] = (sets[num1_set].union(sets[num2_set]))
                numbers[num2] = num1_set
    elif com == 1:
        print("YES" if num1_set == num2_set else "NO")