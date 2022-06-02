"""
문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.
"""


def solution(n, m):
    Max, Min = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = Max % Min
        Max, Min = Min, t
    answer = [Max, int((n * m) / Max)]
    return answer


# 아래 코드는 테스트 코드 입니다.
print(solution(60, 48))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
