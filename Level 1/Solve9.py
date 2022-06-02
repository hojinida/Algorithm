"""
문제 설명
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.
"""


def solution(num):
    return "Even" if num % 2==0 else "Odd"


# 아래 코드는 테스트 코드 입니다.
print(solution(0))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
