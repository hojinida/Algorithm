def solution(name):
    def move(target):
        return min(ord(target) - ord('A'), ord('Z') - ord(target) + 1)

    n = len(name)
    answer = 0

    # 1. 알파벳 변경 횟수 계산
    answer += sum(move(c) for c in name)

    # 2. 좌우 이동 최소 거리 계산
    min_move = n - 1  # 기본적으로 끝까지 가는 경우

    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == "A":  # 연속된 A를 건너뜀
            next_idx += 1

        # 1) 오른쪽으로 쭉 가는 경우 vs
        # 2) 오른쪽 갔다가 되돌아오는 경우 vs
        # 3) 왼쪽으로 갔다가 다시 오른쪽 가는 경우 비교
        min_move = min(
            min_move,
            2 * i + (n - next_idx),  # 오른쪽으로 갔다가 되돌아오기
            i + 2 * (n - next_idx)   # 왼쪽으로 갔다가 돌아가기
        )

    answer += min_move
    return answer
