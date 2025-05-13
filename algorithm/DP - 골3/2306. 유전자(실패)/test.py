string = input()

sad_dict = {
    'a' : 0,
    't' : 0,
    'g' : 1,
    'c' : 1,
}

dp = [0,0]

hehe = 0
for letter in string:
    kind= sad_dict[letter]

    if letter == 'a' or letter == 'g':
        dp[kind] += 1
    if letter == 't' or letter == 'c':
        if dp[kind]:
            dp[kind] -=1
            hehe +=2
    # print(letter, dp, hehe, string)
    

print(hehe)
