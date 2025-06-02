import sys
MOD = 10**9 + 7

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    # 가능한 높이 검사
    for i in range(n):
        if arr[i] != -1 and arr[i] > min(i, n-1-i):
            print(0)
            return
            
    if n == 1:
        print(1)
        return
        
    max_height = (n-1) // 2
    dp0 = [0] * (max_height + 1)
    dp1 = [0] * (max_height + 1)
    dp1[0] = 1  # 초기 상태 (i=-1 가정)
    
    for i in range(n):
        cur = i % 2
        pre = 1 - cur
        dp_cur = dp0 if cur == 0 else dp1
        dp_pre = dp1 if pre == 1 else dp0
        
        # 현재 dp_cur 초기화
        for j in range(len(dp_cur)):
            dp_cur[j] = 0
            
        h_max = min(i, n-1-i)
        
        if arr[i] != -1:
            x = arr[i]
            if x > h_max:
                # 이미 검사했으므로 0
                continue
            for dx in (-1, 0, 1):
                prev_x = x + dx
                if 0 <= prev_x < len(dp_pre):
                    dp_cur[x] = (dp_cur[x] + dp_pre[prev_x]) % MOD
        else:
            for x in range(h_max + 1):
                if x >= len(dp_cur):
                    break
                total = 0
                for dx in (-1, 0, 1):
                    prev_x = x + dx
                    if 0 <= prev_x < len(dp_pre):
                        total = (total + dp_pre[prev_x]) % MOD
                dp_cur[x] = total % MOD
                
        if i == n - 1:
            print(dp_cur[0] % MOD)
            return

if __name__ == '__main__':
    main()