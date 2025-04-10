import sys
input = sys.stdin.readline
verbose = False

letters = ['A', 'C', 'G', 'T']

S, P = map(int, input().split())
dna = input()
freq_list = list(map(int, input().split()))

letter_dict = {letter : freq  for letter, freq in zip(letters, freq_list)}
freq_dict = {letter : 0  for letter in letters}

result = 0

## P번 반복
for i in dna[:P]:
    freq_dict[i] +=1

def freq_test():
    for letter in letters:
        if letter_dict[letter] > freq_dict[letter]:
            return False
    return True

result += int(freq_test())

### (S-P) * 4번 반복
for i in range(S - P):
    freq_dict[dna[i]] -= 1
    freq_dict[dna[i+P]] += 1
    result += int(freq_test())

print(result)