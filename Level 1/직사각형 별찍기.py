"""
문제 설명
이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

제한 조건
n과 m은 각각 1000 이하인 자연수입니다.
"""


def solution(arr1, arr2):
    answer = [[a + b for a, b in zip(A, B)] for A, B in zip(arr1, arr2)]

    return answer


# 아래 코드는 테스트 코드 입니다.
print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
