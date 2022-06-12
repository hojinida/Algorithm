"""
문제 설명
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.
"""


def solution(n):
    s = ""
    while n:
        s += str(n % 3)
        n //= 3
    return int(s, 3)


# 아래 코드는 테스트 코드 입니다.
print(solution(1253))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
