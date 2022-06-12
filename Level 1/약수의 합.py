"""
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.
"""


def solution(n):
    return n + sum([int(i) for i in range(1, (n // 2) + 1) if n % i == 0])


# 아래 코드는 테스트 코드 입니다.
print(solution(25))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
