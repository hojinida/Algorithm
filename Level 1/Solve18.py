"""
문제 설명
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건
s의 길이는 1 이상 5이하입니다.
s의 맨앞에는 부호(+, -)가 올 수 있습니다.
s는 부호와 숫자로만 이루어져있습니다.
s는 "0"으로 시작하지 않습니다.
"""

# int()를 사용한 경우
"""
def solution(s): 
    return int(s)
"""


# int()를 사용하지 않은 경우

def solution(s):
    answer = 0
    for i, data in enumerate(s[::-1]):
        if data == '-':
            answer *= -1
        elif data == '+':
            continue
        else:
            answer += (ord(data) - 48) * (10 ** i)
    return answer


# 아래 코드는 테스트 코드 입니다.
print(solution("+1234"))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
