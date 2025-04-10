import sys
input = sys.stdin.readline
verbose = False

def eratosthenes(num:int = 1000000):
    MAX = num + 1
    LIM = int(num ** 0.5) + 1
    RSET = lambda strt, end, gap: set(range(strt, end, gap))
    
    # 5 (mod 6)과 1 (mod 6)을 참으로 설정한다. 이들은 2의 배수도 아니고 3의 배수도 아닌 숫자집합이다.
    # 단, 1은 소수가 아니기에 1 (mod 6)은 7부터 시작한다.
    prime = RSET(5, MAX, 6) | RSET(7, MAX, 6)
    if num > 2: prime.add(3) # 3 추가
    if num > 1: prime.add(2) # 2 추가
    for i in range(5, LIM, 6):
        # 5 (mod 6) 부분
        if i in prime:
            prime -= RSET(i * i, MAX, i * 6) | RSET(i * (i + 2), MAX, i * 6)
        # 1 (mod 6) 부분
        j = i + 2
        if j in prime:
            prime -= RSET(j * j, MAX, j * 6) | RSET(j * (j + 4), MAX, j * 6)

    return prime

N = int(input())

prime_numbers =  sorted(list(eratosthenes(N)))

prime_len =  len(prime_numbers)
start = prime_len-1
end = prime_len-1

temp_sum = sum(prime_numbers[start:end+1])

result = 0
while True:
    if N == 1:
        break
    else:
        if temp_sum < N :
            if start == 0:
                break
            start -=1
            temp_sum += prime_numbers[start]
        elif temp_sum > N:
            temp_sum -= prime_numbers[end]
            if end == 0:
                break
            end -=1
        else :
            result+=1
            if verbose:
                print(prime_numbers[start], prime_numbers[end], temp_sum)
            if start == 0:
                break
            start -=1
            temp_sum += prime_numbers[start]

        if verbose:
            print(start, end)
            print(prime_numbers[start], prime_numbers[end])
            print(temp_sum)
            print('-' * 10)
print(result)