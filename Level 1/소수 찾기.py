"""
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
"""

import math


def primeNum(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False;
    return True


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if primeNum(i):
            answer += 1
    return answer


# 아래 코드는 테스트 코드 입니다.
print(solution(10))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
