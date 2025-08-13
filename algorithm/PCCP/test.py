def solution(diffs, times, limit):
    N = len(diffs)

    # 이전 퍼즐 시간
    prev_times = [0] * N
    for i in range(1, N):
        prev_times[i] = times[i - 1]

    # 이분 탐색 범위: 숙련도는 1 이상 max(diffs)
    left, right = 1, max(diffs)
    answer = right + 1  # 불가능할 때를 대비

    while left <= right:
        mid = (left + right) // 2  # 테스트할 숙련도
        total = 0

        # 총 소요 시간 계산
        for i in range(N):
            diff, t_cur, t_prev = diffs[i], times[i], prev_times[i]
            mistakes = max(diff - mid, 0)
            # 틀릴 때마다 (t_cur + t_prev), 마지막에 한 번 더 t_cur
            total += mistakes * (t_cur + t_prev) + t_cur
            if total > limit:
                break

        if total <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer if answer <= max(diffs) else 0
