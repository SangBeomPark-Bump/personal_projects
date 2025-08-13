import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

string = input().strip('\n')
N = int(input())

arr = [input().strip('\n') for _ in range(N)]

dt = []
for word in arr:
    temp = [0 for _ in range(26)]
    for letter in word:
        temp[ord(letter) - 97] +=1
    dt.append(temp)

def converter(string):
    return ord(string) - 97

def howmuch(str1, str2):
    value = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            value +=1
    return value

INF = float('inf')
dp = [INF for _ in range(len(string))]
visited = [False for _ in range(len(string))]

def recursive(start):
    if start == len(string):
        return 0
    
    if visited[start]:
        return dp[start]
    
    visited[start] = True
    freq_arr = [0 for _ in range(26)]
    word = ''

    for next_end in range(start, len(string)):
        freq_arr[converter(string[next_end])] +=1
        word += string[next_end]
        for word_index, word_freq_arr in enumerate(dt): ## 50번
            if word_freq_arr == freq_arr: ## 26번
                dp[start] = min(dp[start], howmuch(word, arr[word_index]) + recursive(next_end+1))

    return dp[start]


ans = recursive(0)

print(-1 if ans == INF else ans)