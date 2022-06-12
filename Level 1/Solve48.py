"""
문제 설명
0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ numbers의 길이 ≤ 9
0 ≤ numbers의 모든 원소 ≤ 9
numbers의 모든 원소는 서로 다릅니다.
"""


def solution(numbers):
    return sum(set(range(10)) - set(numbers))


# 아래 코드는 테스트 코드 입니다.
print(solution([1, 2, 3, 4, 5, 6, 7]))
# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
