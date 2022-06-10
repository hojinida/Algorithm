"""
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
"""


def solution(s):
    return s[(len(s) - 1) // 2:len(s) // 2 + 1]


# 아래 코드는 테스트 코드 입니다.
print(solution("foky"))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
