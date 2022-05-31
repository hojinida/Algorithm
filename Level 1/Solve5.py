"""
문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.
"""


def solution(x):
    return x % sum([int(n) for n in str(x)]) == 0


# 아래 코드는 테스트 코드 입니다.
print(solution(10))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
