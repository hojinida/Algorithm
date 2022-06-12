"""
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
"""


def solution(n):
    return int("".join(sorted(str(n), reverse=True)))


# 아래 코드는 테스트 코드 입니다.
print(solution(991107))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
