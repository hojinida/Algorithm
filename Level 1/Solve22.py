"""
문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
"""


def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for i in map(ord, s):
        if i < 48 or i > 58:
            return False
    return True


# 아래 코드는 테스트 코드 입니다.
print(solution("1253"))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
